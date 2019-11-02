import torch
from torch3d.extension import _lazy_import


def cdist(x, y):
    xx = x.pow(2).sum(dim=2, keepdim=True)
    yy = y.pow(2).sum(dim=2, keepdim=True).transpose(2, 1)
    sqdist = torch.baddbmm(yy, x, y.transpose(2, 1), alpha=-2).add_(xx)
    return sqdist


def batched_index_select(x, dim, index):
    views = [x.shape[0]] + [1 if i != dim else -1 for i in range(1, len(x.shape))]
    expanse = list(x.shape)
    expanse[0] = -1
    expanse[dim] = -1
    index = index.view(views).expand(expanse)
    return torch.gather(x, dim, index)


def knn(q, p, k):
    sqdist = cdist(q, p)
    return torch.topk(sqdist, k, dim=2, largest=False)


def chamfer_loss(x, y):
    sqdist = cdist(x, y)
    return torch.mean(sqdist.min(1)[0]) + torch.mean(sqdist.min(2)[0])


def random_point_sample(p, num_samples):
    num_points = p.shape[1]
    if num_samples > num_points:
        raise ValueError("num_samples should be less than input size.")
    return torch.randperm(num_points)[:num_samples]


def farthest_point_sample(p, num_samples):
    num_points = p.shape[1]
    if num_samples > num_points:
        raise ValueError("num_samples should be less than input size.")
    _C = _lazy_import()
    return _C.farthest_point_sample(p, num_samples)
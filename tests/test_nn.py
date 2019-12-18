import torch
import torch3d.nn as nn
import torch3d.nn.functional as F


def test_conv():
    names = ["EdgeConv", "SetConv"]
    batch_size = 2
    in_channels = 3
    out_channels = 64
    kernel_size = 32
    num_points = 1024
    radius = 0.1
    x = torch.rand(batch_size, in_channels, num_points)

    for name in names:
        cls = getattr(nn, name)
        if name == "SetConv":
            size = torch.Size([batch_size, out_channels + 3, num_points])
            conv = cls(in_channels, out_channels, kernel_size, radius=radius)
        else:
            size = torch.Size([batch_size, out_channels, num_points])
            conv = cls(in_channels, out_channels, kernel_size)
        assert conv(x).shape == size


def test_farthest_point_sample():
    batch_size = 1
    num_samples = 2
    in_channels = 3
    p = torch.tensor(
        [
            [
                [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
                [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0],
            ]
        ]
    )
    size = torch.Size([batch_size, in_channels, num_samples])
    q = F.farthest_point_sample(p, num_samples)
    assert q.shape == size
    assert q.tolist() == [[[0.0, 1.0], [0.0, 1.0], [0.0, 1.0]]]


def test_ball_point():
    batch_size = 1
    in_channels = 3
    k = 2
    radius = 0.5
    p = torch.tensor(
        [
            [
                [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0],
                [0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
                [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0],
            ]
        ]
    )
    num_points = p.shape[2]
    size = torch.Size([batch_size, k, num_points])
    index = F.ball_point(p, p, k, radius)
    assert index.shape == size
    assert index.tolist() == [[[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]]]

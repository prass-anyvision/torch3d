torch3d
=======

[![Downloads](https://pepy.tech/badge/torch3d)](https://pepy.tech/project/torch3d)

The torch3d package consists of datasets, model architectures, and common
operations for 3D deep learning.

Why torch3d?
------------

For 3D domain, there is currently no official support from PyTorch that likes
[torchvision](https://github.com/pytorch/vision) for images. Torch3d aims to
fill this gap by streamlining the prototyping process of deep neural networks
on discrete 3D domain. Currently, it focuses on deep learning methods on 3D
point clouds.

The following network architectures are currently included:
- **PointNet** from Qi et al. (CVPR 2017) [[arXiv](https://arxiv.org/abs/1612.00593)]
- **PointCNN** from Li et al. (NeurIPS 2018) [[arXiv](https://arxiv.org/abs/1801.07791)]

Installation
------------

Required PyTorch 1.2 or newer. Some other dependencies are:
- torchvision (only needed to download datasets, may consider dropping it later)
- h5py

From PyPi:
```bash
pip install torch3d
```

From source:
```bash
git clone https://github.com/pqhieu/torch3d
cd torch3d
python setup.py install
```

Roadmap
-------

**0.2.0**
- [ ] PointNet++ model
- [ ] Transforms: jitter, random rotation
- [X] Datasets: ShapeNetPart

**0.1.0**
- [X] PointCNN model
- [X] Publish on PyPi

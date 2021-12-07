from torchvision import datasets

from isl.datasets.dataset import Dataset


class CIFAR10(Dataset):

    def __init__(self, *args, **kwargs) -> None:
        super(CIFAR10, self).__init__(*args, **kwargs)

        self._train = datasets.CIFAR10(self._cache_dir, train=True, download=self._download)
        self._test = datasets.CIFAR10(self._cache_dir, train=False, download=False)

        self._n_class = len(self._train.classes)
        self._n_train = len(self._train)
        self._n_test = len(self._test)


class CIFAR100(Dataset):

    def __init__(self, *args, **kwargs) -> None:
        super(CIFAR100, self).__init__(*args, **kwargs)

        self._train = datasets.CIFAR100(self._cache_dir, train=True, download=self._download)
        self._test = datasets.CIFAR100(self._cache_dir, train=False, download=False)

        self._n_class = len(self._train.classes)
        self._n_train = len(self._train)
        self._n_test = len(self._test)

"""
Exceptions.
"""


class KubernetesError(Exception):
    """
    Base exception for all Kubernetes errors.
    """
    pass


class PyKubeError(KubernetesError):
    """
    PyKube specific errors.
    """
    pass


class HTTPError(PyKubeError):
    def __init__(self, code, message):
        raise NotImplementedError


class ObjectDoesNotExist(PyKubeError):
    pass

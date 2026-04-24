import time


class ReplicatedMixin(object):

    scalable_attr = "replicas"

    @property
    def replicas(self):
        pass

    @replicas.setter
    def replicas(self, value):
        pass


class ScalableMixin(object):

    @property
    def scalable(self):
        pass

    @scalable.setter
    def scalable(self, value):
        pass

    def scale(self, replicas=None):
        pass

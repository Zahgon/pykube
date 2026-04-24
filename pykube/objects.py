import copy
import json
import os.path as op
from inspect import getmro
import six

from six.moves.urllib.parse import urlencode
from .exceptions import ObjectDoesNotExist
from .mixins import ReplicatedMixin, ScalableMixin
from .query import Query
from .utils import obj_merge


class ObjectManager(object):
    def __call__(self, api, namespace=None):
        raise NotImplementedError

    def __get__(self, obj, api_obj_class):
        raise NotImplementedError


@six.python_2_unicode_compatible
class APIObject(object):

    objects = ObjectManager()
    base = None
    namespace = None

    def __init__(self, api, obj):
        raise NotImplementedError

    def set_obj(self, obj):
        pass

    def __repr__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    @property
    def name(self):
        pass

    @property
    def metadata(self):
        pass

    @property
    def labels(self):
        pass

    @property
    def annotations(self):
        pass

    def api_kwargs(self, **kwargs):
        pass

    def exists(self, ensure=False):
        pass

    def create(self):
        pass

    def reload(self):
        pass

    def watch(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class NamespacedAPIObject(APIObject):

    @property
    def namespace(self):
        pass


def object_factory(api, api_version, kind):
    """
    Dynamically builds a Python class for the given Kubernetes object in an API.

    For example:

        api = pykube.HTTPClient(...)
        NetworkPolicy = pykube.object_factory(api, "networking.k8s.io/v1", "NetworkPolicy")

    This enables construction of any Kubernetes object kind without explicit support
    from pykube.

    Currently, the HTTPClient passed to this function will not be bound to the returned type.
    It is planned to fix this, but in the mean time pass it as you would normally.
    """
    raise NotImplementedError


class ConfigMap(NamespacedAPIObject):

    version = "v1"
    endpoint = "configmaps"
    kind = "ConfigMap"


class CronJob(NamespacedAPIObject):

    version = "batch/v2alpha1"
    endpoint = "cronjobs"
    kind = "CronJob"


class DaemonSet(NamespacedAPIObject):

    version = "extensions/v1beta1"
    endpoint = "daemonsets"
    kind = "DaemonSet"


class Deployment(NamespacedAPIObject, ReplicatedMixin, ScalableMixin):

    version = "extensions/v1beta1"
    endpoint = "deployments"
    kind = "Deployment"

    @property
    def ready(self):
        pass

    def rollout_undo(self, target_revision=None):
        """Produces same action as kubectl rollout undo deployment command.
        Input variable is revision to rollback to (in kubectl, --to-revision)
        """
        pass


class Endpoint(NamespacedAPIObject):

    version = "v1"
    endpoint = "endpoints"
    kind = "Endpoint"


class Event(NamespacedAPIObject):

    version = "v1"
    endpoint = "events"
    kind = "Event"


class LimitRange(NamespacedAPIObject):

    version = "v1"
    endpoint = "limitranges"
    kind = "LimitRange"


class ResourceQuota(NamespacedAPIObject):

    version = "v1"
    endpoint = "resourcequotas"
    kind = "ResourceQuota"


class ServiceAccount(NamespacedAPIObject):

    version = "v1"
    endpoint = "serviceaccounts"
    kind = "ServiceAccount"


class Ingress(NamespacedAPIObject):

    version = "extensions/v1beta1"
    endpoint = "ingresses"
    kind = "Ingress"


class ThirdPartyResource(APIObject):

    version = "extensions/v1beta1"
    endpoint = "thirdpartyresources"
    kind = "ThirdPartyResource"


class Job(NamespacedAPIObject, ScalableMixin):

    version = "batch/v1"
    endpoint = "jobs"
    kind = "Job"
    scalable_attr = "parallelism"

    @property
    def parallelism(self):
        pass

    @parallelism.setter
    def parallelism(self, value):
        pass


class Namespace(APIObject):

    version = "v1"
    endpoint = "namespaces"
    kind = "Namespace"


class Node(APIObject):

    version = "v1"
    endpoint = "nodes"
    kind = "Node"

    @property
    def unschedulable(self):
        pass

    @unschedulable.setter
    def unschedulable(self, value):
        pass

    def cordon(self):
        pass

    def uncordon(self):
        pass


class Pod(NamespacedAPIObject):

    version = "v1"
    endpoint = "pods"
    kind = "Pod"

    @property
    def ready(self):
        pass

    def logs(self, container=None, pretty=None, previous=False,
             since_seconds=None, since_time=None, timestamps=False,
             tail_lines=None, limit_bytes=None):
        """
        Produces the same result as calling kubectl logs pod/<pod-name>.
        Check parameters meaning at
        http://kubernetes.io/docs/api-reference/v1/operations/,
        part 'read log of the specified Pod'. The result is plain text.
        """
        pass


class ReplicationController(NamespacedAPIObject, ReplicatedMixin, ScalableMixin):

    version = "v1"
    endpoint = "replicationcontrollers"
    kind = "ReplicationController"

    @property
    def ready(self):
        pass


class ReplicaSet(NamespacedAPIObject, ReplicatedMixin, ScalableMixin):

    version = "extensions/v1beta1"
    endpoint = "replicasets"
    kind = "ReplicaSet"


class Secret(NamespacedAPIObject):

    version = "v1"
    endpoint = "secrets"
    kind = "Secret"


class Service(NamespacedAPIObject):

    version = "v1"
    endpoint = "services"
    kind = "Service"


class PersistentVolume(APIObject):

    version = "v1"
    endpoint = "persistentvolumes"
    kind = "PersistentVolume"


class PersistentVolumeClaim(NamespacedAPIObject):

    version = "v1"
    endpoint = "persistentvolumeclaims"
    kind = "PersistentVolumeClaim"


class HorizontalPodAutoscaler(NamespacedAPIObject):

    version = "autoscaling/v1"
    endpoint = "horizontalpodautoscalers"
    kind = "HorizontalPodAutoscaler"


class PetSet(NamespacedAPIObject):

    version = "apps/v1alpha1"
    endpoint = "petsets"
    kind = "PetSet"


class StatefulSet(NamespacedAPIObject, ReplicatedMixin, ScalableMixin):

    version = "apps/v1beta1"
    endpoint = "statefulsets"
    kind = "StatefulSet"


class Role(NamespacedAPIObject):

    version = "rbac.authorization.k8s.io/v1alpha1"
    endpoint = "roles"
    kind = "Role"


class RoleBinding(NamespacedAPIObject):

    version = "rbac.authorization.k8s.io/v1alpha1"
    endpoint = "rolebindings"
    kind = "RoleBinding"


class ClusterRole(APIObject):

    version = "rbac.authorization.k8s.io/v1alpha1"
    endpoint = "clusterroles"
    kind = "ClusterRole"


class ClusterRoleBinding(APIObject):

    version = "rbac.authorization.k8s.io/v1alpha1"
    endpoint = "clusterrolebindings"
    kind = "ClusterRoleBinding"


class PodSecurityPolicy(APIObject):

    version = "extensions/v1beta1"
    endpoint = "podsecuritypolicies"
    kind = "PodSecurityPolicy"

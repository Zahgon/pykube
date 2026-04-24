import logging
import math
import time

from .objects import Pod
from .exceptions import KubernetesError


logger = logging.getLogger(__name__)


class RollingUpdater(object):

    def __init__(self, api, old_rc, new_rc, **kwargs):
        raise NotImplementedError

    def update(self):
        pass

    def scale_up(self, new_rc, old_rc, original, desired, max_surge, max_unavailable):
        # if we're already at the desired, do nothing.
        pass

    def scale_down(self, new_rc, old_rc, desired, min_available, max_surge):
        # already scaled down; do nothing.
        pass

    def cleanup(self, old_rc, new_rc):
        pass

    def poll_for_ready_pods(self, old_rc, new_rc):
        pass

    def create_rc(self, rc):
        pass


def extract_max_value(field, name, value):
    pass

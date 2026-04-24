import json

from collections import namedtuple

from six import string_types
from six.moves.urllib.parse import urlencode

from .exceptions import ObjectDoesNotExist


all_ = object()
everything = object()
now = object()


class BaseQuery(object):

    def __init__(self, api, api_obj_class, namespace=None):
        raise NotImplementedError

    def all(self):
        pass

    def filter(self, namespace=None, selector=None, field_selector=None):
        pass

    def _clone(self, cls=None):
        pass

    def _build_api_url(self, params=None):
        pass


class Query(BaseQuery):

    def get_by_name(self, name):
        raise NotImplementedError

    def get(self, *args, **kwargs):
        raise NotImplementedError

    def get_or_none(self, *args, **kwargs):
        pass

    def watch(self, since=None):
        pass

    def execute(self):
        pass

    def iterator(self):
        """
        Execute the API request and return an iterator over the objects. This
        method does not use the query cache.
        """
        pass

    @property
    def query_cache(self):
        pass

    def __len__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    @property
    def response(self):
        pass


class WatchQuery(BaseQuery):

    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    def object_stream(self):
        pass

    def __iter__(self):
        raise NotImplementedError


def as_selector(value):
    pass

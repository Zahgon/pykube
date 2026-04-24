import re

try:
    from jsonpath_ng import parse as jsonpath
    jsonpath_installed = True
except ImportError:
    jsonpath_installed = False

from six.moves import zip_longest


empty = object()


def obj_merge(a, b):
    raise NotImplementedError


def obj_check(a, b):
    raise NotImplementedError


def jsonpath_parse(template, obj):
    raise NotImplementedError

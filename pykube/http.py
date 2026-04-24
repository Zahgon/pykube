"""
HTTP request related code.
"""

import datetime
import json
import posixpath
import re
import shlex
import subprocess

try:
    import google.auth
    from google.auth.transport.requests import Request as GoogleAuthRequest
    google_auth_installed = True
except ImportError:
    google_auth_installed = False

import requests.adapters

from six.moves import http_client
from six.moves.urllib.parse import urlparse

from .exceptions import HTTPError
from .utils import jsonpath_installed, jsonpath_parse


_ipv4_re = re.compile(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")


class KubernetesHTTPAdapterSendMixin(object):

    def _persist_credentials(self, config, token, expiry):
        pass

    def _auth_gcp(self, request, token, expiry, config):
        pass

    def send(self, request, **kwargs):
        pass


class KubernetesHTTPAdapter(KubernetesHTTPAdapterSendMixin, requests.adapters.HTTPAdapter):

    def __init__(self, kube_config, **kwargs):
        raise NotImplementedError


class HTTPClient(object):
    """
    Client for interfacing with the Kubernetes API.
    """

    _session = None

    def __init__(self, config):
        """
        Creates a new instance of the HTTPClient.

        :Parameters:
           - `config`: The configuration instance
        """
        raise NotImplementedError

    @property
    def url(self):
        pass

    @url.setter
    def url(self, value):
        pass

    @property
    def version(self):
        """
        Get Kubernetes API version
        """
        pass

    def resource_list(self, api_version):
        raise NotImplementedError

    def get_kwargs(self, **kwargs):
        """
        Creates a full URL to request based on arguments.

        :Parametes:
           - `kwargs`: All keyword arguments to build a kubernetes API endpoint
        """
        raise NotImplementedError

    def raise_for_status(self, resp):
        raise NotImplementedError

    def request(self, *args, **kwargs):
        """
        Makes an API request based on arguments.

        :Parameters:
           - `args`: Non-keyword arguments
           - `kwargs`: Keyword arguments
        """
        pass

    def get(self, *args, **kwargs):
        """
        Executes an HTTP GET.

        :Parameters:
           - `args`: Non-keyword arguments
           - `kwargs`: Keyword arguments
        """
        raise NotImplementedError

    def options(self, *args, **kwargs):
        """
        Executes an HTTP OPTIONS.

        :Parameters:
           - `args`: Non-keyword arguments
           - `kwargs`: Keyword arguments
        """
        pass

    def head(self, *args, **kwargs):
        """
        Executes an HTTP HEAD.

        :Parameters:
           - `args`: Non-keyword arguments
           - `kwargs`: Keyword arguments
        """
        pass

    def post(self, *args, **kwargs):
        """
        Executes an HTTP POST.

        :Parameters:
           - `args`: Non-keyword arguments
           - `kwargs`: Keyword arguments
        """
        pass

    def put(self, *args, **kwargs):
        """
        Executes an HTTP PUT.

        :Parameters:
           - `args`: Non-keyword arguments
           - `kwargs`: Keyword arguments
        """
        pass

    def patch(self, *args, **kwargs):
        """
        Executes an HTTP PATCH.

        :Parameters:
           - `args`: Non-keyword arguments
           - `kwargs`: Keyword arguments
        """
        pass

    def delete(self, *args, **kwargs):
        """
        Executes an HTTP DELETE.

        :Parameters:
           - `args`: Non-keyword arguments
           - `kwargs`: Keyword arguments
        """
        pass

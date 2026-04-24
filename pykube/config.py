"""
Configuration code.
"""

import base64
import copy
import tempfile
import os

import yaml

from pykube import exceptions


class KubeConfig(object):
    """
    Main configuration class.
    """

    @classmethod
    def from_service_account(cls, path="/var/run/secrets/kubernetes.io/serviceaccount", **kwargs):
        pass

    @classmethod
    def from_file(cls, filename, **kwargs):
        """
        Creates an instance of the KubeConfig class from a kubeconfig file.

        :Parameters:
           - `filename`: The full path to the configuration file
        """
        pass

    @classmethod
    def from_url(cls, url, **kwargs):
        """
        Creates an instance of the KubeConfig class from a single URL (useful
        for interacting with kubectl proxy).
        """
        pass

    def __init__(self, doc, current_context=None):
        """
        Creates an instance of the KubeConfig class.
        """
        raise NotImplementedError

    def set_current_context(self, value):
        """
        Sets the context to the provided value.

        :Parameters:
           - `value`: The value for the current context
        """
        pass

    @property
    def current_context(self):
        pass

    @property
    def clusters(self):
        """
        Returns known clusters by exposing as a read-only property.
        """
        pass

    @property
    def users(self):
        """
        Returns known users by exposing as a read-only property.
        """
        pass

    @property
    def contexts(self):
        """
        Returns known contexts by exposing as a read-only property.
        """
        pass

    @property
    def cluster(self):
        """
        Returns the current selected cluster by exposing as a
        read-only property.
        """
        pass

    @property
    def user(self):
        """
        Returns the current user set by current context
        """
        pass

    @property
    def namespace(self):
        """
        Returns the current context namespace by exposing as a read-only property.
        """
        pass

    def persist_doc(self):
        pass

    def reload(self):
        pass


class BytesOrFile(object):
    """
    Implements the same interface for files and byte input.
    """

    @classmethod
    def maybe_set(cls, d, key):
        pass

    def __init__(self, filename=None, data=None):
        """
        Creates a new instance of BytesOrFile.

        :Parameters:
           - `filename`: A full path to a file
           - `data`: base64 encoded bytes
        """
        raise NotImplementedError

    def bytes(self):
        """
        Returns the provided data as bytes.
        """
        pass

    def filename(self):
        """
        Returns the provided data as a file location.
        """
        pass

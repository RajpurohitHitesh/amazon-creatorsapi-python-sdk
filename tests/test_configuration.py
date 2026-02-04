"""Tests for Configuration class."""
import pytest
from creatorsapi_python_sdk.configuration import Configuration


def test_configuration_initialization():
    """Test that Configuration can be instantiated with defaults."""
    config = Configuration()
    assert config is not None


def test_configuration_host_setter():
    """Test that host can be set on Configuration."""
    config = Configuration()
    config.host = "https://custom.api.endpoint.com"
    assert config.host == "https://custom.api.endpoint.com"


def test_configuration_access_token():
    """Test access token can be set."""
    config = Configuration()
    config.access_token = "test-token-123"
    assert config.access_token == "test-token-123"

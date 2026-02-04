"""Tests for API client."""
import pytest
from creatorsapi_python_sdk.api_client import ApiClient
from creatorsapi_python_sdk.configuration import Configuration


def test_api_client_initialization():
    """Test that ApiClient can be instantiated with default configuration."""
    config = Configuration()
    client = ApiClient(configuration=config)
    assert client is not None
    assert client.configuration is not None


def test_api_client_with_custom_host():
    """Test that ApiClient accepts custom host parameter."""
    config = Configuration()
    client = ApiClient(configuration=config, host="https://custom.example.com")
    assert client.configuration.host == "https://custom.example.com"

"""Tests for model classes."""
import pytest
from creatorsapi_python_sdk.models.money import Money
from creatorsapi_python_sdk.models.availability import Availability
from creatorsapi_python_sdk.models.item import Item


def test_money_model():
    """Test Money model instantiation."""
    money = Money(amount=10.99, currency="USD")
    assert money.amount == 10.99
    assert money.currency == "USD"


def test_availability_enum():
    """Test Availability enum values."""
    assert Availability.AVAILABLE == 'Available'
    assert Availability.INCLUDEOUTOFSTOCK == 'IncludeOutOfStock'


def test_item_model():
    """Test Item model instantiation."""
    item = Item(asin="B08N5WRWNW")
    assert item.asin == "B08N5WRWNW"

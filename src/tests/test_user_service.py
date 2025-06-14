import pytest

from services.user_service import UserService


def test_get_age_group_underage():
    assert UserService.get_age_group(10) == "underage"

def test_get_age_group_edge_underage():
    assert UserService.get_age_group(17) == "underage"

def test_get_age_group_adult():
    assert UserService.get_age_group(35) == "adult"

def test_get_age_group_senior():
    assert UserService.get_age_group(70) == "senior"

def test_get_age_group_invalid():
    with pytest.raises(ValueError, match="Edad invalida"):
        UserService.get_age_group(0)

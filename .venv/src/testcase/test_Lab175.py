import pytest
import allure

@pytest.mark.smoke
def test_sub0():
    assert 2-1 == 1

@pytest.mark.smoke
def test_sub1():
    assert 3-2 ==0

@pytest.mark.reg
def test_sub2():
    assert 1-1 ==0

@pytest.mark.skip(reason="Not completed, skip it")
def test_sub3():
    assert 0-1 ==0
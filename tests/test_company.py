import pytest

from company import Company


def test_init_default():
    company = Company()
    assert company.parent is None
    assert company.employee_count == 0


def test_init_with_parameters():
    parent_company = Company(employee_count=100)
    company = Company(parent=parent_company, employee_count=50)
    assert company.parent == parent_company
    assert company.employee_count == 50


@pytest.mark.parametrize("invalid_count", [-1, "ten", 1.5])
def test_init_invalid_employee_count(invalid_count):
    with pytest.raises((TypeError, ValueError)):
        Company(employee_count=invalid_count)


def test_set_parent():
    parent_company = Company(employee_count=100)
    company = Company()
    company.parent = parent_company
    assert company.parent == parent_company


def test_set_own_company_as_parent():
    company = Company()
    with pytest.raises(ValueError):
        company.parent = company


@pytest.mark.parametrize("valid_count", [0, 1, 100])
def test_set_valid_employee_count(valid_count):
    company = Company()
    company.employee_count = valid_count
    assert company.employee_count == valid_count


@pytest.mark.parametrize("invalid_count", [-1, "ten", 1.5])
def test_set_invalid_employee_count(invalid_count):
    company = Company()
    with pytest.raises((TypeError, ValueError)):
        company.employee_count = invalid_count

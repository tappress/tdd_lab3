import pytest

from company import Company, CompanyService


@pytest.fixture
def parent_company() -> Company:
    return Company(None, 100)


@pytest.fixture
def child_company1(parent_company: Company) -> Company:
    return Company(parent_company, 50)


@pytest.fixture
def child_company2(parent_company: Company) -> Company:
    return Company(parent_company, 30)


@pytest.fixture
def grandchild_company(child_company1: Company) -> Company:
    return Company(child_company1, 20)


@pytest.fixture
def great_grandchild_company(grandchild_company: Company) -> Company:
    return Company(grandchild_company, 10)


@pytest.fixture
def companies(
    parent_company: Company,
    child_company1: Company,
    child_company2: Company,
    grandchild_company: Company,
    great_grandchild_company: Company,
) -> list[Company]:
    return [
        parent_company,
        child_company1,
        child_company2,
        grandchild_company,
        great_grandchild_company,
    ]


@pytest.fixture
def service() -> CompanyService:
    return CompanyService()


def test_get_top_level_parent_for_top_level_company(
    parent_company: Company, service: CompanyService
):
    assert service.get_top_level_parent(parent_company) is parent_company


def test_get_top_level_parent_for_grandchild(
    grandchild_company: Company, service: CompanyService
):
    top_level_parent = service.get_top_level_parent(grandchild_company)

    assert top_level_parent.employee_count == 100


def test_employee_count_for_company_without_children(
    child_company2: Company, service: CompanyService
):
    # A company without children should return only its own employee count
    assert (
        service.get_employee_count_for_company_and_children(child_company2, [])
        == child_company2.employee_count
    )


def test_employee_count_with_nested_children(
    child_company1: Company,
    companies: list[Company],
    service: CompanyService,
):
    total_count = service.get_employee_count_for_company_and_children(
        child_company1, companies
    )

    assert total_count == 70  # Expected 50 (child) + 20 (grandchild)


def test_no_companies_provided(service: CompanyService):
    new_company = Company()

    assert service.get_employee_count_for_company_and_children(new_company, []) == 0


def test_circular_hierarchy_detection(service: CompanyService):
    parent_company = Company(None, 100)
    child_company = Company(parent_company, 50)
    parent_company.parent = child_company

    with pytest.raises(RecursionError):
        service.get_top_level_parent(child_company)

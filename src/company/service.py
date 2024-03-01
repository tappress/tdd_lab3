from company.api import ICompanyService
from company.model import Company


class CompanyService(ICompanyService):
    def get_top_level_parent(self, child: Company) -> Company:
        """
        Recursively finds the top level parent for the company.

        :param child: Company for whom we are searching the top level parent
        :return: top level parent
        """

        if child.parent is None:
            return child

        return self.get_top_level_parent(child.parent)

    def get_employee_count_for_company_and_children(
        self, company: Company, companies: list[Company]
    ) -> int:
        """
        Recursively calculates the total number of employees for the company and its children.

        :param company: Company for whom we are searching count of employees
        :param companies: List of all available companies
        :return: total count of employees
        """

        total_employees = company.employee_count

        for comp in companies:
            if comp.parent is company:
                total_employees += comp.employee_count

        return total_employees

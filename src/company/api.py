from abc import abstractmethod, ABC

from company.model import Company


class ICompanyService(ABC):
    @abstractmethod
    def get_top_level_parent(self, child: Company) -> Company:
        """
        Get the top level parent (parent of parent...) for the company.

        :param child: Company for whom we are searching the top level parent
        :return: top level parent
        """
        pass

    @abstractmethod
    def get_employee_count_for_company_and_children(
        self, company: Company, companies: list[Company]
    ) -> int:
        """
        Get the total employee count for the company and its children.

        :param company: Company for whom we are searching count of employees
        :param companies: List of all available companies
        :return: total count of employees
        """
        pass

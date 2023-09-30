"""Provides Publix weekly BOGO itmes."""
import re
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


class PublixBogo:
    """Obtain a list of Publix's weekly BOGO items.

    Args:
        store_number (str): Publix store number.
    """

    BASE_URL = "https://accessibleweeklyad.publix.com/PublixAccessibility/BrowseByListing/ByCategory/?StoreID"
    BOGO_ID = "CategoryID=5232540"

    def __init__(self, store_number: str) -> None:
        """Instantiate a PublixBogo Class instance."""
        self.store_number = store_number
        self.bogo_data = self._get_bogo_data()

    def _get_bogo_data(self) -> object:
        """Get the BOGO data via Publix"s Accessibility Site.

        Returns:
            (object): Output is a BeautifulSoup object.
        """
        url = f"{self.BASE_URL}={self.store_number}&{self.BOGO_ID}"
        try:
            bogo_data = requests.get(url, timeout=10)
            bogo_data.raise_for_status()
            bogo_soup = BeautifulSoup(bogo_data.text, "html.parser")
            return bogo_soup
        except RequestException as request_error:
            raise SystemExit(f"Erorr getting BOGO data: {request_error}")

    def get_date(self) -> str:
        """Parse the weekly BOGO date.

        Raises:
            (str): An error is raised if the date cannot be parsed from the Beautiful Soup data.

        Returns:
            (str): Output is the date as is from the Beautfiul Soup data with stripped whitespace.
        """
        try:
            raw_date = self.bogo_data.find("div", class_="action-elide validDates")
            date = raw_date.text
        except AttributeError as attribute_error:
            raise attribute_error

        return date.strip()

    def get_modified_date(self) -> str:
        """Parse the weekly BOGO date.

        Raises:
            (str): An error is raised if the date cannot be parsed from the Beautiful Soup data.

        Returns:
            (str): Output is a modified date using regex.
        """
        REGEX = r"(\d{1,2}/\d{1,2}\s-\s\d{1,2}/\d{1,2})"

        try:
            raw_date = self.bogo_data.find("div", class_="action-elide validDates")
            date = raw_date.text
            modified_date = re.search(REGEX, date).group()
        except AttributeError as attribute_error:
            raise attribute_error

        return modified_date

    def get_bogo_items(self) -> list:
        """Get a list of the weekly BOGO items.

        Returns:
            (list): Output is a sorted list of the weekly BOGO items.
        """
        bogo_items_list = []

        bogo_items = self.bogo_data.find_all("h2", class_="ellipsis_text")

        for item in bogo_items:
            bogo_item = item.text
            bogo_items_list.append(bogo_item)
        return sorted(bogo_items_list)

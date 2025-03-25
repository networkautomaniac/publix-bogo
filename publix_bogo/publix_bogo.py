"""Provides Publix Supermarkets weekly BOGO items."""

import re
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


class PublixBogo:
    """Obtain a list of Publix's weekly BOGO items.

    Args:
        store_number (int): Publix store number.
    """

    def __init__(self, store_number: int) -> None:
        """Instantiate a PublixBogo Class instance."""
        self.store_number = store_number
        self.bogo_data = self._get_bogo_data()

    def _get_bogo_data(self) -> BeautifulSoup:
        """Get the BOGO data via Publix's Accessibility Site.

        Raises:
            str: An error is raised if the bogo data cannot be retrieved.

        Returns:
            BeautifulSoup: Output is a BeautifulSoup object.
        """
        BASE_URL = "https://accessibleweeklyad.publix.com/PublixAccessibility/BrowseByListing/ByCategory/?StoreID"
        BOGO_ID = "CategoryID=5232540"

        url = f"{BASE_URL}={self.store_number}&{BOGO_ID}"
        try:
            bogo_data = requests.get(url, timeout=10)
            bogo_data.raise_for_status()
            bogo_soup = BeautifulSoup(bogo_data.text, "html.parser")

            return bogo_soup

        except RequestException as request_error:
            raise SystemExit(f"Error getting BOGO data: {request_error}")

    def get_date(self) -> str:
        """Parse the weekly BOGO date.

        Raises:
            ValueError: If the date cannot be parsed from the Beautiful Soup data.

        Returns:
            str: Output is the date as is from the Beautiful Soup data with stripped whitespace.
        """
        try:
            raw_date = self.bogo_data.find("div", class_="action-elide validDates")
            date = raw_date.text

            return date.strip()

        except AttributeError as attribute_error:
            raise attribute_error

    def get_modified_date(self) -> str:
        """Parse the weekly BOGO date.

        Raises:
            str: An error is raised if the date cannot be parsed from the Beautiful Soup data.

        Returns:
            str: Output is a modified date using regex.
        """
        REGEX = r"(\d{1,2}/\d{1,2}\s-\s\d{1,2}/\d{1,2})"

        try:
            raw_date = self.bogo_data.find("div", class_="action-elide validDates")
            date = raw_date.text
            modified_date = re.search(REGEX, date).group()

            return modified_date

        except AttributeError as attribute_error:
            raise attribute_error

    def get_bogo_items(self) -> list:
        """Get a list of the weekly BOGO items.

        Returns:
            list: Output is a sorted list of the weekly BOGO items.
        """
        bogo_items_list = []

        bogo_items = self.bogo_data.find_all("h2", class_="ellipsis_text")

        for item in bogo_items:
            bogo_item = item.text
            bogo_items_list.append(bogo_item)

        return sorted(bogo_items_list)


if __name__ == "__main__":
    # Palm Crossings Store Number.
    PALM_CROSSINGS = 2500579

    bogo_data = PublixBogo(store_number=PALM_CROSSINGS)

    # Get the date.
    date = bogo_data.get_date()
    print(date)

    # Get a modified version of the date.
    custom_date = bogo_data.get_modified_date()
    print(custom_date)

    # Get a list of all the BOGO's for the week.
    bogo_items = bogo_data.get_bogo_items()
    print(bogo_items)

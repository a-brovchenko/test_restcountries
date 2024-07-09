import requests
from typing import Union, Iterator, List
from tabulate import tabulate


class CountryInfo:
    """
    Test class for outputting data about the name of the country, capital and link to the flag
    """

    def __init__(self) -> None:
        self.url = 'https://restcountries.com/v3.1/all'
        self.country_data = self.__fetch_data()


    def __fetch_data(self) -> Union [dict, None]:
        """
        Request for raw data of all countries
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json() 
        else:
            return None 


    def __iter__(self) -> Iterator[List[str]]:
        if self.country_data:
            for country in self.country_data:
                yield   [country['name']['common'], country.get('capital', ['No capital'])[0], country["flags"]['png']]

                   
    def __str__(self) -> str:
        if not self.country_data:
            return "No data available"
        
        table_data = [country for country in self]
        headers = ["Name", "Capital", "Flag"]
        return tabulate(table_data, headers=headers, tablefmt="fancy_grid", maxcolwidths=[None, None, 40])


if __name__ == "__main__":
    country_info = CountryInfo()
    print(country_info)
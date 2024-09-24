import requests

from includes.get_config import get_config

auth_config = get_config()


def _get_womens_colleges():
    """
    Basic function that returns the full JSON string for women's colleges

    See also:
     - https://collegescorecard.ed.gov/data/api-documentation/
    """

    return requests.get(
        url=f"https://api.data.gov/ed/collegescorecard/v1/schools?api_key={auth_config['API_KEY']}&school.women_only=1&fields=id,school.name,school.city,school.state,location&per_page=100",
    ).json()

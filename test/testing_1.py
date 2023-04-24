import pytest
from src.WikipediaPopularity_1 import fetch_data
import re

@pytest.mark.parametrize("min_visitors", [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9])
def test_popularity(min_visitors):
    data = fetch_data()
    errors = []

    for item in data:
        visitors_string = item.popularity.split()[0]
        # Удалить запятые, точки и любое содержимое внутри квадратных скобок
        visitors_string = re.sub(r'\[.*?\]', '', visitors_string).replace(',', '').replace('.', '')
        visitors = float(visitors_string)

        if visitors < min_visitors:
            errors.append(f"{item.website} (Frontend:{item.frontend}|Backend:{item.backend}) has {item.popularity} unique visitors per month. (Expected more than {min_visitors})")

    if errors:
        pytest.fail('\n'.join(errors))

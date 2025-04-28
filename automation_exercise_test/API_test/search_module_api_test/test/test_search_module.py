import allure
import pytest

from automation_exercise_test.API_test.search_module_api_test.utils.api_client import search_users
from test_data import test_data_positive, test_data_negative

@pytest.mark.parametrize("params", test_data_positive)

def test_search_positive(params):
    response = search_users(criteria=params[0], limit=params[1])
    assert response.status_code == 200
    allure.dynamic.title("POSITIVE тест")


@pytest.mark.parametrize("params", test_data_negative)
    
def test_search_negative(params):
    response = search_users(criteria=params[0], limit=params[1])
    assert response.status_code == 400
    allure.dynamic.title("NEGATIVE тест")



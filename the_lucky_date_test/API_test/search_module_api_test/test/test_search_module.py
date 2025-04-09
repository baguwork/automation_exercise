import allure
import pytest

from the_lucky_date_test.API_test.search_module_api_test.utils.api_client import search_users
from test_data import test_data_positive, test_data_negative

@pytest.mark.parametrize("params", test_data_positive)

def test_search_positive(params, setup_logger):
    response = search_users(criteria=params[0], limit=params[1])
    logger = setup_logger
    response = search_users(criteria=params[0], limit=params[1])
    logger.info(f"[POSITIVE] status={response.status_code}, data={params}")
    assert response.status_code == 200
    allure.dynamic.title("POSITIVE тест")


@pytest.mark.parametrize("params", test_data_negative)
    
def test_search_negative(params, setup_logger):
    response = search_users(criteria=params[0], limit=params[1])
    logger = setup_logger
    response = search_users(criteria=params[0], limit=params[1])
    logger.info(f"[NEGATIVE] status={response.status_code}, data={params}")
    assert response.status_code == 400
    allure.dynamic.title("NEGATIVE тест")



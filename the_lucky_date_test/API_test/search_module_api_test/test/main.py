import pytest

if __name__ == "__main__":
    # сюда можно вставить любой путь или аргументы для запуска
    pytest.main(["test_search_module.py",
                 "--alluredir=allure-results",  # папка для сырых результатов
                 ])



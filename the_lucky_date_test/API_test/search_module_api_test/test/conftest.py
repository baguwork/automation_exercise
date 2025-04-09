import pytest
import logging

# === Глобальный логгер проекта ===
@pytest.fixture(scope="session", autouse=False)
def setup_logger():
    logger = logging.getLogger("search_tests")
    logger.setLevel(logging.DEBUG)

    # Консоль
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # Файл
    file_handler = logging.FileHandler("test_log.log", mode='w', encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    # Формат
    formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger

# === Пример фикстуры с токеном (если нужен) ===
@pytest.fixture(scope="session")
def token():
    # можно получить динамически, если знаешь запрос
    return "fake-jwt-or-bearer-token"

# === Хук на падение: логирует FAIL в консоль или файл ===
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        outcome = call.excinfo
        if outcome is not None:
            logger = logging.getLogger("search_tests")
            logger.error(f"[FAIL] {item.name} — {outcome.value}")

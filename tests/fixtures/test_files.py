import pytest

pytest_plugins = [
    "tests.fixtures.test_files",
]


@pytest.fixture
def file1_json():
    return "tests/fixtures/file1.json"


@pytest.fixture
def file2_json():
    return "tests/fixtures/file2.json"


@pytest.fixture
def file1_yaml():
    return "tests/fixtures/file1.yaml"


@pytest.fixture
def file2_yml():
    return "tests/fixtures/file2.yml"


@pytest.fixture
def big_file1_json():
    return "tests/fixtures/big_file1.json"


@pytest.fixture
def big_file2_json():
    return "tests/fixtures/big_file2.json"


@pytest.fixture
def big_file1_yaml():
    return "tests/fixtures/big_file1.yaml"


@pytest.fixture
def big_file2_yml():
    return "tests/fixtures/big_file2.yml"

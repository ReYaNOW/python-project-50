import yaml
import json


def parser(file, extension):
    with open(file) as file:
        match extension:
            case "json":
                return json.load(file)
            case "yaml" | "yml":
                return yaml.safe_load(file)


def parse_files(file_path1: str, file_path2: str) -> tuple:
    """
    Parse two files and return their contents.

    args:
    - file_path1 (str): the path to the first file to be parsed.
    - file_path2 (str): the path to the second file to be parsed.

    return:
    - tuple: a tuple containing the contents of the two files.
    """
    f1 = parser(file_path1, file_path1.split(".")[-1])
    f2 = parser(file_path2, file_path2.split(".")[-1])
    return f1, f2

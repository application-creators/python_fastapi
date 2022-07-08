from keyword import iskeyword
from sys import exit

PROJECT_PACKAGE_NAME = "{{ cookiecutter.project_package_name }}"
API_PORT = "{{ cookiecutter.api_port }}"


def validate_project_package_name(package_name: str) -> None:
    if not package_name.isidentifier() or iskeyword(package_name):
        print(
            "The project package name (project_package_name) must "
            "be a valid python package name"
        )
        exit(1)


def validate_api_port(port_number: str) -> None:
    if not port_number.isdigit():
        print("The API port number (api_port) must be a positive integer")
        exit(2)

    if not (0 < int(port_number) <= 65535):
        print(
            "The API port number (api_port) must be higher than 0"
            " and minor or equal to 65535"
        )
        exit(3)


VALIDATIONS = {
    PROJECT_PACKAGE_NAME: validate_project_package_name,
    API_PORT: validate_api_port,
}


for setting_value, validation_function in VALIDATIONS.items():
    validation_function(setting_value)

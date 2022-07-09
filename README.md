# FastAPI Project Template

This is a template used by [create_app](https://github.com/application-creators/create_app) to create a 
new FastAPI project.

To create your new project from this template, simply run:

```shell
pip install create_app
python -m create_app python_fastapi
```


## What's in this template

 * Project structure
 * A [FastAPI](https://fastapi.tiangolo.com/) API:
   * Configurable through environment variables and environment file
   * With CORS
   * And Base models for endpoints with pagination
 * Virtualenv
 * Unit tests
 * Docker containerization
 * Pre-commit GIT hooks
   * [Black](https://github.com/psf/black)
   * [Isort](https://pycqa.github.io/isort/)
   * [Flake8](https://flake8.pycqa.org/en/latest/)
 * Makefile with useful commands


## Git hooks

This template uses [pre-commit](https://pre-commit.com/) to run GIT hooks in your repo:
 * [Black](https://github.com/psf/black)
 * [Isort](https://pycqa.github.io/isort/)
 * [Flake8](https://flake8.pycqa.org/en/latest/)

This helps developers to keep the same code styling in the project.

To install the hooks in your repo, first [install pre-commit](https://pre-commit.com/#install) in your system. Then run:
```shell
make install_git_hooks
```


## Docker

You can build and run this project with Docker.

To build the Docker image, run:
```shell
make docker_build
```

To start the Docker image, run:
```shell
make docker_run
```

To build and start the Docker image with a single command, run:
```shell
make docker_build_and_run
```

### Take a look at your running API

After starting the container, you can hit the API root with any browser or HTTP client. For example, with CURL:
```shell
curl localhost:{api_port}
```

Check the API docs! http://localhost:{api_port}/docs

And the alternative API docs! http://localhost:{api_port}/redoc


## Virtualenv

It is recommended to keep your system's Python interpreter clean, and install your project's dependencies in a virtual 
environment (_venv_). Doing this has advantages like preventing dependencies conflicts between different projects
you may have in your system.

### Create the virtualenv

After you've installed [venv](https://docs.python.org/3/library/venv.html) in your system, do the following to create 
the venv:

```shell
make create_virtualenv
```


### Requirements

Use the [requirements.frozen](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/requirements.frozen) file to declare 
the project's dependencies, and [requirements.test.frozen](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/requirements.test.frozen) 
to declare dependencies that are only required to run tests. As indicated in the filenames, it is advised to declare 
the dependencies with explicit versions (example: _requests==2.28.1_). This will allow you to control when to upgrade
dependencies versions, and will save you headaches when a new dependency version is released right when you were 
running a deployment pipeline.

To install the requirements in the venv, run:
```shell
make install_requirements
```

To install the test requirements in the venv, run:
```shell
make install_test_requirements
```

To install requirements and test requirements with a single, command, run:
```shell
make install_all_requirements
```


## Unit tests

Add your unit tests to the 
[tests package](/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/%7B%7B%20cookiecutter.project_package_name%20%7D%7D/tests).

To run all unit tests:
```shell
make run_unit_tests
```

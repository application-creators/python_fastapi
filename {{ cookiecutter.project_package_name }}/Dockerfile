FROM python:3.10


ARG PROJECT_PACKAGE_NAME={{ cookiecutter.project_package_name }}

ARG WORK_DIR=/code
ARG REQUIREMENTS_FILENAME=requirements.frozen

ENV API_HOST=0.0.0.0
ENV API_PORT={{ cookiecutter.api_port }}


EXPOSE ${API_PORT}


WORKDIR ${WORK_DIR}


COPY ${REQUIREMENTS_FILENAME} .
RUN pip install -r ${REQUIREMENTS_FILENAME}


COPY ${PROJECT_PACKAGE_NAME} .


CMD uvicorn main:app --host ${API_HOST} --port ${API_PORT} --reload

FROM python:3.10


ARG SERVICE_NAME=api

ARG WORK_DIR=/code
ARG REQUIREMENTS_FILENAME=requirements.frozen

ENV API_HOST=0.0.0.0
ENV API_PORT=5000


EXPOSE ${API_PORT}


WORKDIR ${WORK_DIR}


COPY ${SERVICE_NAME} .


RUN pip install -r ${REQUIREMENTS_FILENAME}


CMD uvicorn main:app --host ${API_HOST} --port ${API_PORT} --reload

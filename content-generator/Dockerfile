ARG FUNCTION_DIR="/function"

FROM python:3.9-slim AS build-image

RUN apt-get update && \
    apt-get install -y \
    g++ \
    make \
    cmake \
    unzip \
    libcurl4-openssl-dev

ARG FUNCTION_DIR
RUN mkdir -p ${FUNCTION_DIR}
COPY ./src ${FUNCTION_DIR}

RUN pip3 install  \
    --target ${FUNCTION_DIR} \
    awslambdaric

FROM python:3.9-slim

ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

ENTRYPOINT [ "/usr/bin/python3", "-m", "awslambdaric" ]
CMD [ "app.lambda_handler" ]
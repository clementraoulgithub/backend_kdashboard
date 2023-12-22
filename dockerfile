FROM python:3.12.1-alpine3.19
WORKDIR /app
COPY . /app/

RUN apk update \
    && apk add build-base \
    && python3 -m pip install --upgrade pip \
    && pip install -r requirements.txt

ENTRYPOINT [ "python", "-m", "uvicorn", "src.__main__:app", "--host", "0.0.0.0", "--port", "8000"]
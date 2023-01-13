FROM python:3.10-slim-bullseye as base
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN mkdir /build
WORKDIR /build

RUN apt-get update -y && apt-get install gcc -y && rm -rf /var/lib/apt/lists/*
RUN python3 -m venv $VIRTUAL_ENV && pip install poetry==1.2.0 --no-cache-dir

COPY pyproject.toml .

RUN poetry install
COPY . /build

RUN $VIRTUAL_ENV/bin/poetry run mkdocs build

FROM python:3.10-alpine
COPY --from=base /build/site /site
WORKDIR /site
CMD ["python3", "-m", "http.server"]


# in production we use nginx; this is just for local testing
FROM nginx:1.21.3-alpine
COPY --from=base /build/site /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

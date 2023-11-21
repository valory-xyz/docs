FROM python:3.10-slim-bullseye as base
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN mkdir /build
WORKDIR /build

RUN apt-get update -y && apt-get install git gcc -y && rm -rf /var/lib/apt/lists/*
RUN python3 -m venv $VIRTUAL_ENV && pip install poetry==1.3.2 --no-cache-dir

COPY pyproject.toml .

RUN poetry install
COPY . /build

RUN find . -name "mkdocs.yml" | xargs -L1 sed -i.snrbck "s/materialx.emoji.twemoji/material.extensions.emoji.twemoji/g"
RUN find . -name "mkdocs.yml" | xargs -L1 sed -i.snrbck "s/materialx.emoji.to_svg/material.extensions.emoji.to_svg/g"
RUN find . -name "*.snrbck" | xargs -L1 rm

RUN $VIRTUAL_ENV/bin/poetry run pip3 install mkdocs-material==9.4.10 mkdocs-material-extensions==1.3
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

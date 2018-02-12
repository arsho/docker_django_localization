FROM python:2.7
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update && apt-get install -y \
		mysql-client libmysqlclient-dev \
		postgresql-client libpq-dev \
		sqlite3 \
        gettext \
		gcc \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

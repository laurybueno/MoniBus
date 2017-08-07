FROM python:3.6

RUN apt-get update \
    && apt-get install -y \
        postgresql-client \
        libpq-dev \
        libgdal-dev \
        gdal-bin \
        python3-gdal \
        # cron \
    && rm -rf /var/lib/apt/lists/*

ENV CPLUS_INCLUDE_PATH /usr/include/gdal
ENV C_INCLUDE_PATH /usr/include/gdal
ENV PYTHONUNBUFFERED=0

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN cat config/cron_observador >> /etc/crontab \
#    && service cron start

VOLUME /usr/src/app/static

EXPOSE 8000

CMD ["./start.sh"]

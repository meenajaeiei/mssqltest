FROM python:3.6.9
ENV dbip=10.33.0.199
ENV dbname=defaultdb123
ENV dbuser=sa
ENV dbpass=1qazXSW@
ENV webpath='test'

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN  apt update  && apt install -y unixodbc-dev &&  ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools && pip3 install django && pip3 install --upgrade pyodbc

COPY . /app

WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000" , "--noreload"]

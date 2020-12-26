FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app
ENV FLASK_ENV=production
ADD requirements.txt /app
RUN pip install -r requirements.txt
ADD . /app
EXPOSE 5000
ENTRYPOINT ["gunicorn", "-w", "1", "-t", "60", "--threads", "1", "--bind", "0.0.0.0:5000", "--log-config", "gunicorn_logging.conf", "mathapi:create_app()"]

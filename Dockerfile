FROM python:3.8-slim

ENV APP_HOME=/app

RUN useradd -ms /bin/sh -u 1001 -U mathapi \
  && mkdir -p $APP_HOME /home/mathapi/.local/bin \
  && chown -R mathapi:mathapi $APP_HOME /home/mathapi
ENV FLASK_ENV=production

COPY --chown=mathapi:mathapi requirements.txt $APP_HOME
RUN pip install --no-cache-dir -r $APP_HOME/requirements.txt
COPY --chown=mathapi:mathapi requirements-dev.txt $APP_HOME
RUN pip install --no-cache-dir -r $APP_HOME/requirements-dev.txt

COPY --chown=mathapi:mathapi . $APP_HOME  

EXPOSE 5000

USER mathapi
WORKDIR $APP_HOME
CMD ["gunicorn", "-w", "1", "-t", "60", "--threads", "1", "--bind", "0.0.0.0:5000", "--log-config", "gunicorn_logging.conf", "mathapi:create_app()"]

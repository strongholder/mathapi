FROM python:3.8-slim-buster

ENV APP_HOME=/app

COPY install-nginx-debian.sh /
COPY nginx.conf /etc/nginx/nginx.conf

RUN bash /install-nginx-debian.sh

RUN useradd -ms /bin/sh -u 1001 -U mathapi \
  && mkdir -p $APP_HOME $APP_HOME/log/nginx $APP_HOME/run /var/cache/nginx /home/mathapi/.local/bin \
  && chown -R mathapi:mathapi $APP_HOME /home/mathapi /var/cache/nginx

RUN rm /etc/nginx/conf.d/default.conf

ENV FLASK_ENV=production

COPY --chown=mathapi:mathapi requirements.txt $APP_HOME
RUN pip install --no-cache-dir -r $APP_HOME/requirements.txt
COPY --chown=mathapi:mathapi requirements-dev.txt $APP_HOME
RUN pip install --no-cache-dir -r $APP_HOME/requirements-dev.txt

COPY --chown=mathapi:mathapi . $APP_HOME  

EXPOSE 5000
STOPSIGNAL SIGQUIT

USER mathapi
WORKDIR $APP_HOME
CMD /app/entrypoint.sh

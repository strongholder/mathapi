from mathapi import config


def init_celery(app, celery):
    celery.config_from_object(config.load_object(app))

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    return celery

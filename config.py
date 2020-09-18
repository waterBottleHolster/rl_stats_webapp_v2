#!/home/dh_4gxtme/rl-experiment-tracker.com/public/rl_stats_webapp_v2/.flask_venv/bin/python3
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'docker': DockerConfig,
    'unix': UnixConfig,

    'default': DevelopmentConfig
}
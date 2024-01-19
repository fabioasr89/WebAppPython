from flask import Flask
import logging
import logging.config
from controller.login import login_blueprint
from controller.health import healt_flask
#Il primo argomento è il Nome del modulo o del pacchetto dell'applicazione. è un Comoda scorciatoia per questo che è appropriata per la maggior parte dei casi. 
#Questo è necessario in modo che Flask sappia dove cercare risorse come come modelli e file statici.__name__
flask=Flask(__name__,static_url_path='/static/')
flask.register_blueprint(login_blueprint)
flask.register_blueprint(healt_flask)
flask.secret_key='abcgagagag'
logging.config.fileConfig('configuration/log.conf',disable_existing_loggers=True, encoding=None)
logger = logging.getLogger('weblog')

flask.run()
logger.info("Applicazione correttamente startata")





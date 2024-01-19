from flask import Blueprint,render_template,request,session
from configuration.dbConf import DatabaseManager
import logging
login_blueprint=Blueprint("login_blueprint",__name__)


logging.config.fileConfig('configuration/log.conf',disable_existing_loggers=True, encoding=None)
logger = logging.getLogger('weblog')

@login_blueprint.route('/login',methods=['GET','POST'])
def login():
    error=""
    i=0
    try:
        username=session['username']
    except:
        i=1
        logger.warn('utente non in sessione')
        
    if request.method=='GET':
        if i==0:
            return render_template('index.htm',username=username)
        else:
            return render_template('login.htm')
    elif request.method=='POST':
        logger.debug('Verifica session in corso..')
        if i==0:
            logger.debug('Utente '+username+" "+"già in sessione")
            return render_template('index.htm',username=username)
        else:
            logger.debug('Verifica request in corso...')
            check=request.form and request.form.get('username') and request.form.get('password')
            if check:
                logger.debug('Request correttamente verificata')
                try:
                    logger.debug('connessione database in corso..')
                    db=DatabaseManager('127.0.0.1','root','','test')
                    logger.debug('connessione correttamente eseguita')
                    username=request.form.get('username')
                    password=request.form.get('password')
                    logger.debug('Ricerca utente in corso..')
                    users=db.finfById(username,password)
                    logger.debug(users)
                    logger.debug('utente correttamente recuperato')
                    if users:
                        session['username']=username
                        return render_template('index.htm',session['username'])
                    else:
                        logger.error("Utente non autorizzato")
                        return render_template('login.htm',error="Utente non autorizzato")
                except :
                    logger.error('Si è verificato un errore nella fase di connessione al db')
                    return render_template('login.htm',error="Si è verificato un errore nella fase di connessione al db")
                
        
@login_blueprint.route('/logout',methods=['POST'])
def logout():
    logger.debug('Disconnessione in corso..')
    i=0
    try:
        username=session['username']
    except:
        i=1
    if i==0:
        logger.debug('Disconnessione utente '+username+" "+"in corso..")
        session.clear()
        logger.debug("Disconnessione correttamente eseguita")
        return render_template('login.htm')
    else:
        logger.debug('Utente non in sessione, impossibile fare il logout')

@login_blueprint.route('/',methods=['GET','POST'])
def default():
    return render_template('login.htm')
    

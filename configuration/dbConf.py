import mysql.connector
import logging
class DatabaseManager:
    connection=""
    query=""

    def __init__(self,host,username,password,databasename):
        ##self.logging=logging.config.fileConfig('configuration/log.conf',disable_existing_loggers=True, encoding=None)
        logging.config.fileConfig('configuration/log.conf',disable_existing_loggers=True, encoding=None)
        logger = logging.getLogger('weblog')
        logger.debug('Connessione...')
        try:
            self.connection=mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=databasename,
            raise_on_warnings=True
            )
            self.query=self.connection.cursor()
        except mysql.connector.Error as error:
            logger.error('errore nella fase di connessione')
            logger.error(error)
        
       


    #esegue una query con una transazione sul db
    def executeUpdateQuery(self,queryString):
       
        self.query.execute(queryString)
        self.connection.commit
   

    def finfById(self,id,password):
        logging.config.fileConfig('configuration/log.conf',disable_existing_loggers=True, encoding=None)
        logging.getLogger('mysql.connector').setLevel(logging.DEBUG)
        logger = logging.getLogger('weblog')

        try:
            logger.debug("Esecuzione query in corso..")
            logger.debug(id)
            logger.debug(password)
            queryString="Select* from users where username=%s and password=%s"
            tuple=(id,password)
            self.query.execute(queryString,tuple)
            return self.query.fetchall()
        except mysql.connector.Error as error:
            print(error)
            logger.error(error)
    
    
    def disconnettiConnessione(self):
        if self.connection:
            self.connection.close()
        
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', level=logging.DEBUG)

logger.debug('   Loging %s lewel', 'DEBUG')
logger.info('    Loging %s lewel', 'INFO')
logger.warning(' Loging %s lewel', 'WARN')
logger.error('   Loging %s lewel', 'ERROR')
logger.critical('Loging %s lewel', 'CRITICAL')

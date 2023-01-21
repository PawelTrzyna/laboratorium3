import logging
 
 
def show_logs(level, format):
    logging.basicConfig(level=level, format=format)
    logging.debug('DEBUG')
    logging.info('INFO')
    logging.warning('WARNING')
    logging.error('ERROR')
    logging.critical('CRITICAL')
 
 
show_logs(logging.DEBUG, '%(levelname)s: %(message)s')
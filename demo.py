from US_VISA.logger import logging
from US_VISA.exception import USvisaException
import sys



try:
    a = 2/0

except Exception as e:
    logging.info(e)
    raise USvisaException(e, sys)
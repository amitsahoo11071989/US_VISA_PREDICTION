import logging
import os

from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = "logs"
current_directory = os.getcwd()

logs_path = os.path.join(current_directory, log_dir, LOG_FILE)

if not os.path.exists(os.path.join(current_directory, log_dir)):
    os.makedirs(log_dir)


logging.basicConfig(filename=logs_path,
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    level=logging.DEBUG)




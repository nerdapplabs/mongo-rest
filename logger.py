import json
import logging.config
from logging.handlers import SysLogHandler


class MyLogger:

    @staticmethod
    def setup(logger_name: str=None):

        # loading_data_from_json_file
        with open("app.json", "r", encoding="utf-8") as fd:
            data = json.load(fd)

            # LOG_SYSLOG
            syslog_loaded = data["handlers"]["SysLog"]
            syslog_address = syslog_loaded["address"]
            syslog_level = syslog_loaded["level"]
            formatter = logging.Formatter(fmt=data["formatters"]["simple"]["format"],
                                          datefmt=data["formatters"]["simple"]["date_fmt"])
            propagate = data["loggers"]["propagate"]

            # accessing_the_loaded_json_file_SYSLOG
            logger = logging.getLogger(logger_name)
            handler = SysLogHandler(address=syslog_address)
            handler.setFormatter(formatter)
            logger.setLevel(syslog_level)
            logger.propagate = propagate
            logger.addHandler(handler)




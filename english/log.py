# -*- coding:utf-8 -*-
import logging
import colorlog

class logger():
    def __init__(self,
                 name,
                 log_name='/tmp/info.log',
                 log_level=logging.DEBUG,
                 is_file_output=True,
                 is_stream_output=True):
        format_dict = {
                'format': '%(asctime)s %(process)d %(log_color)s[%(levelname)s]%(reset)s %(pathname)s:%(lineno)d <%(funcName)s> %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
                }
        log_colors_config = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red',
        }
        # self.fmt = logging.Formatter(format_dict['format'], format_dict['datefmt'])
        self.fmt = colorlog.ColoredFormatter(format_dict['format'], format_dict['datefmt'], log_colors=log_colors_config)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        if is_file_output:
            self.create_file_handler(log_name)

        if is_stream_output:
            self.create_stream_handler()

    def create_file_handler(self, log_name, log_level=logging.DEBUG):
        '''Create a handler for record log to file'''
        f_handler = logging.FileHandler(log_name)
        f_handler.setLevel(log_level)
        f_handler.setFormatter(self.fmt)
        self.logger.addHandler(f_handler)

    def create_stream_handler(self, log_level=logging.DEBUG):
        '''Create a handler for record log to stream'''
        s_handler = logging.StreamHandler()
        s_handler.setLevel(log_level)
        s_handler.setFormatter(self.fmt)
        self.logger.addHandler(s_handler)

    def get_logger(self):
        return self.logger


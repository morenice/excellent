# -*- coding: utf-8 -*-
import yaml
from exceltp.config_define import *


class Config:

    def __init__(self, filename):
        self.filename = filename
        self.analyzer_conf = None
        self.action_conf = None

    def _validate(self, config):
        if CONFIG_VERSION not in config:
            return False
        return True

    def _read(self, config):
        if ANALYZER in config:
            self.analyzer_conf = config[ANALYZER]
        if ACTION in config:
            self.action_conf = config[ACTION]

    def read(self):
        try:
            with open(self.filename, encoding="utf-8") as f:
                config = yaml.load(f.read())

            if self._validate(config) == False:
                return -1

            self._read(config)
        except FileNotFoundError as ex:
            return -2
        except Exception as ex:
            print(ex)
            return -3

        return 0

    def read_raw_data(self, raw_data):
        try:
            config = yaml.load(raw_data)

            if self._validate(config) == False:
                return -1

            self._read(config)

        except Exception as ex:
            print(ex)
            return -3

        return 0

    def get_analyzer_conf(self):
        return self.analyzer_conf

    def get_action_conf(self):
        return self.action_conf

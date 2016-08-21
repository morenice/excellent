# -*- coding: utf-8 -*-
import yaml


class Config:
    filename = ""
    analyzer_conf = None
    action_conf = None

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, encoding="utf-8") as f:
                config = yaml.load(f.read())

            if 'config_version' not in config:
                return -1

            if 'analyzer' in config:
                self.analyzer_conf = config['analyzer']
            if 'action' in config:
                self.action_conf = config['action']

        except FileNotFoundError as ex:
            return -2
        except Exception as ex:
            return -3

        return 0

    def get_analyzer_conf(self):
        return self.analyzer_conf

    def get_action_conf(self):
        return self.action_conf

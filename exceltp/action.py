# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Action:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.action_type = None

    @abstractmethod
    def do(self, data):
        pass

    def get_type(self):
        return self.action_type

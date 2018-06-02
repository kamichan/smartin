# -*- coding: utf-8 -*-

import readline

class Command:

    # Initialize
    def __init__(self):
        self.options  = {}
        self.matches  = []

    # Add an option to the command
    def add_option(self, option, entity=None):
        if entity is None:
            entity = option
        self.options[option] = entity

    # Get options
    def get_options(self, prefix=''):
        keys = []
        if prefix == '':
            keys = self.options.keys()
        else:
            for key in self.options.keys():
                if not key.startswith(prefix, 0, len(prefix)):
                    continue
                keys.append(key)

        return keys

    # Get args
    def get_option_args(self, option, prefix=''):
        keys = []
        args = []

        if isinstance(self.options[option], list):
            args = self.options[option]
        elif callable(self.options[option]):
            handler = self.options[option]
            args    = handler(option)
        else:
            args = []

        if prefix == '':
            keys = args
        else:
            for key in args:
                if not key.startswith(prefix, 0, len(prefix)):
                    continue
                keys.append(key)

        return keys

    def completer_handler(self, text, state):
        if state == 0:
            line = readline.get_line_buffer()
            line = line[0:len(line)-len(text)].strip()
            index= line.rfind(' ')
            if index == -1:
                self.matches = self.get_options(text)
            else:
                last = line[index+1:]
                if self.options.has_key(last):
                    self.matches = self.get_option_args(last, text)
                else:
                    self.matches = self.get_options(text)

        try:
            if len(self.matches) == 1 and self.matches[0] == text:
                readline.insert_text(' ')
                return None
            else:
                return self.matches[state]
        except IndexError:
            pass

        return None

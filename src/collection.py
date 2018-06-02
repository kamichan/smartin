# -*- coding: utf-8 -*-

import readline
from command import Command

class Collection:

    # Initialize
    def __init__(self):
        self.commands = {}
        self.matches  = []

    # Add a command to the collection
    def add_command(self, cmd, entity=None):
        if entity is None:
            entity = cmd
        self.commands[cmd] = entity

    # Get commands
    def get_commands(self, prefix=''):
        keys = []
        if prefix == '':
            keys = self.commands.keys()
        else:
            for key in self.commands.keys():
                if not key.startswith(prefix, 0, len(prefix)):
                    continue
                keys.append(key)

        return keys

    def completer_handler(self, text, state):
        line = readline.get_line_buffer()
        if ' ' in line:
            cmd = line.split(' ')[0]
            if self.commands.has_key(cmd) and isinstance(self.commands[cmd], Command):
                return self.commands[cmd].completer_handler(text, state)            
            else:
                self.matches = []
        elif state == 0:
            self.matches = self.get_commands(text)

        try:
            if len(self.matches) == 1 and self.matches[0] == text:
                readline.insert_text(' ')
                return None
            else:
                return self.matches[state]
        except IndexError:
            pass

        return None
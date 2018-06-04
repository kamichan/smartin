# -*- coding: utf-8 -*-

import os, sys
import atexit
import readline
from   collection import Collection
from   command    import Command

# Initialize
def init(history=None, maxlength=1000):
    # Initialize readline
    readline.parse_and_bind('tab: complete')
    # Completer
    readline.set_completer_delims(' \t\n=')
    # History file
    if history is not None:
        _init_history(history, maxlength)

# Input
def input(prompt, collection=None):
    if isinstance(collection, Collection):
        readline.set_completer(collection.completer_handler)
    else:
        readline.set_completer(_completer_handler)

    try:
        # Listen the input
        return raw_input(prompt)
    except KeyboardInterrupt, e: # ctrl + c
        raise e

    return ''

# Initialize history
def _init_history(history, maxlength):
    if history[0] == '~':
        history = os.environ['HOME'] + history[1:]
    # New file
    if not os.path.isfile(history):
        try:
            fp = open(history, 'w')
            fp.close()
        except IOError:
            return False

    readline.read_history_file(history)
    readline.set_history_length(maxlength)
    # Register a callback for shutdown
    atexit.register(readline.write_history_file, history)

    return True

# Default completer
def _completer_handler(text, state):
    return None
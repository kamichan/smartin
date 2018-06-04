# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.path.realpath('..'))
######################################################################

import smartin

smartin.init()
# smartin.init('~/.history')

def user_args(option):
    return ['root', 'admin']

command = smartin.Command()
command.add_option('--user=',   user_args)
command.add_option('--pass=')
command.add_option('--port=',   ['8000', '9000'])

collection = smartin.Collection()
collection.add_command('test',  command)
collection.add_command('help')

# test del_command
collection.add_command('test_del')
collection.del_command('test_del')

try:
    print(smartin.input('smartin> ', collection))
except KeyboardInterrupt:
    print('\nbye!')
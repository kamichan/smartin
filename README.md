# Smart input
> *自动命令输入提示*

## Manual

```python
# -*- coding: utf-8 -*-

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

try:
    print(smartin.input('smartin> ', collection))
except KeyboardInterrupt:
    print('\nbye!')
```
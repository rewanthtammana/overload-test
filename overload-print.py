from __future__ import print_function
import re

try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

def print(*args, **kwargs):
    def __repr__(*argss, **kwargss):
        return __builtin__.repr(*argss, **kwargss)

    if type(args[0]) == dict:
        if args[0].get('Password') != None and args[0]['Password'] != "":
            __builtin__.print("{'PassProps.Username': '" + args[0]['PassProps.Username'] + "', 'Password': '*****'}")
            return
    
    if type(args[0]) == str:
        result = re.findall("{'PassProps.Username': ?'([^']*)', ?'Password': ?'([^']*)'}", args[0])
        if len(result) != 0:
            __builtin__.print("{'PassProps.Username': '" + result[0][0] + "', 'Password': '*****'}")
            return

    return __builtin__.print(*args, **kwargs)

# Test cases
obj = {
    'Username': 'hello',
    'Password': 'sup3rs3cr3t'
}
print(obj)

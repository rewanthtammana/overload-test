from __future__ import print_function

try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

def print(*args, **kwargs):
    if type(args) == tuple and args[0].get('Password') != None and args[0]['Password'] != "":
        __builtin__.print("{'PassProps.Username': 'mongoAppUsr', 'Password': '*****'}")
        return
    return __builtin__.print(*args, **kwargs)

obj = {
    'Username': 'hello',
    'Password': 'sup3rs3cr3t'
}
print(obj)

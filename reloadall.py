import types
from imp import reload

def status(module):
    print(module.__name__, 'reloading')

def transitive_reload(module, visited):
    if not module in visited:
        status(module)
        reload(module)
        visited[module] = None
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visites = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visites)

if __name__ == "__main__":
    import reloadall
    reload_all(reloadall)

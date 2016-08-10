import importlib


class Container:
    """
    In this post I am going to look at the basics of Dependency Injection again and how they tie in with the move to
    using a Dependency Injection Container. The basics of why injecting an object's dependencies is a good idea are
    fairly easy to grasp, how this then leads to the use of a container is not so easily apparent.

    """
    container = {
        'ftplib.ftp': None,
        'pysftp': None,
        'fnmatch': None,
        'os': None,
        'yaml': None,
        'sys': None,
        'config_app': None,
        'logger': None,
        'strategy.secure': None,
        'strategy.unsecure': None,
        'open': None,
        'get_opt': None
    }

    mapper = {
        'ftplib.ftp': 'ftplib',
        'pysftp': 'pysftp',
        'fnmatch': 'fnmatch',
        'os': 'os',
        'yaml': 'yaml',
        'sys': 'sys',
        'config_app': 'config.config_app',
        'logger': 'logging',
        'strategy.secure': 'strategy.secure',
        'strategy.unsecure': 'strategy.unsecure',
        'open': 'shared.open_file',
        'get_opt': 'getopt'
    }

    @staticmethod
    def dependency(key: str) -> str:
        return Container.__import_module(key)

    @staticmethod
    def update(container):
        Container.container.update(container)

    @staticmethod
    def get_container():
        return Container.container

    @staticmethod
    def __import_module(name):
        if Container.container.get(name) is not None:
            return Container.container.get(name)
        else:
            if name in Container.mapper:
                Container.container.__setitem__(name, importlib.import_module(Container.mapper.get(name)))
                return Container.container.get(name)
            else:
                raise Exception('module name ' + name + ' no exist in the mapper')

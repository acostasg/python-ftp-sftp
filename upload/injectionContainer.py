import importlib

from shared.Singleton import SingleMetaClass


class Container(metaclass=SingleMetaClass):
    """
    In this post I am going to look at the basics of Dependency Injection again and how they tie in with the move to
    using a Dependency Injection Container. The basics of why injecting an object's dependencies is a good idea are
    fairly easy to grasp, how this then leads to the use of a container is not so easily apparent.

    """
    __container = {
        'ftplib.ftp': None,
        'pysftp': None,
        'fnmatch': None,
        'os': None,
        'yaml': None,
        'sys': None,
        'config_app': None,
        'logger': None,
        'strategy.secure': None,
        'strategy.unsecure': None
    }

    __mapper = {
        'ftplib.ftp': 'ftplib',
        'pysftp': 'pysftp',
        'fnmatch': 'fnmatch',
        'os': 'os',
        'yaml': 'yaml',
        'sys': 'sys',
        'config_app': 'config.ConfigApp',
        'logger': 'logging',
        'strategy.secure': 'strategy.secure',
        'strategy.unsecure': 'strategy.unsecure'
    }

    @staticmethod
    def dependency(key):
        return Container.__import_module(Container, key)

    @staticmethod
    def update(container):
        return Container.__container.update(container)

    @staticmethod
    def get_container():
        return Container.__container

    @staticmethod
    def __import_module(self, name):
        if self.__container.get(name) is not None:
            return self.__container.get(name)
        else:
            if name in self.__mapper:
                return importlib.import_module(self.__mapper.get(name))
            else:
                raise Exception('module name ' + name + ' no exist in the mapper')

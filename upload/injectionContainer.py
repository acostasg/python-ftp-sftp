import importlib

from shared.Singleton import SingleMetaClass


class Container(metaclass=SingleMetaClass):
    __container = {
        'ftplib.ftp': None,
        'pysftp': None,
        'fnmatch': None,
        'os': None,
        'yaml': None,
        'sys': None,
        'config_app': None,
        'logger': None
    }

    __mapper = {
        'ftplib.ftp': 'ftplib',
        'pysftp': 'pysftp',
        'fnmatch': 'fnmatch',
        'os': 'os',
        'yaml': 'yaml',
        'sys': 'sys',
        'config_app': 'config.ConfigApp',
        'logger': 'logging'
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
                raise Exception('module name '+name+' no exist in the mapper')
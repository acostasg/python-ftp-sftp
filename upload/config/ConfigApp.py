from shared import SingletonMetaClass as Singleton


class Handle:
    __metaclass__ = Singleton.SingletonMetaClass

    def __init__(self, os, yaml):
        """

        :param os:
        :param yaml:
        :return:
        """
        import strategy.requestParams

        script_dir = os.path.dirname(__file__)
        with open(script_dir + '/../../config/connections.yml', 'r') as connectionsConfig:
            connections = yaml.load(connectionsConfig)
            self.connectionInfoSecure = {'host': connections['secure']['host'],
                                         'username': connections['secure']['username'],
                                         'password': connections['secure']['secret'],
                                         'port': int(connections['secure']['port'])
                                         }
            self.connectionInfoUnsercure = {'host': connections['unsercure']['host'],
                                            'username': connections['unsercure']['username'],
                                            'password': connections['unsercure']['secret'],
                                            'port': int(connections['unsercure']['port'])
                                            }

        with open(script_dir + '/../../config/app.yml', 'r') as app_config:
            app_config = yaml.load(app_config)
            self.request = strategy.requestParams.RequestParams()
            self.request.connectionInfo = self.connectionInfoSecure
            self.request.localPath = app_config['local']['path']
            self.request.remotePath = app_config['remote']['path']
            self.request.prefix = app_config['local']['prefix']
            self.request.pattern = app_config['local']['pattern']

            self.defaultStrategy = int(app_config['strategy']['default'])

    pass

    def get_request(self, type):
        """
        :param type: int
        :return: RequestParams
        """
        self.request.connectionInfo = self.get_connections(type)
        return self.request

    def get_connections(self, type):
        """

        :param type: int
        :return: dict
        """
        import strategy.strategyFactory
        if type == strategy.strategyFactory.Strategy.CONST_SECURE:
            return self.connectionInfoSecure
        elif type == strategy.strategyFactory.Strategy.CONST_UNSECURE:
            return self.connectionInfoUnsercure
        else:
            raise Exception('Unknown strategy')

    def get_strategy(self):
        """

        :return: int
        """
        return int(self.defaultStrategy)

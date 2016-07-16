class Handle:
    def __init__(self, os, yaml):
        """

        :param os:
        :param yaml:
        :return:
        """
        import strategy.RequestParams

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

        with open(script_dir + '/../../config/app.yml', 'r') as appConfig:
            appConfig = yaml.load(appConfig)
            self.request = strategy.RequestParams
            self.request.connectionInfo = self.connectionInfoSecure
            self.request.localPath = appConfig['local']['path']
            self.request.remotePath = appConfig['remote']['path']
            self.request.prefix = appConfig['local']['prefix']
            self.request.pattern = appConfig['local']['pattern']

            self.defaultStrategy = int(appConfig['strategy']['default'])

    pass

    def get_request(self, type):
        """
        :param type: int
        :return: RequestParams
        """
        self.request.RequestParams.connectionInfo = self.get_connections(type)
        return self.request.RequestParams

    def get_connections(self, type):
        """

        :param type: int
        :return: dict
        """
        import strategy.StrategyFactory
        if type == strategy.StrategyFactory.Strategy.CONST_SECURE:
            return self.connectionInfoSecure
        elif type == strategy.StrategyFactory.Strategy.CONST_UNSECURE:
            return self.connectionInfoUnsercure
        else:
            return self.get_connections(self.get_strategy())

    def get_strategy(self):
        """

        :return: int
        """
        return int(self.defaultStrategy)

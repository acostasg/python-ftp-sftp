from injectionContainer import Container


class Unsecure:
    def __init__(self, logging):
        self.logging = logging
        pass

    def upload(self, request):
        """

        :param request:
        :return: boolean
        """
        ftp = Container.dependency('ftplib.ftp')
        fnmatch_module = Container.dependency('fnmatch')
        os_module = Container.dependency('os')

        self.logging.warning('Starting strategy unsecured...')

        ftp.connect(request.connectionInfo['host'], request.connectionInfo['port'])
        ftp.login(request.connectionInfo['username'], request.connectionInfo['password'])
        ftp.cwd(request.remote_path)

        for file in os_module.listdir(request.local_path):
            if fnmatch_module.fnmatch(file, request.provider + request.pattern):
                self.logging.info('Uploading file %s...' % file)
                ftp.storlines('STOR %s' % file, open('%s%s' % (request.local_path, file), 'r'))

        self.logging.info('Files has been successfully uploaded to %s' % (request.connectionInfo['host']))

        ftp.quit()
        return True

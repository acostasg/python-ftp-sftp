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
        open_module = Container.dependency('open')

        self.logging.warning('Starting strategy unsecured...')

        ftp.connect(request.connectionInfo['host'], request.connectionInfo['port'])
        ftp.login(request.connectionInfo['username'], request.connectionInfo['password'])
        ftp.cwd(request.remotePath)

        for file in os_module.listdir(request.localPath):
            if fnmatch_module.fnmatch(file, request.prefix + request.pattern):
                self.logging.info('Uploading file {0!s}...'.format(file))
                ftp.storlines('STOR {0!s}'.format(file), open_module('{0!s}{1!s}'.format(request.localPath, file), 'r'))

        self.logging.info('Files has been successfully uploaded to {0!s}'.format((request.connectionInfo['host'])))

        ftp.quit()
        return True

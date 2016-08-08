from injectionContainer import Container


class Secure:
    """
    Secure strategy for upload files, ftp
    """
    def __init__(self, logging):
        self.logging = logging
        pass

    def upload(self, request):
        """

        :param request:
        :return: boolean
        """
        ftp_module = Container().dependency('pysftp')
        fnmatch_module = Container.dependency('fnmatch')
        os_module = Container.dependency('os')

        sftp = ftp_module.Connection(**request.connectionInfo)

        self.logging.info('Starting strategy secure...')

        for file in os_module.listdir(request.localPath):
            if fnmatch_module.fnmatch(file, request.prefix + request.pattern):
                self.logging.info('Uploading file %s...' % file)
                sftp.put(request.localPath + file, request.remotePath + '/' + file)

        self.logging.info('Files has been successfully uploaded to %s' % (request.connectionInfo['host']))

        sftp.close()

        return True

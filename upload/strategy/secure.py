from injectionContainer import Container


class Secure:
    def __init__(self, logging):
        self.logging = logging
        pass

    def upload(self, request):
        """

        :param request:
        :return: boolean
        """
        ftp_module = Container.dependency('pysftp')
        fnmatch_module = Container.dependency('fnmatch')
        os_module = Container.dependency('os')

        sftp = ftp_module.Connection(**request.connectionInfo)

        self.logging.info('Starting strategy secure...')

        for file in os_module.listdir(request.local_path):
            if fnmatch_module.fnmatch(file, request.provider + request.pattern):
                request.logging.info('Uploading file %s...' % file)
                sftp.put(request.requestlocal_path + file, request.remote_path + '/' + file)

        self.logging.info('Files has been successfully uploaded to %s' % (request.connection_info['host']))

        sftp.close()

        return True

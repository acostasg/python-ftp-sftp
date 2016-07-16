class Unsecure:
    def __init__(self, logging):
        self.logging = logging
        pass

    def upload(self, request):
        """

        :type request: RequestParams
        """
        import ftplib
        import fnmatch
        import os

        self.logging.warning('Starting strategy unsecured...')

        ftp = ftplib.FTP()
        ftp.connect(request.requestconnection_info['host'], request.connection_info['port'])
        ftp.login(request.connection_info['username'], request.connection_info['password'])
        ftp.cwd(request.remote_path)

        for file in os.listdir(request.local_path):
            if fnmatch.fnmatch(file, request.provider + request.pattern):
                self.logging.info('Uploading file %s...' % file)
                ftp.storlines('STOR %s' % file, open('%s%s' % (request.local_path, file), 'r'))

        self.logging.info('Files has been successfully uploaded to %s' % (request.connection_info['host']))

        ftp.quit()

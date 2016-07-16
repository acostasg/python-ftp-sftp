class Secure:
    def __init__(self, logging):
        self.logging = logging
        pass

    def upload(self, request):
        """

        :type request: RequestParams
        """
        import pysftp
        import fnmatch
        import os

        sftp = pysftp.Connection(**request.connectionInfo)

        self.logging.info('Starting strategy secure...')

        for file in os.listdir(request.local_path):
            if fnmatch.fnmatch(file, request.provider + request.pattern):
                request.logging.info('Uploading file %s...' % file)
                sftp.put(request.requestlocal_path + file, request.remote_path + '/' + file)

        self.logging.info('Files has been successfully uploaded to %s' % (request.connection_info['host']))

        sftp.close()

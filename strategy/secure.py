import pysftp
import fnmatch
import os

def secure_upload(request,logging):
    sftp = pysftp.Connection(**request.connection_info)

    logging.info('Starting strategy secure...')

    for file in os.listdir(request.local_path):
        if fnmatch.fnmatch(file, request.provider + request.pattern):
            request.logging.info('Uploading file %s...' % file)
            sftp.put(request.requestlocal_path + file, request.remote_path + '/' + file)

    logging.info('Files has been successfully uploaded to %s' % (request.connection_info['host']))

    sftp.close()

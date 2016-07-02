import pysftp
import fnmatch
import os

def secure_upload(connection_info, local_path, remote_path, provider, pattern, logging):
    sftp = pysftp.Connection(**connection_info)

    logging.info('Starting strategy secure...')

    for file in os.listdir(local_path):
        if fnmatch.fnmatch(file, provider + pattern):
            logging.info('Uploading file %s...' % file)
            sftp.put(local_path + file, remote_path + '/' + file)

    logging.info('Files has been successfully uploaded to %s' % (connection_info['host']))

    sftp.close()

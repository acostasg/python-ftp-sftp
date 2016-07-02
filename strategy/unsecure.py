import ftplib
import fnmatch
import os

def unsecured_upload(connection_info, local_path, remote_path, provider, pattern, logging):

    logging.warning('Starting strategy unsecured...')

    ftp = ftplib.FTP()
    ftp.connect(connection_info['host'], connection_info['port'])
    ftp.login(connection_info['username'], connection_info['password'])
    ftp.cwd(remote_path)

    for file in os.listdir(local_path):
        if fnmatch.fnmatch(file, provider + pattern):
            logging.info('Uploading file %s...' % file)
            ftp.storlines('STOR %s' % file, open('%s%s' % (local_path, file), 'r'))

    logging.info('Files has been successfully uploaded to %s' % (connection_info['host']))

    ftp.quit()

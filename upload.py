#!/usr/bin/env python

import sys
import getopt
import strategy.secure
import strategy.unsecure
import logging

host = ''
username = ''
secret = ''
localPath = ''
remotePath = ''
port = 0
provider = ''
secure = '1'

try:
    opts, args = getopt.getopt(
        sys.argv[1:], "h:p:u:s:l:r:o::c::",
        ["host=", "port=", "username=", "secret=", "local-path=",
         "remote-path=", "provider=", "is-secure="]
    )
    logging.basicConfig(filename='upload.log', level=logging.DEBUG)
except getopt.GetoptError:
    logging.warning(
        """Usage:\n
        ./upload.py <options>\n
        Options:
            -h, --host: FTP hostname
            -p, --port: FTP username
            -s, --secret: FTP account password
            -l, --local-path: Local path where files are
            -r, --remote-path: Remote path where files will be uploaded
            -o, --provider:[optional] Provider name
            -c, --is-secure:[optional] 1 for sftp or 2 for ftp
            """
    )
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-h', '--host'):
        host = arg
    elif opt in ('-p', '--port'):
        port = arg
    elif opt in ('-u', '--username'):
        username = arg
    elif opt in ('-s', '--secret'):
        secret = arg
    elif opt in ('-l', '--local-path'):
        localPath = arg
    elif opt in ('-r', '--remote-path'):
        remotePath = arg
    elif opt in ('-o', '--provider'):
        provider = arg
    elif opt in ('-c', '--is-secure'):
        secure = arg

if not provider:
    provider = username

logging.debug('Provider is ', provider)
logging.debug('Host is ', host)
logging.debug('Username is ', username)
logging.debug('Local path is ', localPath)
logging.debug('Remote path is ', remotePath)

connectionInfo = {'host': host, 'username': username, 'password': secret, 'port': int(port)}

if secure == '1':
    logging.debug('Strategy secure')
    strategy.secure.secure_upload(connectionInfo, localPath, remotePath, provider, logging)
elif secure == '0':
    logging.debug('Strategy unsecured')
    strategy.unsecure.unsecured_upload(connectionInfo, localPath, remotePath, provider, logging)

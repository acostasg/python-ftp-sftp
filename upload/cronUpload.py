#!/usr/bin/env python

import getopt
import logging
import sys

from strategy \
    import strategyFactory, requestParams

host = ''
username = ''
secret = ''
localPath = ''
remotePath = ''
port = 0
prefix = ''
secure = 1
pattern = '*.csv'

try:
    opts, args = getopt.getopt(
        sys.argv[1:], "h:p:u:s:l:r:o::c::e::",
        ["host=", "port=", "username=", "secret=", "local-path=",
         "remote-path=", "provider=", "is-secure=", "files-extension"]
    )
    logging.basicConfig(filename='./../logs/cronUpload.log', level=logging.DEBUG)
except getopt.GetoptError:
    print(
        """Usage:\n
        ./cronUpload.py <options>\n
        Options:
            -h, --host: FTP hostname
            -p, --port: FTP username
            -s, --secret: FTP account password
            -l, --local-path: Local path where files are
            -e, --files-extension:[optional] file extension default csv
            -r, --remote-path: Remote path where files will be uploaded
            -o, --prefix:[optional] Initial characters to files name
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
    elif opt in ('-o', '--prefix'):
        prefix = arg
    elif opt in ('-c', '--is-secure'):
        secure = arg
    elif opt in ('-e', '--files-extension'):
        pattern = '*.' + arg

connectionInfo = {'host': host, 'username': username, 'password': secret, 'port': int(port)}

request = requestParams.RequestParams()
request.connectionInfo = connectionInfo
request.localPath = localPath
request.remotePath = remotePath
request.prefix = prefix
request.pattern = pattern

strategyObject = strategyFactory.Strategy(int(secure), logging)
strategyObject.upload(request)

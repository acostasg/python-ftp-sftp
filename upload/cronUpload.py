#!/usr/bin/env python

import getopt
import logging
import sys

from upload.strategy \
    import strategyFactory, requestParams

host = ''
username = ''
secret = ''
local_path = ''
remote_path = ''
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
    raise Exception('Invalid params')

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
        local_path = arg
    elif opt in ('-r', '--remote-path'):
        remote_path = arg
    elif opt in ('-o', '--prefix'):
        prefix = arg
    elif opt in ('-c', '--is-secure'):
        secure = arg
    elif opt in ('-e', '--files-extension'):
        pattern = '*.' + arg


def execute_cron(
        host_param,
        username_param,
        secret_param,
        port_param,
        local_path_param,
        remote_path_param,
        prefix_param,
        pattern_param,
        secure_param
):
    """
    Execute strategy unsecure

    :param host_param:
    :param username_param:
    :param secret_param:
    :param port_param:
    :param local_path_param:
    :param remote_path_param:
    :param prefix_param:
    :param pattern_param:
    :param secure_param:
    :return:
    """
    connection_info = {'host': host_param, 'username': username_param, 'password': secret_param,
                       'port': int(port_param)}
    request = requestParams.RequestParams()
    request.connectionInfo = connection_info
    request.localPath = local_path_param
    request.remotePath = remote_path_param
    request.prefix = prefix_param
    request.pattern = pattern_param
    strategy_instance = strategyFactory.Strategy(int(secure_param))
    strategy_instance.upload(request)

    return True


execute_cron(host, username, secret, port, local_path, remote_path, prefix, pattern, secure)

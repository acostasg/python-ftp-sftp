#!/usr/bin/env python

import getopt
import logging
import sys
import yaml
import strategy.secure
import strategy.unsecure
from strategy import requestParams

host = ''
username = ''
secret = ''
localPath = ''
remotePath = ''
port = 0
provider = ''
secure = '1'
pattern = '*.csv'

try:
    logging.basicConfig(filename='upload.log', level=logging.DEBUG)

    # @TODO move to object config to cache lazzy for yml
    with open('/app.yml', 'r') as appConfig:
        docAppConfig = yaml.load(appConfig)
    with open('/connections.yml', 'r') as connectionsConfig:
        docConnectionsConfig = yaml.load(connectionsConfig)


except getopt.GetoptError:
    logging.warning(
        """Corrupt configuration files or not is located in the configuration directory.\n
            /config/app.yml\n
            /config/connections.yml
            """
    )
    sys.exit(2)

if not provider:
    provider = username

logging.debug('Provider is ', provider)
logging.debug('Host is ', host)
logging.debug('Username is ', username)
logging.debug('Local path is ', localPath)
logging.debug('Remote path is ', remotePath)
logging.debug('File extension is ', pattern)

connectionInfo = {'host': host, 'username': username, 'password': secret, 'port': int(port)}

request = requestParams.RequestParams()
request.connectionInfo = connectionInfo
request.localPath = localPath
request.remotePath = remotePath
request.prefix = provider
request.pattern = pattern

if secure == '1':
    logging.debug('Strategy secure')
    try:
        strategy.secure.secure_upload(request, logging)
    except Exception, e:
        logging.error(e.message)
        sys.exit(2)

elif secure == '0':
    logging.debug('Strategy unsecured')
    try:
        strategy.unsecure.unsecured_upload(request, logging)
    except Exception, e:
        logging.error(e.message)
        sys.exit(2)

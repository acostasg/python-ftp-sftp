#!/usr/bin/env python

import logging
import os
import sys
import yaml
import getopt
from strategy \
    import StrategyFactory
from config \
    import ConfigApp

try:
    logging.basicConfig(filename='./../logs/upload.log', level=logging.DEBUG)
    handleConfigApp = ConfigApp.Handle(os, yaml)

except Exception, e:
    logging.warning(
        """Corrupt configuration files or not is located in the configuration directory.\n
            /config/app.yml\n
            /config/connections.yml
            """ + e.message
    )
    sys.exit(2)

try:
    strategyObject = StrategyFactory.Strategy(
        handleConfigApp.get_strategy(),
        logging
    )

    strategyObject.upload(
        handleConfigApp.get_request(
            handleConfigApp.get_strategy()
        )
    )
except Exception, e:
    logging.error(e)
    sys.exit(2)

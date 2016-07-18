#!/usr/bin/env python
from injectionContainer import Container
from strategy import strategyFactory

def execute(log, config_app, system, os, yaml):
    log.basicConfig(filename='./../logs/appUpload.log', level=log.DEBUG)

    try:
        handle_config_app = config_app.Handle(os, yaml)
    except Exception, e:
        log.warning(
            """Corrupt configuration files or not is located in the configuration directory.\n
                /config/app.yml\n
                /config/connections.yml
                """ + e.message
        )
        system.exit(2)

    try:
        strategy = strategyFactory.Strategy(
            handle_config_app.get_strategy(),
            log
        )

        strategy.upload(
            handle_config_app.get_request(
                handle_config_app.get_strategy()
            )
        )
    except Exception, e:
        log.error(e)
        system.exit(2)


execute(
    Container.dependency('logger'),
    Container.dependency('config_app'),
    Container.dependency('sys'),
    Container.dependency('os'),
    Container.dependency('yaml')
)

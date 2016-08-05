#!/usr/bin/env python
from injectionContainer import Container
from strategy import strategyFactory


def execute(logger, config_app, system, os, yaml):
    logger.basicConfig(filename='./../logs/appUpload.log', level=logger.DEBUG)

    try:
        handle_config_app = config_app.Handle(os, yaml)
    except Exception as e:
        logger.warning(
            """Corrupt configuration files or not is located in the configuration directory.\n
                /config/app.yml\n
                /config/connections.yml
                """ + str(e)
        )
        system.exit(2)

    try:
        strategy = strategyFactory.Strategy(
            handle_config_app.get_strategy(),
            logger
        )

        strategy.upload(
            handle_config_app.get_request(
                handle_config_app.get_strategy()
            )
        )
    except Exception as e:
        logger.error(e)
        system.exit(2)

execute(
    Container.dependency('logger'),
    Container.dependency('config_app'),
    Container.dependency('sys'),
    Container.dependency('os'),
    Container.dependency('yaml')
)

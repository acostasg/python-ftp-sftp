#!/usr/bin/env python
from upload.injectionContainer import Container
from upload.strategy import strategyFactory


def execute(logger, config_app, os, yaml):
    """
        App with config files
    :param logger:
    :param config_app:
    :param os:
    :param yaml:
    :return: True
    """
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
        raise Exception('Corrupt configuration files')

    try:
        strategy = strategyFactory.Strategy(
            handle_config_app.get_strategy()
        )

        strategy.upload(
            handle_config_app.get_request(
                handle_config_app.get_strategy()
            )
        )

        return True
    except Exception as e:
        logger.error(e)
        raise Exception(e)


execute(
    Container.dependency('logger'),
    Container.dependency('config_app'),
    Container.dependency('os'),
    Container.dependency('yaml')
)

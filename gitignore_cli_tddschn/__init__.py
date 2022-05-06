__version__ = '0.2.1'
__app_name__ = 'gitignore CLI'
__app_name_slug__ = 'gitignore-cli'

try:
    from logging_utils_tddschn import get_logger
    logger, _ = get_logger(__app_name_slug__)
except:
    import logging
    from logging import NullHandler
    logger = logging.getLogger(__app_name_slug__)
    logger.addHandler(NullHandler())

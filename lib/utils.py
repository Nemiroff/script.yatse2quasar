# -*- coding: utf-8 -*-
import sys
import xbmc, xbmcaddon
import logging

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
_settings = xbmcaddon.Addon(id=ADDON_ID)


class XBMCHandler(logging.StreamHandler):
    xbmc_levels = {
        'DEBUG': 0,
        'INFO': 2,
        'WARNING': 3,
        'ERROR': 4,
        'LOGCRITICAL': 5,
    }

    def emit(self, record):
        xbmc_level = self.xbmc_levels.get(record.levelname)
        if isinstance(record.msg, unicode):
            record.msg = record.msg.encode('utf-8')
        xbmc.log(self.format(record), xbmc_level)

loggers = {}

def _get_logger(name):
    global loggers

    if loggers.get(name):
        return loggers.get(name)
    else:
        logger = logging.getLogger(ADDON_ID)
        logger.setLevel(logging.DEBUG)
        handler = XBMCHandler()
        handler.setFormatter(logging.Formatter('[script.yatse2elementum] %(message)s'))
        logger.addHandler(handler)
        return logger

log = _get_logger(__name__)

def start(url):
    log.debug('Open url %s' % url)
    xbmc.executebuiltin('XBMC.RunPlugin(%s)' % url)

def _getSetting(key):
    return _settings.getSetting(key)
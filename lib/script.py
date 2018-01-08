# -*- coding: utf-8 -*-
from utils import log, _getSetting, start

def run(args):
    if args == '':
        log.debug("No given args")
    else:
        open_with = _getSetting('open_with')
        if open_with == 'Elementum':
            start('plugin://plugin.video.elementum/playuri' + args + ')')
        elif open_with == 'Torrenter V2':
            start('plugin://plugin.video.torrenter/?action=playSTRM&url'+ args[4:] + ')')
        elif open_with == 'Quasar':
            start('plugin://plugin.video.quasar/playuri' + args + ')')

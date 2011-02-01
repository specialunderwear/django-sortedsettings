#! /usr/bin/env python
import re
import pickle
import settings.base as settings_module

SETTING_PATTERN_LOOSE = re.compile(r'^[_0-9A-Z]+')
SETTING_PATTERN_STRICT = re.compile(r'^[_0-9A-Z]+$')

group = None

for key in sorted(filter(SETTING_PATTERN_STRICT.match, dir(settings_module))):
    # group settings by first word
    if not group or group not in key:
        group = key[0:key.find('_')]
        print ""
    
    active = False
    code_buffer = ""

    with open('settings/base.py') as settings_file:
        for line in settings_file:
            # when a new settings block is found, reset buffer.
            if SETTING_PATTERN_LOOSE.match(line):
                active = False
                code_buffer = ""
            
            # if the key is found, activate output of settings block
            if line.find(key) == 0:
                active = True
            
            # output block but skip empty lines and comments
            if active and not re.match(r'$\S*^', line) and line[0] != '#':
                code_buffer += line[-1]
                print line[:-1]

                context = dict()

                # check if the current outputted block is complete by using
                # eval and comparison with the value from the module
                try:
                    code_buffer = line
                    exec code_buffer in settings_module.__dict__, context
                except Exception as e:
                    pass

                if context.get(key) == getattr(settings_module, key):
                    active = False
                    code_buffer = ""

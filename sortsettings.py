#! /usr/bin/env python
import sys
import getopt
import re
import os

sys.path.append(os.getcwd())

SETTING_PATTERN_LOOSE = re.compile(r'^[_0-9A-Z]+')
SETTING_PATTERN_STRICT = re.compile(r'^[_0-9A-Z]+$')

def main():
    if len(sys.argv) > 1:
        module_name = sys.argv[1]
        __import__(module_name, globals(), locals(), [], -1)
        settings_module = sys.modules[module_name]
    else:
        import settings as settings_module
    
    group = None
    
    for key in sorted(filter(SETTING_PATTERN_STRICT.match, dir(settings_module))):
    
        active = False
        code_buffer = ""
        found = False
        
        with open(re.sub(r'pyc|pyo', 'py', settings_module.__file__)) as settings_file:
            for line in settings_file:
                # when a new settings block is found, reset buffer.
                if SETTING_PATTERN_LOOSE.match(line):
                    active = False
                    code_buffer = ""
            
                # if the key is found, activate output of settings block
                if line.find(key) == 0:
                    active = True
                    found = True
            
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
                        break

        # group settings by first word
        if (not group or group not in key) and found:
            group = key[0:key.find('_')]
            print ""
        
if __name__ == "__main__":
    sys.exit(main())
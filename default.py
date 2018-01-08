import sys
from lib import script

try:
    args = sys.argv[2]
except IndexError:
    args = ''
finally:
    script.run(args)

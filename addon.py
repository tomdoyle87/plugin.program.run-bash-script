"""
    Plugin to run bash script
"""

# -*- coding: UTF-8 -*-
# main imports

import xbmc
import xbmcgui
import xbmcaddon
import subprocess
import time

# plugin constants
__plugin__ = "Run Bash script from a program plugin "
__author__ = "tomdoyle87"
__url__ = "https://github.com/tomdoyle87"
__git_url__ = "https://github.com/tomdoyle87/plugin.program.run-bash-script"
__credits__ = "tomdoyle87"
__version__ = "0.0.1"

os.system("/bin/echo -e '{0}\n{0}' | /usr/bin/sudo /usr/bin/passwd osmc" .format(Osmc))
time.sleep(5)
subprocess.Popen(["/home/osmc/bin/getstreamlist", "R"])
dialog.ok("Streams updated")

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
__plugin__ = "Run Bash script from a program plugin"
__author__ = "tomdoyle87"
__git_url__ = "https://github.com/tomdoyle87/plugin.program.run-bash-script"
__credits__ = "tomdoyle87"
__version__ = "0.0.2"

subprocess.Popen(["/home/osmc/bin/getstreamlist", "R"])
time.sleep(5)
dialog.ok("Streams updated")
~                             

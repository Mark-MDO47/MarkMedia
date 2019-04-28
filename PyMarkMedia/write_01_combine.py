#
# Mark Olson
#
# combine_MarkMedia.py is used to insert my specific code into wxFormBuilder output.
# combine.sh
#    changes tabs to spaces so I don't have a crazy mixture
#    runs all the write_*_combine.py to create the YAML files
#    runs this file on each of the sorted YAML files
#        YAML file has cmds, events, inputFile and outputFile
#        cmds are done in order; events can happen in any order
#
import os
import sys
import yaml

inpFile  = "_00_MarkMedia.py"
otpFile  = "_01_MarkMedia.py"

# events will be processed in any order; make sure they are unique
events = []

# cmds are checked one at a time, waiting until each is done in order before moving to the next
cmds = [
        ["afteraddtext", "coding: utf-8", "\nimport sys\nimport os\nfrom time import sleep\n", "unused"],
        ["afterskipto", "## http://www.wxformbuilder.org/", "#################################", "unused"],
        ["aftercopyfilefrom",  "import wx.xrc", "import gettext", "_00_DialogEnterVidNum.py"],
        ["afteraddtext", "wx.Frame.__init__", "\n        self.m_txtFilePath = \"UNKNOWN\" # absolute path to open text file\n        self.m_txtFileLines = []       # lines for open text file, stripped\n        self.m_txtFileIdx = -1         # which line for open text file or -1\n        self.m_mediaLength = None # the length of media file; appears to be in milliseconds\n        self.m_mediaLoad = False  # True when media load done until timer processes it\n\n        self.SetIcon(wx.Icon(\"MadScience_256.ico\")) # Mark: set icon\n\n", "unused"],
        ["afterskipto", "bSizerPanel.Add( self.m_staticTextStatus,", "bSizer3 = wx.BoxSizer(", "unused"],   # remove placeholder m_notebookMediaCtrl to make room for m_mediactrl
        ["afteraddtext", "def __del__( self", "        del self.m_mediactrl\n", "unused"],
        ["atendaddtext", "unused", "###########################################################################\n## MAIN PROGRAM\n###########################################################################\n\napp = wx.App()\nframe = MainFrame(None).Show()\napp.MainLoop()\n", "unused"]
]

data = {"events": events, "cmds": cmds, "inpFile": inpFile, "otpFile": otpFile}

fp = open('01_combine.yaml', 'wt')
yaml.dump(data, fp)
fp.close()



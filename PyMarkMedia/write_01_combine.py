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
        ["afterskippastcopyentirefilefrom", "class MainFrame ( ", "def __init__( self, parent )", "_01_FrameInit_def.py"],
        ["afterskippastcopyentirefilefrom", "wx.Frame.__init__ (", "self.SetSizeHints(", "_01_FrameInit.py"],
        ["afterskipto", "bSizerPanel.Add( self.m_staticTextStatus,", "bSizer3 = wx.BoxSizer(", "unused"],   # remove placeholder m_notebookMediaCtrl to make room for m_mediactrl
        ["afteraddtext", "def __del__( self", "        del self.m_mediactrl\n", "unused"],
        ["atendaddtext", "unused", "###########################################################################\n## MAIN PROGRAM\n###########################################################################\n\napp = wx.App()\nframe = MainFrame(None, os.path.dirname(os.path.realpath(__file__))).Show()\napp.MainLoop()\n", "unused"]
]

data = {"events": events, "cmds": cmds, "inpFile": inpFile, "otpFile": otpFile}

fp = open('01_combine.yaml', 'wt')
yaml.dump(data, fp)
fp.close()

import os
import sys
import yaml

inpFile  = "../wxFormBuilder_MarkMedia/MarkMedia.py"
otpFile  = "_01_MarkMedia.py"

# events will be processed in any order; make sure they are unique
events = []

# cmds are checked one at a time, waiting until each is done in order before moving to the next
cmds = [
        ["afteraddtext", "coding: utf-8", "\nimport sys\nimport os\n", "unused"],
        ["afterskipto", "## http://www.wxformbuilder.org/", "#################################", "unused"],
        ["aftercopyfilefrom",  "import wx.xrc", "import gettext", "../wxFormBuilder_MarkMedia/DialogEnterVidNum.py"],
        ["afteraddtext", "wx.Frame.__init__", "\n\t\tself.SetIcon(wx.Icon(\"MadScience_256.ico\")) # Mark: set icon\n\n", "unused"],
        ["afteraddtext", "self.m_notebookMediaCtrl.SetMinSize(", "\t\tself.m_mediactrl = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER)\n", "unused"],
        ["atendaddtext", "unused", "###########################################################################\n## MAIN PROGRAM\n###########################################################################\n\napp = wx.App()\nframe = MainFrame(None).Show()\napp.MainLoop()\n", "unused"]
]

data = {"events": events, "cmds": cmds, "inpFile": inpFile, "otpFile": otpFile}

fp = open('01_combine.yaml', 'wt')
yaml.dump(data, fp)
fp.close()


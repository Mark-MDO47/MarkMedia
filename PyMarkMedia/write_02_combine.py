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

inpFile  = "_01_MarkMedia.py"
otpFile  = "MarkMedia.py"

# events will be processed in any order; make sure they are unique
events = []
eventFn = "_02_event_handlers.py"
fobj_events = open(eventFn, 'rt')
eventLines = fobj_events.readlines()
fobj_events.close()
status = "start"
tmp1 = "string to search for"
tmp2 = "string to copy in"
for line in eventLines:
    if (-1 != line.find("def ")) and (-1 == line.find("# keep copying")):
        if "capture" == status:
            status = "start"
            events.append([tmp1, tmp2])
        if "start" == status:
            status = "capture"
            tmp1 = line[line.find("def "):line.find("(")+1]
            tmp2 = ""
    elif "capture" == status:
        tmp2 += line
if "capture" == status:
    events.append([tmp1, tmp2])

"""
events = [
           ["def OnFileOpen(", "        dlg = wx.FileDialog(self, message=\"Choose a media file\", defaultDir=os.getcwd(), defaultFile=\"\", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)\n\n        if dlg.ShowModal() == wx.ID_OK:\n            path = dlg.GetPath()\n            self.DoLoadFile(path)\n\n    def DoLoadFile(self, path):\n        # self.m_buttonPlay.Disable() ### FIXME\n        if not self.m_mediactrl.Load(path):\n            wx.MessageBox(\"Unable to load %s: Unsupported format?\" % path, \"ERROR\", wx.ICON_ERROR | wx.OK)\n        else:\n            self.m_mediactrl.SetInitialSize()\n            self.GetSizer().Layout()\n"],
           ["def onBtnPlay(",  "        if not self.m_mediactrl.Play():\n            wx.MessageBox(\"Unable to Play media : Unsupported format?\",\n                \"ERROR\", wx.ICON_ERROR | wx.OK)\n        else:\n            self.m_mediactrl.SetInitialSize()\n            self.GetSizer().Layout()\n"],
           ["def onBtnStop(", "        self.m_mediactrl.Stop()\n"],
           ["def onBtnEnterVidNum(", "        DlgEnterVidNum(self).ShowModal()\n"]
]
"""

# cmds are checked one at a time, waiting until each is done in order before moving to the next
cmds =  [
            ["afteraddtext",  "import wx.xrc", "import wx.media\n", "unused"],
            ["afteraddtext", "bSizerPanel.Add( self.m_staticTextStatus,", "        self.m_mediactrl = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER, size=wx.Size( 800,800 ))\n        bSizerPanel.Add( self.m_mediactrl, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )\n\n", "unused"] # add m_mediactrl in place of placeholder m_notebookMediaCtrl
        ]

data = {"events": events, "cmds": cmds, "inpFile": inpFile, "otpFile": otpFile}

fp = open('02_combine.yaml', 'wt')
yaml.dump(data, fp)
fp.close()


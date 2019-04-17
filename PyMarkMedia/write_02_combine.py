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
           ["def OnFileOpen(", "\t\tdlg = wx.FileDialog(self, message=\"Choose a media file\", defaultDir=os.getcwd(), defaultFile=\"\", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)\n\n\t\tif dlg.ShowModal() == wx.ID_OK:\n\t\t\tpath = dlg.GetPath()\n\t\t\tself.DoLoadFile(path)\n\n\tdef DoLoadFile(self, path):\n\t\t# self.m_buttonPlay.Disable() ### FIXME\n\t\tif not self.m_mediactrl.Load(path):\n\t\t\twx.MessageBox(\"Unable to load %s: Unsupported format?\" % path, \"ERROR\", wx.ICON_ERROR | wx.OK)\n\t\telse:\n\t\t\tself.m_mediactrl.SetInitialSize()\n\t\t\tself.GetSizer().Layout()\n"],
           ["def onBtnPlay(",  "\t\tif not self.m_mediactrl.Play():\n\t\t\twx.MessageBox(\"Unable to Play media : Unsupported format?\",\n\t\t\t\t\"ERROR\", wx.ICON_ERROR | wx.OK)\n\t\telse:\n\t\t\tself.m_mediactrl.SetInitialSize()\n\t\t\tself.GetSizer().Layout()\n"],
           ["def onBtnStop(", "\t\tself.m_mediactrl.Stop()\n"],
           ["def onBtnEnterVidNum(", "\t\tDlgEnterVidNum(self).ShowModal()\n"]
]
"""

# cmds are checked one at a time, waiting until each is done in order before moving to the next
cmds =  [
            ["afteraddtext",  "import wx.xrc", "import wx.media\n", "unused"],
            ["afteraddtext", "bSizerPanel.Add( self.m_staticTextStatus,", "\t\tself.m_mediactrl = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER, size=wx.Size( 800,800 ))\n\t\tbSizerPanel.Add( self.m_mediactrl, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )\n\n", "unused"] # add m_mediactrl in place of placeholder m_notebookMediaCtrl
        ]

data = {"events": events, "cmds": cmds, "inpFile": inpFile, "otpFile": otpFile}

fp = open('02_combine.yaml', 'wt')
yaml.dump(data, fp)
fp.close()


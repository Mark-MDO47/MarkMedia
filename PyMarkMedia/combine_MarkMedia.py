
import sys
import io
import yaml

######################################################################################
# here is example after being read in for use
######################################################################################
#   inpFile  = "../wxFormBuilder_MarkMedia/MarkMedia.py"
#   otpFile  = "MarkMedia.py"

# events will be processed in any order; make sure they are unique
#   events = [
           #   ["def onBtnEnterVidNum(", "        DlgEnterVidNum(self).ShowModal()\n"]
#   ]

# cmds are checked one at a time, waiting until each is done in order before moving to the next
#   cmds = [
        #   ["afterskipto", "## http://www.wxformbuilder.org/", "#################################", "unused"],
        #   ["aftercopyfilefrom",  "import wx.xrc", "import gettext", "../wxFormBuilder_MarkMedia/DialogEnterVidNum.py"],
        #   ["afteraddtext", "wx.Frame.__init__", "\n        self.SetIcon(wx.Icon(\"MadScience_256.ico\")) # Mark: set icon\n\n", "unused"],
        #   # moved to events ["afterreplaceline", "def onBtnEnterVidNum(", "        DlgEnterVidNum(self).ShowModal()\n", "unused"],
        #   ["atendaddtext", "unused", "###########################################################################\n## MAIN PROGRAM\n###########################################################################\n\napp = wx.App()\nframe = MainFrame(None).Show()\napp.MainLoop()\n", "unused"]
#   ]


cmdcmd = 0
cmdaftr = 1
cmdtext = 2
cmdfile = 3

def getline(fobj, numline):
    myLine = fobj.readline()
    numline += 1
    return numline, myLine

def doMain(inpFile="unknown", otpFile="unknown", events=[], cmds=[]):

    fobj_inp = open(inpFile, "rt")
    fobj_otp = open(otpFile, "wt")
    
    cmdidx = 0
    line = "start your engines"
    numline = 0
    while len(line) > 0:

            # always read and write the next line before processing; that is why cmds and events are "after..."
       numline, line = getline(fobj_inp, numline)
       if len(line) <= 0:
           break
       fobj_otp.write(line)

       # events will be processed in any order; make sure they are unique
       for evt in events:
           if line.find(evt[0]) != -1:
               sys.stdout.write("DEBUG installing event line %d: %s" % (numline, line))
               numline, line = getline(fobj_inp, numline) # remove original event.Skip()
               fobj_otp.write(evt[1])
               break

       # cmds are checked one at a time, waiting until each is done in order before moving to the next
       if cmdidx >= len(cmds):
           continue
       theCmd = cmds[cmdidx][cmdcmd]
            # atend... finish copying the input file then add the cmdtext - only atendaddtext at this time
       if theCmd.find("atend") != -1:
           sys.stdout.write("DEBUG atend line %d: %s" % (numline, line))
           continue # just copy the rest of the lines
            # afterskipto... after seeing cmdaftr, skip input file until see cmdtext
       elif (theCmd.find("afterskipto") != -1) and (line.find(cmds[cmdidx][cmdaftr]) != -1):
           thetext = cmds[cmdidx][cmdtext]
           sys.stdout.write("DEBUG found line %d: %s    skipping till %s\n" % (numline, line, thetext))
           line = ""
           while line.find(thetext) == -1:
               sys.stdout.write("DEBUG skipping line %d: %s" % (numline, line))
               numline, line = getline(fobj_inp, numline) # keep skipping
           sys.stdout.write("DEBUG done skipping found line %d: %s" % (numline, line))
           fobj_otp.write(line)
           cmdidx += 1
            # afteraddtext... after seeing cmdaftr, write cmdtext
       elif (theCmd.find("afteraddtext") != -1) and (line.find(cmds[cmdidx][cmdaftr]) != -1):
           sys.stdout.write("DEBUG afteraddtext line %d: %s" % (numline, line))
           fobj_otp.write(cmds[cmdidx][cmdtext])
           cmdidx += 1
            # afterreplaceline... after seeing cmdaftr, skip next input line and write cmdtext - easier to do with events if unique
       elif (theCmd.find("afterreplaceline") != -1) and (line.find(cmds[cmdidx][cmdaftr]) != -1):
           sys.stdout.write("DEBUG afterreplaceline line %d: %s" % (numline, line))
           numrepl = 1 # have not found a need for multiple line replace yet
           while numrepl > 0:
               sys.stdout.write("DEBUG skipping replace line %d: %s" % (numline, line))
               numline, line = getline(fobj_inp, numline) # keep skipping
               numrepl -= 1
           fobj_otp.write(cmds[cmdidx][cmdtext])
           cmdidx += 1
            # aftercopyfilefrom... after seeing cmdaftr, open cmdfile then read till find cmdtext and copy that line and all the rest of cmdfile
       elif (theCmd.find("aftercopyfilefrom") != -1) and (line.find(cmds[cmdidx][cmdaftr]) != -1):
           sys.stdout.write("DEBUG aftercopyfilefrom line %d: %s    read file %s\n" % (numline, line, cmds[cmdidx][cmdfile]))
           copyit = False
           fobj_copy = open(cmds[cmdidx][cmdfile], "rt")
           for cpyline in fobj_copy:
               if cpyline.find(cmds[cmdidx][cmdtext]) != -1:
                   copyit = True
               if copyit:
                   fobj_otp.write(cpyline)
           fobj_copy.close()
           cmdidx += 1
           pass
    
    
    fobj_inp.close()
        # final processing of atend...
    while cmdidx < len(cmds):
       if cmds[cmdidx][cmdcmd].find("atendaddtext") != -1:
           fobj_otp.write(cmds[cmdidx][cmdtext])
       else:
           sys.stderr.write("ERROR found cmd#%d %s at end of input file\n" % (cmdidx, cmds[cmdidx][cmdcmd]))
       cmdidx += 1
    fobj_otp.close()


def getMyParms(fname):
    data = {}

    fobj_parms = open(fname, "rt")
    data = yaml.safe_load(fobj_parms)
    fobj_parms.close()
    return data["inpFile"], data["otpFile"], data["events"], data["cmds"]

# always reads and writes the next input line before processing; that is why cmds and events are "after..."
#
# events will be processed in any order; make sure they are unique
#    events find and copy the text then replace the next line with new line(s)
#
# cmds are checked one at a time, waiting until each is done in order before moving to the next
# here are the commands:
#    atend... finish copying the input file then add the cmdtext - only atendaddtext at this time
#    afterskipto... after seeing cmdaftr, skip input file until see cmdtext
#    afteraddtext... after seeing cmdaftr, write cmdtext
#    afterreplaceline... after seeing cmdaftr, skip next input line and write cmdtext - easier to do with events if unique
#    aftercopyfilefrom... after seeing cmdaftr, open cmdfile then read till find cmdtext and copy that line and all the rest of cmdfile
if __name__ == "__main__":
    if 2 != len(sys.argv):
        print("ERROR: need exactly one param: YAML input file for %s" % sys.argv[0])
        exit(1)
    inpFile, otpFile, events, cmds = getMyParms(sys.argv[1])
    doMain(inpFile=inpFile, otpFile=otpFile, events=events, cmds=cmds)

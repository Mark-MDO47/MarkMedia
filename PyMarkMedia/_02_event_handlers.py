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
# This file has the "event handlers" that get replaced in any order.
# This is read by write_02_combine.html and turned into YAML.
#

    # Virtual event handlers, overide them in your derived class
    def onBtnPrevFile( self, event ):
        event.Skip()            # need to write this one

    def onBtnPrev( self, event ):
        event.Skip()            # need to write this one


    def onBtnPlay( self, event ):
        if not self.m_mediactrl.Play():
            wx.MessageBox("Unable to Play media : Unsupported format?",
                "ERROR", wx.ICON_ERROR | wx.OK)
        else:
            self.m_mediactrl.SetInitialSize()
            self.GetSizer().Layout()


    def onBtnPause( self, event ):
        self.m_mediactrl.Pause()

    def onBtnNext( self, event ):
        event.Skip()            # need to write this one


    def onBtnNextFile( self, event ):
        event.Skip()            # need to write this one

    def onBtnEnterVidNum( self, event ):
        DlgEnterVidNum(self).ShowModal()


    def onBtnLouder( self, event ):
        # increase volume by 5 percent; makes assumption that current volume is valid
                self.m_mediactrl.SetVolume(min(1.0, self.m_mediactrl.GetVolume()+0.05))


    def onBtnSofter( self, event ):
        # decrease volume by 5 percent; makes assumption that current volume is valid
                self.m_mediactrl.SetVolume(max(0.0, self.m_mediactrl.GetVolume()-0.05))


    def onLBoxVidComments( self, event ):
        event.Skip()            # need to write this one


    def onListBoxDClickVidComments( self, event ):
        event.Skip()            # need to write this one


    def OnFileOpen( self, event ):
        dlg = wx.FileDialog(self, message="Choose a media file", defaultDir=os.getcwd(), defaultFile="", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.DoLoadFile(path)
            self.m_mediactrl.SetInitialSize()
            self.m_mediaLength = None
            #     print("Open length %s" % self.m_mediaLength)
            # onTimerMedia() will cause the video to play and show an early frame

    def DoLoadFile(self, path): # keep copying - this is in addition to OnFileOpen
        # self.m_buttonPlay.Disable() ### FIXME
        if not self.m_mediactrl.Load(path):
            wx.MessageBox("Unable to load %s: Unsupported format?" % path, "ERROR", wx.ICON_ERROR | wx.OK)
        else:
            # print(" m_bLoaded=%d" % self.m_mediactrl.m_bLoaded) # not in wxPython
            self.m_mediactrl.SetInitialSize()
            self.GetSizer().Layout()

    def fromMarksWeirdNumbers(self, theNumberText): # keep copying - this is in addition to OnFileOpen
        # for historical reasons numbering is
        # leftmost digit: _01...9A...Z
        # next     digit: 01...9A...Z
        # next 3  digits: 01...9
        # (example: _0001 to _Z999 to 00000 to 99999 to 9A000 to 9Z999 to A0000 to ZZ999)

        if type(theNumberText) != type('123'):
            dlgRslt = wx.MessageBox("ERROR: cannot convert input type %s inside fromMarksWeirdNumbers()" % (type(theNumberText)), "Bad Inputs", wx.ICON_EXCLAMATION|wx.CENTRE)
            good = False
        theNumberText = theNumberText.upper()
        good = True
        converted = 0
        if len(theNumberText) < len(self.MarksWeirdDigits):
            good = False
            converted = -1
        if good:
            for idx in range(len(self.MarksWeirdDigits)):
                converted *= len(self.MarksWeirdDigits[idx])
                tmp = self.MarksWeirdDigits[idx].find(theNumberText[idx])
                if -1 != tmp:
                    converted += tmp
                else:
                    good = False
                    converted = -1
                    break
        return good, converted

    def toMarksWeirdNumbers(self, theNumber): # keep copying - this is in addition to OnFileOpen
        # see fromMarksWeirdNumbers() for description of strange numbering scheme
        good = True
        converted = "_0000" # zero
        if type(theNumber) == type("123"): # if it is a string
            theNumber = int(theNumber)
        if type(theNumber) != type(123):
            dlgRslt = wx.MessageBox("ERROR: cannot convert %s type %s inside toMarksWeirdNumbers()" % (str(theNumber), type(theNumber)), "Bad Inputs", wx.ICON_EXCLAMATION|wx.CENTRE)
            good = False
        else:
            # FIXME let's cheat a little; we know some things about this...
            last3 = "%3d" % (theNumber % 1000)
            first2int = int(theNumber // 1000)
            firstint = int(first2int // len(self.MarksWeirdDigits[1]))
            secondint = first2int - firstint*len(self.MarksWeirdDigits[1])
            if firstint > len(self.MarksWeirdDigits[0]):
                theMax = ((len(self.MarksWeirdDigits[0])-1) * len(self.MarksWeirdDigits[1]) + (len(self.MarksWeirdDigits[1])-1))*1000 + 999
                dlgRslt = wx.MessageBox("ERROR: cannot convert %d: larger than max %d inside toMarksWeirdNumbers()" % (theNumber, theMax), "Bad Inputs", wx.ICON_EXCLAMATION|wx.CENTRE)
                good = False
            else:
                converted = self.MarksWeirdDigits[0][firstint] + self.MarksWeirdDigits[1][secondint] + last3
        return good, converted

    def doFindNextTextFileUsableLine(self, theLines, idxLines): # keep copying - this is in addition to OnFileOpen
        """finds next TxtFile Usable Line"""
        foundit = -1
        good = False
        for idx in range(idxLines+1, len(theLines)):
            good, theNum = self.fromMarksWeirdNumbers(theLines[idx])
            if good != True:
                continue
            else:
                foundit = idx
                break
        return foundit

    def doLoadTextFile(self, fname): # keep copying - this is in addition to OnFileOpen
        """Opens text file, makes a backup *.001.txt"""
        self.m_txtFileIdx = -1
        self.m_txtFileLines = []
        retn = "OK"
        absName = "UNKNOWN"
        fp = None
        try:
            absName = os.path.abspath(fname)
            fp = open(absName, 'rt')
            while True:
                line = fp.readline()
                if len(line) <= 0:
                    break
                self.m_txtFileLines.append(line.strip())
            fp.close()
        except: # I know, too broad, but this is just for me
            if fp:
                fp.close()
            self.m_txtFileLines = []
        if len(self.m_txtFileLines) < 1:
            self.m_txtFileLines = []
            return "ERROR: cannot read %s" % fname
        if ("#" != self.m_txtFileLines[-1][0]) or (-1 == self.m_txtFileLines[-1].find("END OF FILE")):
            self.m_txtFileLines = []
            retn = "ERROR: file %s last line is not # ... END OF FILE" % fname
        self.m_txtFilePath = absName
        self.m_txtFileIdx = self.doFindNextTextFileUsableLine(self.m_txtFileLines, self.m_txtFileIdx)
        if self.m_txtFileIdx < 0:
            self.m_txtFileLines = []
            retn = "ERROR: file %s has no non-comment lines" % fname
        return retn


    def onFileSave( self, event ):
        event.Skip()            # need to write this one

    def onFileSaveAs( self, event ):
        event.Skip()            # need to write this one


    def OnFileQuit( self, event ):
        dlgRslt = wx.MessageBox("Are you sure? This will lose changes", "Are you sure?", wx.YES|wx.NO|wx.CANCEL|wx.ICON_EXCLAMATION|wx.CENTRE)
        if wx.NO == dlgRslt:
            event.Skip()
        else:
            self.Close()

    def OnFileExit( self, event ):
        event.Skip()            # need to write this one

    def onHelpAbout( self, event ):
        event.Skip()            # need to write this one

    def onTimerMedia( self, event ):
        # the length is -1 if nothing is loaded
        # after the load it is length None
        # some time after loading it goes to 0
        # some time after that it goes to number of millisecs (ex: 9637)
        # then some time later it rounds off to the seconds (ex: 9000); I don't know why
        # we want to keep the 9637 from the example above
        tmp = self.m_mediactrl.Length()
        if ((None == self.m_mediaLength) or (self.m_mediaLength <= 0)) and ((tmp > 0) and (self.m_mediaLength != tmp)):
            self.m_mediaLength = self.m_mediactrl.Length()
            # print("timer length %s" % self.m_mediaLength)
            if self.m_mediactrl.Play():
                # print("timer: Play worked")
                self.m_mediactrl.SetInitialSize()
                self.GetSizer().Layout()
                sleep(0.05) # sleep seconds
                self.m_mediactrl.Pause()


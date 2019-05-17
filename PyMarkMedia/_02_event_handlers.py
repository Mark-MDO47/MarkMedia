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
        possibleIdx = m_txtFileIdx = self.doFindDirecTextFileUsableLine(-1)
        if possibleIdx >= 0:
            self.m_txtFileIdx = possibleIdx
            ignore = self.doLoadupNumMediaFile( mediaWeirdNum = self.m_txtFileLines[self.m_txtFileIdx][:5], statusText= self.m_txtFileLines[self.m_txtFileIdx] )

    def onBtnPrev( self, event ):
        ignore, mediaDecNum = self.fromMarksWeirdNumbers(self.m_mediaCurrentWeirdNum)
        # print("fromMarksWeirdNumbers m_mediaCurrentWeirdNum: |%s| ignore: |%s| mediaDecNum: |%s|" % (self.m_mediaCurrentWeirdNum, ignore, mediaDecNum))
        if mediaDecNum > 1:
            mediaDecNum -= 1
        # print("decrement m_mediaCurrentWeirdNum: |%s| ignore: |%s| mediaDecNum: |%s|" % (self.m_mediaCurrentWeirdNum, ignore, mediaDecNum))
        ignore, weirdMediaNum = self.toMarksWeirdNumbers(mediaDecNum)
        # print("toMarksWeirdNumbers weirdMediaNum: |%s| ignore: |%s| mediaDecNum: |%s|" % (weirdMediaNum, ignore, mediaDecNum))
        self.doLoadupNumMediaFile( mediaWeirdNum = weirdMediaNum, statusText = "non-text-file %d" % mediaDecNum )


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
        ignore, mediaDecNum = self.fromMarksWeirdNumbers(self.m_mediaCurrentWeirdNum)
        # FIXME Pix vs Movies
        if mediaDecNum < self.m_infoFile["THE_MAX_MVINUM"]:
            mediaDecNum += 1
            ignore, weirdMediaNum = self.toMarksWeirdNumbers(mediaDecNum)
            self.doLoadupNumMediaFile( mediaWeirdNum = weirdMediaNum, statusText = "non-text-file %d" % mediaDecNum )


    def onBtnNextFile( self, event ):
        possibleIdx = m_txtFileIdx = self.doFindDirecTextFileUsableLine(+1)
        if possibleIdx >= 0:
            self.m_txtFileIdx = possibleIdx
            ignore = self.doLoadupNumMediaFile( mediaWeirdNum = self.m_txtFileLines[self.m_txtFileIdx][:5], statusText= self.m_txtFileLines[self.m_txtFileIdx] )

    def onBtnEnterVidNum( self, event ):
        DlgEnterVidNum(self).ShowModal()


    def onBtnLouder( self, event ):
        # increase volume by 5 percent; makes assumption that current volume is valid
                self.m_mediactrl.SetVolume(min(1.0, self.m_mediactrl.GetVolume()+0.05))


    def onBtnSofter( self, event ):
        # decrease volume by 5 percent; makes assumption that current volume is valid
                self.m_mediactrl.SetVolume(max(0.0, self.m_mediactrl.GetVolume()-0.05))


    def onListBoxDClickVidComments( self, event ):
        event.Skip()            # need to write this one


    def onListBoxDClickVidComments( self, event ):
        event.Skip()            # need to write this one

    def OnFileOpen( self, event ):
        # FIXME Pix vs Movies
        dlg = wx.FileDialog(self, message="Choose a NewMovie.txt file in complete Olson www folder", defaultDir=r'X:\OlsonMedia\DigitalCamera\www_html', defaultFile="*.txt", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            loadOK = True
            pathTxt = os.path.abspath(dlg.GetPath())
            pathRootDir = os.path.dirname(pathTxt)
            pathPictureInfo = os.path.join(pathRootDir, "OlsonPictureInfo.php")
            if False == os.path.exists(pathPictureInfo):
                wx.MessageBox("Unable to load required Info file %s: file does not exist" % pathPictureInfo, "ERROR", wx.ICON_ERROR | wx.OK)
                loadOK = False
            if loadOK:
                retn = self.doLoadInfoFile(pathPictureInfo)
                if "OK" != retn:
                    wx.MessageBox("Unable to load %s: %s" % (pathTxt, retn), "ERROR", wx.ICON_ERROR | wx.OK)
                    loadOK = False
            if loadOK:
                retn = self.doLoadTextFile(pathTxt)
                if "OK" != retn:
                    wx.MessageBox("Unable to load %s: %s" % (pathTxt, retn), "ERROR", wx.ICON_ERROR | wx.OK)
                    loadOK = False
            if loadOK:
                loadOK = self.doLoadupNumMediaFile( mediaWeirdNum = self.m_txtFileLines[self.m_txtFileIdx][:5], statusText= self.m_txtFileLines[self.m_txtFileIdx] )

    def doGetTxtFileLines(self, fname): # keep copying - this is in addition to OnFileOpen
        """Opens text file and reads the lines"""
        retn = "OK"
        absName = "UNKNOWN"
        fp = None
        theLines = []
        try:
            absName = os.path.abspath(fname)
            fp = open(absName, 'rt')
            while True:
                line = fp.readline()
                if len(line) <= 0:
                    break
                theLines.append(line.strip())
            fp.close()
        except OSError as err:
            try:
                fp.close()
            except:
                pass
            retn = "Error: %s" % err
            theLines = []
        except: # I know, too broad, but this is just for me
            try:
                fp.close()
            except:
                pass
            retn = "Unexpected Error"
            theLines = []
        if ("OK" == retn) and (len(theLines) < 1):
            retn = "ERROR: %s has no lines" % fname
            theLines = []
        return retn, theLines

    def doLoadInfoFile(self, fname): # keep copying - this is in addition to OnFileOpen
        """gets last filenum for MVI and IMG"""
        # should contain lines that look like this:
        # define("THE_MAX_IMGNUM","45065");
        # define("THE_MAX_MVINUM","3441");
        self.m_infoFile = {}
        infoFile = {"THE_MAX_IMGNUM": -1, "THE_MAX_MVINUM": -1}
        retn, infoLines = self.doGetTxtFileLines( fname )
        if "OK" != retn:
            return retn
        for line in infoLines:
            for key in infoFile.keys():
                if -1 != line.find(key):
                    lsplit = line.split('"')
                    try:
                        infoFile[key] = int(lsplit[-2])
                    except:
                        infoFile[key] = -1
                        retn = "ERROR: file %s not in infoFile format" % fname
        if ("OK" == retn) and (infoFile["THE_MAX_IMGNUM"] > 0) and (infoFile["THE_MAX_MVINUM"] > 0):
            # infoFile is good; store it
            self.m_infoFile = infoFile
            # let's just see if the info in infoFile is up to date, shall we?
            # FIXME Pix vs Movies
            ignore, mediaWeirdNum = self.toMarksWeirdNumbers(infoFile["THE_MAX_MVINUM"])
            mediaDirList = sorted(os.listdir((os.path.join(os.path.dirname(fname), 'movies', mediaWeirdNum[:2]))))
            mp4List = []
            for mDirFile in mediaDirList:
                if mDirFile.endswith(".MP4"):
                   mp4List.append(mDirFile)
            # FIXME Pix vs Movies
            expectedLastFile = "MVI"+mediaWeirdNum+".MP4"
            found = -1
            if expectedLastFile in mp4List:
                found = mp4List.index(expectedLastFile)
            if found < 0:
                # FIXME Pix vs Movies
                wx.MessageBox("Warning: directory structure does not include \"%s\" media directory files per infoFile %s" % ("movie", fname), "ERROR", wx.ICON_ERROR | wx.OK)
            elif (found + 1) != len(mp4List):
                ignore, decNum =  self.fromMarksWeirdNumbers(mp4List[-1][3:3+5])
                wx.MessageBox("Warning: \"%s\" media directory files per infoFile %s\nExpected last file was %s (%d)\nActual last file in directory was %s (%d)" % ("movie", fname, expectedLastFile, infoFile["THE_MAX_MVINUM"], mp4List[-1], decNum), "ERROR", wx.ICON_ERROR | wx.OK)
        return retn

    def doLoadTextFile(self, fname): # keep copying - this is in addition to OnFileOpen
        """Opens text file"""
        self.m_txtFileIdx = -1
        retn, self.m_txtFileLines = self.doGetTxtFileLines( fname )
        if "OK" != retn:
            self.m_txtFileLines = []
            return retn
        if ("#" != self.m_txtFileLines[-1][0]) or (-1 == self.m_txtFileLines[-1].find("END OF FILE")):
            self.m_txtFileLines = []
            return "ERROR: file %s last line is not # ... END OF FILE" % fname
        self.m_txtFilePath = os.path.abspath(fname)
        self.rootDir = os.path.dirname(self.m_txtFilePath)
        for line in self.m_txtFileLines:
            self.doAddListCtrlLine(line, self.m_listCtrlVidComments.GetItemCount())
        self.m_txtFileIdx = len(self.m_txtFileLines)-1
        self.m_txtFileIdx = self.doFindDirecTextFileUsableLine(-1)
        if self.m_txtFileIdx < 0:
            self.m_txtFileLines = []
            retn = "ERROR: file %s has no non-comment lines" % fname
        self.m_listCtrlVidComments.EnsureVisible(self.m_listCtrlVidComments.GetItemCount())
        return retn

    def doAddListCtrlLine( self, line = "", posn = 0 ): # keep copying - this is in addition to OnFileOpen
        # adds line to list control before specified position
        mediaFlag, ignore = self.fromMarksWeirdNumbers(line, quiet=True)
        if mediaFlag:
            # media line
            self.m_listCtrlVidComments.InsertItem(posn, line[:5])
            self.m_listCtrlVidComments.SetItem(posn, 1, line[5:].strip())
        else:
            # comment
            self.m_listCtrlVidComments.InsertItem(posn, " ")
            self.m_listCtrlVidComments.SetItem(posn, 1, line)

    def doLoadupNumMediaFile( self, mediaWeirdNum = "_0001", statusText = "Status: ..." ): # keep copying - this is in addition to OnFileOpen
        loadOK = True
        prevStatus = self.m_staticTextStatus.GetLabel()
        self.m_staticTextStatus.SetLabel("Status: loading %s ..." % mediaWeirdNum)
        # FIXME Pix vs Movies
        self.m_mediaLength = None
        mediaFile = os.path.join(self.rootDir, 'movies', mediaWeirdNum[:2], "MVI"+mediaWeirdNum+".MP4")
        if False == os.path.exists(mediaFile):
            txt = "Media file %s does not exist" % mediaFile
            self.m_staticTextStatus.SetLabel("Status: %s" % txt)
            wx.MessageBox(txt, "ERROR", wx.ICON_ERROR | wx.OK)
            loadOK = False
        else:
            if not self.m_mediactrl.Load(mediaFile):
                txt = "Unable to load media file %s: Unsupported format?" % mediaFile
                self.m_staticTextStatus.SetLabel("Status: %s" % txt)
                wx.MessageBox(txt, "ERROR", wx.ICON_ERROR | wx.OK)
                loadOK = False
            else:
                # print(" m_bLoaded=%d" % self.m_mediactrl.m_bLoaded) # not in wxPython
                self.m_staticTextStatus.SetLabel("Status: %s (%s)" % (statusText, self.m_mediaMtime))
                self.m_mediactrl.SetInitialSize()
                self.GetSizer().Layout()
                self.m_mediaMtime = time.ctime(os.path.getmtime(mediaFile))
                self.m_mediaCurrentWeirdNum = mediaWeirdNum
        self.m_mediaStartStopDisplay = loadOK
        if not loadOK:
            self.m_staticTextStatus.SetLabel(prevStatus)
        return loadOK

    def fromMarksWeirdNumbers(self, theNumberText, quiet = False): # keep copying - this is in addition to OnFileOpen
        # for historical reasons numbering is
        # leftmost digit: _01...9A...Z
        # next     digit: 01...9A...Z
        # next 3  digits: 01...9
        # (example: _0001 to _Z999 to 00000 to 99999 to 9A000 to 9Z999 to A0000 to ZZ999)

        if type(theNumberText) != type('_A123'):
            if False == quiet:
                dlgRslt = wx.MessageBox("ERROR: cannot convert input type %s - inside fromMarksWeirdNumbers()" % (type(theNumberText)), "Bad Inputs", wx.ICON_EXCLAMATION|wx.CENTRE)
            good = False
        elif len(theNumberText) < 5:
            if False == quiet:
                dlgRslt = wx.MessageBox("ERROR: string |%s| is too short; must be >= 5 - inside fromMarksWeirdNumbers()" % (theNumberText), "Bad Inputs", wx.ICON_EXCLAMATION|wx.CENTRE)
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

    def toMarksWeirdNumbers(self, theNumber, quiet = False): # keep copying - this is in addition to OnFileOpen
        # see fromMarksWeirdNumbers() for description of strange numbering scheme
        good = True
        converted = "_0000" # zero
        if type(theNumber) == type("123"): # if it is a string
            theNumber = int(theNumber)
        if type(theNumber) != type(123):
            if False == quiet:
                dlgRslt = wx.MessageBox("ERROR: cannot convert %s type %s inside toMarksWeirdNumbers()" % (str(theNumber), type(theNumber)), "Bad Inputs", wx.ICON_EXCLAMATION|wx.CENTRE)
            good = False
        else:
            # FIXME let's cheat a little; we know some things about this...
            last3 = "%03d" % (theNumber % 1000)
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

    def doFindDirecTextFileUsableLine(self, direc): # keep copying - this is in addition to OnFileOpen
        """finds m_txtFileLines Usable Line idx in direction direc or -1"""
        foundit = -1
        good = False
        idx = self.m_txtFileIdx
        while True:
            idx += direc
            if (idx < 0) or (idx >= len(self.m_txtFileLines)):
                break
            good, ignore = self.fromMarksWeirdNumbers(self.m_txtFileLines[idx])
            if good != True:
                continue
            else:
                foundit = idx
                break
        return foundit

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
        if self.m_mediaStartStopDisplay: # set True to load to a bit past the start
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
                    self.m_mediaStartStopDisplay = False


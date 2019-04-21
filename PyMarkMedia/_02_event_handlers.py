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
            self.m_mediaLoad = True
            self.m_mediaLength = self.m_mediactrl.SetInitialSize()
            print("Open length %s" % self.m_mediaLength)
            # print(" m_bLoaded=%d" % self.m_mediactrl.m_bLoaded) # not in wxPython
            # how to get the video to show ???
            # if self.m_mediactrl.Play():
                # self.m_mediactrl.SetInitialSize()
                # self.GetSizer().Layout()
                # sleep(10.0) # sleep seconds
                # self.m_mediactrl.Pause()

    def DoLoadFile(self, path): # keep copying - this is in addition to OnFileOpen
        # self.m_buttonPlay.Disable() ### FIXME
        if not self.m_mediactrl.Load(path):
            wx.MessageBox("Unable to load %s: Unsupported format?" % path, "ERROR", wx.ICON_ERROR | wx.OK)
        else:
            # print(" m_bLoaded=%d" % self.m_mediactrl.m_bLoaded) # not in wxPython
            self.m_mediactrl.SetInitialSize()
            self.GetSizer().Layout()


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
            print("timer length %s" % self.m_mediaLength)
            if self.m_mediactrl.Play():
                print("timer: Play worked")
                self.m_mediactrl.SetInitialSize()
                self.GetSizer().Layout()
                sleep(0.05) # sleep seconds
                self.m_mediactrl.Pause()

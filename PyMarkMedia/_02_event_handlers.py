	def onBtnPrev10( self, event ):
		event.Skip()

	def onBtnPrev( self, event ):
		event.Skip()

	def onBtnPlay( self, event ):
		if not self.m_mediactrl.Play():
			wx.MessageBox("Unable to Play media : Unsupported format?",
				"ERROR", wx.ICON_ERROR | wx.OK)
		else:
			self.m_mediactrl.SetInitialSize()
			self.GetSizer().Layout()

	def onBtnStop( self, event ):
		self.m_mediactrl.Stop()

	def onBtnNext( self, event ):
		event.Skip()

	def onBtnNext10( self, event ):
		event.Skip()

	def onBtnEnterVidNum( self, event ):
		DlgEnterVidNum(self).ShowModal()

	def onBtnLouder( self, event ):
		event.Skip()

	def onBtnSofter( self, event ):
		event.Skip()

	def onLBoxVidComments( self, event ):
		event.Skip()

	def onListBoxDClickVidComments( self, event ):
		event.Skip()

	def OnFileOpen( self, event ):
		dlg = wx.FileDialog(self, message="Choose a media file", defaultDir=os.getcwd(), defaultFile="", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			self.DoLoadFile(path)

	def DoLoadFile(self, path): # keep copying - this is in addition to OnFileOpen
		# self.m_buttonPlay.Disable() ### FIXME
		if not self.m_mediactrl.Load(path):
			wx.MessageBox("Unable to load %s: Unsupported format?" % path, "ERROR", wx.ICON_ERROR | wx.OK)
		else:
			self.m_mediactrl.SetInitialSize()
			self.GetSizer().Layout()

	def onFileSave( self, event ):
		event.Skip()

	def onFileSaveAs( self, event ):
		event.Skip()

	def onHelpAbout( self, event ):
		event.Skip()

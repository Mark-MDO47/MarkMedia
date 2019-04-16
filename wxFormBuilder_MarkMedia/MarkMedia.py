# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1245,1193 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerFrame = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetToolTip( u"Video is displayed here" )

		bSizerPanel = wx.BoxSizer( wx.VERTICAL )

		self.m_staticTextStatus = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Status: ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextStatus.Wrap( -1 )

		self.m_staticTextStatus.SetToolTip( u"Status is displayed here" )

		bSizerPanel.Add( self.m_staticTextStatus, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_notebookMediaCtrl = wx.Notebook( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebookMediaCtrl.SetMinSize( wx.Size( 800,800 ) )


		bSizerPanel.Add( self.m_notebookMediaCtrl, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		m_radioBox1Choices = [ u"Pix", u"Movies" ]
		self.m_radioBox1 = wx.RadioBox( self.m_panel1, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 2, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer3.Add( self.m_radioBox1, 0, wx.ALL, 5 )

		self.m_buttonPrev10 = wx.Button( self.m_panel1, wx.ID_ANY, u"|<<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonPrev10.SetToolTip( u"10 Previous" )

		bSizer3.Add( self.m_buttonPrev10, 0, wx.ALL, 5 )

		self.m_buttonPrev = wx.Button( self.m_panel1, wx.ID_ANY, u"|<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonPrev.SetToolTip( u"Previous" )

		bSizer3.Add( self.m_buttonPrev, 0, wx.ALL, 5 )

		self.m_buttonPlay = wx.Button( self.m_panel1, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonPlay.SetToolTip( u"Play" )

		bSizer3.Add( self.m_buttonPlay, 0, wx.ALL, 5 )

		self.m_buttonStop = wx.Button( self.m_panel1, wx.ID_ANY, u">][<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonStop.SetToolTip( u"Stop" )

		bSizer3.Add( self.m_buttonStop, 0, wx.ALL, 5 )

		self.m_buttonNext = wx.Button( self.m_panel1, wx.ID_ANY, u">|", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonNext.SetToolTip( u"Next" )

		bSizer3.Add( self.m_buttonNext, 0, wx.ALL, 5 )

		self.m_buttonNext10 = wx.Button( self.m_panel1, wx.ID_ANY, u">>>|", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonNext10.SetToolTip( u"10 Next" )

		bSizer3.Add( self.m_buttonNext10, 0, wx.ALL, 5 )

		self.m_buttonEnterVidNum = wx.Button( self.m_panel1, wx.ID_ANY, u"Enter...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonEnterVidNum.SetToolTip( u"Enter video number" )

		bSizer3.Add( self.m_buttonEnterVidNum, 0, wx.ALL, 5 )

		self.m_buttonLouder = wx.Button( self.m_panel1, wx.ID_ANY, u"^^^", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonLouder.SetToolTip( u"Louder" )

		bSizer3.Add( self.m_buttonLouder, 0, wx.ALL, 5 )

		self.m_buttonSofter = wx.Button( self.m_panel1, wx.ID_ANY, u"vvv", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSofter.SetToolTip( u"Softer" )

		bSizer3.Add( self.m_buttonSofter, 0, wx.ALL, 5 )


		bSizerPanel.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl1.SetToolTip( u"Enter/Edit Comment" )

		bSizerPanel.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		m_listBoxVidCommentsChoices = []
		self.m_listBoxVidComments = wx.ListBox( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxVidCommentsChoices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE )
		self.m_listBoxVidComments.SetToolTip( u"List of existing Video txt comments" )
		self.m_listBoxVidComments.SetMinSize( wx.Size( -1,300 ) )

		bSizerPanel.Add( self.m_listBoxVidComments, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizerPanel )
		self.m_panel1.Layout()
		bSizerPanel.Fit( self.m_panel1 )
		bSizerFrame.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizerFrame )
		self.Layout()
		self.m_menubarMainFrame = wx.MenuBar( 0 )
		self.m_menuFile = wx.Menu()
		self.m_menuItemFileOpen = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"Open Video txt...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuFile.Append( self.m_menuItemFileOpen )

		self.m_menuItemFileSave = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"Save Video txt...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuFile.Append( self.m_menuItemFileSave )

		self.m_menuItemFileSaveAs = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"Save As Video txt...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuFile.Append( self.m_menuItemFileSaveAs )

		self.m_menubarMainFrame.Append( self.m_menuFile, u"File" )

		self.m_menuHelp = wx.Menu()
		self.m_menuItemHelpAbout = wx.MenuItem( self.m_menuHelp, wx.ID_ANY, u"About...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuHelp.Append( self.m_menuItemHelpAbout )

		self.m_menubarMainFrame.Append( self.m_menuHelp, u"Help" )

		self.SetMenuBar( self.m_menubarMainFrame )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonPrev10.Bind( wx.EVT_BUTTON, self.onBtnPrev10 )
		self.m_buttonPrev.Bind( wx.EVT_BUTTON, self.onBtnPrev )
		self.m_buttonPlay.Bind( wx.EVT_BUTTON, self.onBtnPlay )
		self.m_buttonStop.Bind( wx.EVT_BUTTON, self.onBtnStop )
		self.m_buttonNext.Bind( wx.EVT_BUTTON, self.onBtnNext )
		self.m_buttonNext10.Bind( wx.EVT_BUTTON, self.onBtnNext10 )
		self.m_buttonEnterVidNum.Bind( wx.EVT_BUTTON, self.onBtnEnterVidNum )
		self.m_buttonLouder.Bind( wx.EVT_BUTTON, self.onBtnLouder )
		self.m_buttonSofter.Bind( wx.EVT_BUTTON, self.onBtnSofter )
		self.m_listBoxVidComments.Bind( wx.EVT_LISTBOX, self.onLBoxVidComments )
		self.m_listBoxVidComments.Bind( wx.EVT_LISTBOX_DCLICK, self.onListBoxDClickVidComments )
		self.Bind( wx.EVT_MENU, self.OnFileOpen, id = self.m_menuItemFileOpen.GetId() )
		self.Bind( wx.EVT_MENU, self.onFileSave, id = self.m_menuItemFileSave.GetId() )
		self.Bind( wx.EVT_MENU, self.onFileSaveAs, id = self.m_menuItemFileSaveAs.GetId() )
		self.Bind( wx.EVT_MENU, self.onHelpAbout, id = self.m_menuItemHelpAbout.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onBtnPrev10( self, event ):
		event.Skip()

	def onBtnPrev( self, event ):
		event.Skip()

	def onBtnPlay( self, event ):
		event.Skip()

	def onBtnStop( self, event ):
		event.Skip()

	def onBtnNext( self, event ):
		event.Skip()

	def onBtnNext10( self, event ):
		event.Skip()

	def onBtnEnterVidNum( self, event ):
		event.Skip()

	def onBtnLouder( self, event ):
		event.Skip()

	def onBtnSofter( self, event ):
		event.Skip()

	def onLBoxVidComments( self, event ):
		event.Skip()

	def onListBoxDClickVidComments( self, event ):
		event.Skip()

	def OnFileOpen( self, event ):
		event.Skip()

	def onFileSave( self, event ):
		event.Skip()

	def onFileSaveAs( self, event ):
		event.Skip()

	def onHelpAbout( self, event ):
		event.Skip()



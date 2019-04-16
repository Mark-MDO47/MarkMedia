# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class DlgEnterVidNum
###########################################################################

class DlgEnterVidNum ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 474,187 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticTextDlgEnterVidNum = wx.StaticText( self, wx.ID_ANY, _(u"Enter last 5 digits below. Example:  for IMG_P085 enter _P085, for MVI0C123 enter 0C123"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticTextDlgEnterVidNum.Wrap( -1 )

		bSizer4.Add( self.m_staticTextDlgEnterVidNum, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticTextDlgEnterVidNumStatus = wx.StaticText( self, wx.ID_ANY, _(u"Status: waiting for entry..."), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticTextDlgEnterVidNumStatus.Wrap( -1 )

		bSizer4.Add( self.m_staticTextDlgEnterVidNumStatus, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Apply )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer4.Add( m_sdbSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer1Apply.Bind( wx.EVT_BUTTON, self.onDlgBtnEnterVidNumApply )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.onDlgBtnEnterVidNumCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onDlgBtnEnterVidNumApply( self, event ):
		event.Skip()

	def onDlgBtnEnterVidNumCancel( self, event ):
		event.Skip()



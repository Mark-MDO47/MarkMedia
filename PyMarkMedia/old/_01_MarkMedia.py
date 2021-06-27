# -*- coding: utf-8 -*-

import sys
import os
import time
from time import sleep

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
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



###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
    def __init__( self, parent, absRunPath = "" ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1245,1193 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        # inserted by aftercopyfilefrom to be copied after "wx.Frame.__init__"
        self.m_absRunPath = absRunPath # absolute path we were run from
        self.m_txtFilePath = "UNKNOWN" # absolute path to open text file
        self.m_txtFileLines = []       # lines for open text file, stripped
        self.m_txtFileIdx = -1         # which line for open text file or -1
        self.m_mediaLength = None # the length of media file; appears to be in milliseconds
        self.m_mediaLoad = False  # True when media load done until timer processes it
        self.m_mediaStartStopDisplay = False # yet another media load flag
        self.m_mediaCurrentWeirdNum = "_0001"
        self.m_mediaMtime = "" # time.ctime(os.path.getmtime(<<thepath>>))
        self.m_infoFile = {}   # filled with max nums, example {'THE_MAX_IMGNUM': 45065, 'THE_MAX_MVINUM': 3441}
        self.m_listCtrlInfo = {} # [validWeirdNum] = {"line": -1} , others TBD
        self.m_listCtrlSlctd = {"prev": -1, "curr": -1}
        self.m_textCtrlEntry_unchanged = ""
        self.m_textCtrlEntry_edited = ""
        
        self.SetIcon(wx.Icon(os.path.join(self.m_absRunPath,"MadScience_256.ico"))) # Mark: set icon

        # for historical reasons numbering is
        #   leftmost digit: _01...9A...Z
        #   next     digit: 01...9A...Z
        #   next 3  digits: 01...9
        #   (example: _0001 to _Z999 to 00000 to 99999 to 9A000 to 9Z999 to A0000 to ZZ999)
        self.MarksWeirdDigits = [ "_0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "0123456789",
            "0123456789",
            "0123456789"
        ]

        bSizerFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel1.SetToolTip( u"Video is displayed here" )

        bSizerPanel = wx.BoxSizer( wx.VERTICAL )

        self.m_staticTextStatus = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Status: ...", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextStatus.Wrap( -1 )

        self.m_staticTextStatus.SetToolTip( u"Status is displayed here" )

        bSizerPanel.Add( self.m_staticTextStatus, 0, wx.ALL|wx.EXPAND, 5 )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_buttonPrevfile = wx.Button( self.m_panel1, wx.ID_ANY, u"|<textfile", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonPrevfile.SetToolTip( u"Previous in text file" )

        bSizer3.Add( self.m_buttonPrevfile, 0, wx.ALL, 5 )

        self.m_buttonPrev = wx.Button( self.m_panel1, wx.ID_ANY, u"|<", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonPrev.SetToolTip( u"Previous media file" )

        bSizer3.Add( self.m_buttonPrev, 0, wx.ALL, 5 )

        self.m_buttonPlay = wx.Button( self.m_panel1, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonPlay.SetToolTip( u"Play" )

        bSizer3.Add( self.m_buttonPlay, 0, wx.ALL, 5 )

        self.m_buttonPause = wx.Button( self.m_panel1, wx.ID_ANY, u">][<", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonPause.SetToolTip( u"Pause" )

        bSizer3.Add( self.m_buttonPause, 0, wx.ALL, 5 )

        self.m_buttonNext = wx.Button( self.m_panel1, wx.ID_ANY, u">|", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonNext.SetToolTip( u"Next media file" )

        bSizer3.Add( self.m_buttonNext, 0, wx.ALL, 5 )

        self.m_buttonNextFile = wx.Button( self.m_panel1, wx.ID_ANY, u"textfile>|", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonNextFile.SetToolTip( u"Next in text file" )

        bSizer3.Add( self.m_buttonNextFile, 0, wx.ALL, 5 )

        self.m_buttonEnterVidNum = wx.Button( self.m_panel1, wx.ID_ANY, u"Enter #...", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonEnterVidNum.SetToolTip( u"Enter media number" )

        bSizer3.Add( self.m_buttonEnterVidNum, 0, wx.ALL, 5 )

        self.m_buttonLouder = wx.Button( self.m_panel1, wx.ID_ANY, u"Louder", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonLouder.SetToolTip( u"Louder" )

        bSizer3.Add( self.m_buttonLouder, 0, wx.ALL, 5 )

        self.m_buttonSofter = wx.Button( self.m_panel1, wx.ID_ANY, u"Softer", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonSofter.SetToolTip( u"Softer" )

        bSizer3.Add( self.m_buttonSofter, 0, wx.ALL, 5 )


        bSizerPanel.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_textCtrlEntry = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_NOHIDESEL|wx.TE_NO_VSCROLL|wx.TE_PROCESS_ENTER )
        self.m_textCtrlEntry.SetToolTip( u"Enter/Edit Comment" )

        bSizerPanel.Add( self.m_textCtrlEntry, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_listCtrlVidComments = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_REPORT|wx.BORDER_SUNKEN )
        self.m_listCtrlVidComments.SetToolTip( u"List of existing Video txt comments" )
        self.m_listCtrlVidComments.SetMinSize( wx.Size( -1,300 ) )
# start copying here
        self.m_listCtrlVidComments.InsertColumn(0, 'MagicNum')
        self.m_listCtrlVidComments.InsertColumn(1, 'Comment')
        self.m_listCtrlVidComments.SetColumnWidth(0, 50)
        self.m_listCtrlVidComments.SetColumnWidth(1, 1500)


        bSizerPanel.Add( self.m_listCtrlVidComments, 0, wx.ALL|wx.EXPAND, 5 )


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

        self.m_menuItemQuit = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"Quit without save...", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuFile.Append( self.m_menuItemQuit )

        self.m_menuItemeExit = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"Exit and save", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuFile.Append( self.m_menuItemeExit )

        self.m_menubarMainFrame.Append( self.m_menuFile, u"File" )

        self.m_menuHelp = wx.Menu()
        self.m_menuItemHelpAbout = wx.MenuItem( self.m_menuHelp, wx.ID_ANY, u"About...", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuHelp.Append( self.m_menuItemHelpAbout )

        self.m_menubarMainFrame.Append( self.m_menuHelp, u"Help" )

        self.SetMenuBar( self.m_menubarMainFrame )

        self.m_timerMedia = wx.Timer()
        self.m_timerMedia.SetOwner( self, wx.ID_ANY )
        self.m_timerMedia.Start( 125 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.m_buttonPrevfile.Bind( wx.EVT_BUTTON, self.onBtnPrevFile )
        self.m_buttonPrev.Bind( wx.EVT_BUTTON, self.onBtnPrev )
        self.m_buttonPlay.Bind( wx.EVT_BUTTON, self.onBtnPlay )
        self.m_buttonPause.Bind( wx.EVT_BUTTON, self.onBtnPause )
        self.m_buttonNext.Bind( wx.EVT_BUTTON, self.onBtnNext )
        self.m_buttonNextFile.Bind( wx.EVT_BUTTON, self.onBtnNextFile )
        self.m_buttonEnterVidNum.Bind( wx.EVT_BUTTON, self.onBtnEnterVidNum )
        self.m_buttonLouder.Bind( wx.EVT_BUTTON, self.onBtnLouder )
        self.m_buttonSofter.Bind( wx.EVT_BUTTON, self.onBtnSofter )
        self.m_textCtrlEntry.Bind( wx.EVT_TEXT_ENTER, self.onTextCtrlEntry )
        self.m_listCtrlVidComments.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.onListCtrlActivated )
        self.Bind( wx.EVT_MENU, self.OnFileOpen, id = self.m_menuItemFileOpen.GetId() )
        self.Bind( wx.EVT_MENU, self.onFileSave, id = self.m_menuItemFileSave.GetId() )
        self.Bind( wx.EVT_MENU, self.onFileSaveAs, id = self.m_menuItemFileSaveAs.GetId() )
        self.Bind( wx.EVT_MENU, self.OnFileQuit, id = self.m_menuItemQuit.GetId() )
        self.Bind( wx.EVT_MENU, self.OnFileExit, id = self.m_menuItemeExit.GetId() )
        self.Bind( wx.EVT_MENU, self.onHelpAbout, id = self.m_menuItemHelpAbout.GetId() )
        self.Bind( wx.EVT_TIMER, self.onTimerMedia, id=wx.ID_ANY )

    def __del__( self ):
        del self.m_mediactrl
        pass


    # Virtual event handlers, overide them in your derived class
    def onBtnPrevFile( self, event ):
        event.Skip()

    def onBtnPrev( self, event ):
        event.Skip()

    def onBtnPlay( self, event ):
        event.Skip()

    def onBtnPause( self, event ):
        event.Skip()

    def onBtnNext( self, event ):
        event.Skip()

    def onBtnNextFile( self, event ):
        event.Skip()

    def onBtnEnterVidNum( self, event ):
        event.Skip()

    def onBtnLouder( self, event ):
        event.Skip()

    def onBtnSofter( self, event ):
        event.Skip()

    def onTextCtrlEntry( self, event ):
        event.Skip()

    def onListCtrlActivated( self, event ):
        event.Skip()

    def OnFileOpen( self, event ):
        event.Skip()

    def onFileSave( self, event ):
        event.Skip()

    def onFileSaveAs( self, event ):
        event.Skip()

    def OnFileQuit( self, event ):
        event.Skip()

    def OnFileExit( self, event ):
        event.Skip()

    def onHelpAbout( self, event ):
        event.Skip()

    def onTimerMedia( self, event ):
        event.Skip()


###########################################################################
## MAIN PROGRAM
###########################################################################

app = wx.App()
frame = MainFrame(None, os.path.dirname(os.path.realpath(__file__))).Show()
app.MainLoop()

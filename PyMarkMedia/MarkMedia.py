# -*- coding: utf-8 -*-

import sys
import os
from time import sleep

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
###########################################################################

import wx
import wx.xrc
import wx.media
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

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1245,1193 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.m_mediaLength = None # the length of media file; appears to be in milliseconds
        self.m_mediaLoad = False # True when media load done until timer processes it

        self.SetIcon(wx.Icon("MadScience_256.ico")) # Mark: set icon


        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizerFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel1.SetToolTip( u"Video is displayed here" )

        bSizerPanel = wx.BoxSizer( wx.VERTICAL )

        self.m_staticTextStatus = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Status: ...", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextStatus.Wrap( -1 )

        self.m_staticTextStatus.SetToolTip( u"Status is displayed here" )

        bSizerPanel.Add( self.m_staticTextStatus, 0, wx.ALL|wx.EXPAND, 5 )
        self.m_mediactrl = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER, size=wx.Size( 800,800 ))
        bSizerPanel.Add( self.m_mediactrl, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.m_notebookMediaCtrl = wx.Notebook( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_notebookMediaCtrl.SetMinSize( wx.Size( 800,800 ) )


        bSizerPanel.Add( self.m_notebookMediaCtrl, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

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
        self.m_listBoxVidComments.Bind( wx.EVT_LISTBOX, self.onLBoxVidComments )
        self.m_listBoxVidComments.Bind( wx.EVT_LISTBOX_DCLICK, self.onListBoxDClickVidComments )
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
                print("timer: Play worked")
                self.m_mediactrl.SetInitialSize()
                self.GetSizer().Layout()
                sleep(0.05) # sleep seconds
                self.m_mediactrl.Pause()



###########################################################################
## MAIN PROGRAM
###########################################################################

app = wx.App()
frame = MainFrame(None).Show()
app.MainLoop()

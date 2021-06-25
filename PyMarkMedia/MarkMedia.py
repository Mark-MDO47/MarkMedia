# -*- coding: utf-8 -*-

###########################################################################
#
# Author: Mark Olson 2018
#
# This is to help me manage my personal photo and video collection.
# 
###########################################################################


# import sys
import os
import time
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
## some globals - need use by everyone
###########################################################################

# for historical reasons Weird numbering is
#   leftmost digit: _01...9A...Z re: [_0-9A-Z]
#   next     digit: 01...9A...Z  re: [0-9A-Z]
#   next 3  digits: 01...9       re: [0-9]
#   (example: _0001 to _Z999 to 00000 to 99999 to 9A000 to 9Z999 to A0000 to ZZ999)
MarksWeirdDigits = ["_0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                    "0123456789",
                    "0123456789",
                    "0123456789"
                   ]

def fromMarksWeirdNumbers(theNumberText, quiet=False):
    if not isinstance(theNumberText, type('_A123')):
        if quiet is False:
            ignore = wx.MessageBox(
                "ERROR: cannot convert input type %s - inside fromMarksWeirdNumbers()" % (type(theNumberText)),
                "Bad Inputs", wx.ICON_EXCLAMATION | wx.CENTRE)
    elif len(theNumberText) < 5:
        if quiet is False:
            ignore = wx.MessageBox(
                "ERROR: string |%s| is too short; must be >= 5 - inside fromMarksWeirdNumbers()" % theNumberText,
                "Bad Inputs", wx.ICON_EXCLAMATION | wx.CENTRE)
    theNumberText = theNumberText.upper()
    good = True
    converted = 0
    if len(theNumberText) < len(MarksWeirdDigits):
        good = False
        converted = -1
    if good:
        for idx in range(len(MarksWeirdDigits)):
            converted *= len(MarksWeirdDigits[idx])
            tmp = MarksWeirdDigits[idx].find(theNumberText[idx])
            if -1 != tmp:
                converted += tmp
            else:
                good = False
                converted = -1
                break
    return good, converted

def toMarksWeirdNumbers(theNumber, quiet=False):
    # see MarksWeirdDigits[] for description of strange numbering scheme
    good = True
    converted = "_0000"  # zero
    if isinstance(theNumber, type("123")):  # if it is a string
        theNumber = int(theNumber)
    if not isinstance(theNumber, type(123)): # if it is not a number
        if quiet is False:
            ignore = wx.MessageBox(
                "ERROR: cannot convert %s type %s inside toMarksWeirdNumbers()" % (str(theNumber), type(theNumber)),
                "Bad Inputs", wx.ICON_EXCLAMATION | wx.CENTRE)
        good = False
    else:
        # TODO FIXME let's cheat a little; we know some things about this...
        last3 = "%03d" % (theNumber % 1000)
        first2int = int(theNumber // 1000)
        firstint = int(first2int // len(MarksWeirdDigits[1]))
        secondint = first2int - firstint * len(MarksWeirdDigits[1])
        if firstint > len(MarksWeirdDigits[0]):
            theMax = ((len(MarksWeirdDigits[0]) - 1) * len(MarksWeirdDigits[1]) + (
                        len(MarksWeirdDigits[1]) - 1)) * 1000 + 999
            ignore = wx.MessageBox(
                "ERROR: cannot convert %d: larger than max %d inside toMarksWeirdNumbers()" % (theNumber, theMax),
                "Bad Inputs", wx.ICON_EXCLAMATION | wx.CENTRE)
            good = False
        else:
            converted = MarksWeirdDigits[0][firstint] + MarksWeirdDigits[1][secondint] + last3
    return good, converted


###########################################################################
# Class DlgEnterVidNum - retrieve hand-entered Weird media number
#   local non-control variables
#     self.l_returnNumberDec    - decimal number of media entered or else -1
#     self.l_returnNumberWeird  - weird number of media entered or else "UNKNOWN"
#   local control variables
#     self.m_sdbtn_Sizer1Apply     - to hold the "Apply" button
#     self.m_sdbtn_Sizer1Cancel    - to hold the "Cancel" button
#     self.m_staticTextDlgEnterVidNum       - static text telling how to enter video number
#     self.m_staticTextDlgEnterVidNumStatus - static text telling what dialog is doing or waiting for
#     self.m_textCtrlEnterNum      - text control that user types Weird number into
###########################################################################

class DlgEnterVidNum ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition,
                             size = wx.Size( 474,187 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.l_returnNumberWeird = "UNKNOWN"
        self.l_returnNumberDec = -1

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticTextDlgEnterVidNum =\
            wx.StaticText(self, wx.ID_ANY,
                          _(u"Enter last 5 digits below. Example:  for IMG_P085 enter _P085, for MVI0C123 enter 0C123"),
                          wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticTextDlgEnterVidNum.Wrap( -1 )

        bSizer4.Add( self.m_staticTextDlgEnterVidNum, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_textCtrlEnterNum = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, size=wx.DefaultSize, style = wx.TE_PROCESS_ENTER)
        bSizer4.Add( self.m_textCtrlEnterNum, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticTextDlgEnterVidNumStatus =\
            wx.StaticText( self, wx.ID_ANY, _(u"Status: waiting for entry..."),
                           wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticTextDlgEnterVidNumStatus.Wrap( -1 )

        bSizer4.Add( self.m_staticTextDlgEnterVidNumStatus, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        # m_sdbtn_ is standard dialog button
        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbtn_Sizer1Apply = wx.Button( self, wx.ID_APPLY )
        m_sdbSizer1.AddButton( self.m_sdbtn_Sizer1Apply )
        self.m_sdbtn_Sizer1Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer1.AddButton( self.m_sdbtn_Sizer1Cancel )
        m_sdbSizer1.Realize()

        bSizer4.Add( m_sdbSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_sdbtn_Sizer1Apply.Bind( wx.EVT_BUTTON, self.onDlgBtnEnterVidNumApply )
        self.m_sdbtn_Sizer1Cancel.Bind( wx.EVT_BUTTON, self.onDlgBtnEnterVidNumCancel )
        self.Bind(wx.EVT_TEXT_ENTER, self.onDlgBtnEnterVidNumApply)
    # end class DlgEnterVidNum().__init__()

    def __del__( self ):
        pass
    # end class DlgEnterVidNum().__del__()

    # Virtual event handlers
    def onDlgBtnEnterVidNumApply( self, event ):
        typedNumWeird = self.m_textCtrlEnterNum.GetValue()
        # see if this is a valid number; should be one of my weird numbers
        good, typedNumDec = fromMarksWeirdNumbers(typedNumWeird)
        if good:
            self.l_returnNumberWeird = typedNumWeird
            self.l_returnNumberDec = typedNumDec
            self.Destroy()
        else:
            message = wx.MessageDialog(self, _("%s is not a valid weird number" % typedNumWeird),
                                       _("ERROR"), wx.OK | wx.ICON_ERROR)
            message.ShowModal()
            message.Destroy()
    # end class DlgEnterVidNum().onDlgBtnEnterVidNumApply()

    def onDlgBtnEnterVidNumCancel( self, event ):
        self.l_returnNumberWeird = "UNKNOWN"
        self.Destroy()
    # end class DlgEnterVidNum().onDlgBtnEnterVidNumCancel()
    # end class DlgEnterVidNum()



###########################################################################
# Class MainFrame - main class
#   local non-control variables
#     self.l_absRunPath             - absolute path we were run from; used to find resources such as the icon
#     self.l_dbDirName              - path to directory for database (db) text file
#     self.l_dbFileName             - filename (no path) for database (db) text file
#     self.l_dbMediaDescripIdx      - if no db or no line select -1, else line number (starting @ 0) currently displayed
#     self.l_dbMediaDescripLines    - lines for open db text file, stripped
#     self.l_dbMediaDescripModified - will be True if db text file edits not yet saved to l_dbFileName
#     self.l_dbMediaDescripPath     - absolute path to the open db text file
#     self.l_infoMaxImgMvi          - maximum numbers for pix and mvi media in decimal
#     self.l_listCtrlInfo           - where display version of db text file is stored; not exact txt format
#     self.l_listCtrlSlctd          - prev and curr lines; TODO candidate for deletion, maybe use when editing
#     self.l_mediaCurrentWeirdNum   - mediaWeirdNum of currently displayed file
#     self.l_mediaLength            - self.m_mediactrl.Length() (millisec) of currently displayed video or else None
#     self.l_mediaMtime             - time.ctime(os.path.getmtime(mediaFile)) date/time file modified
#     self.l_mediaStartStopDisplay  - set True to load movie video to a bit past the start (otherwise blank)
#     self.l_rootDir                - absolute path to the root directory: has db text file and dirs for all media
#     self.l_textCtrlEntry_unchanged - copy of single db text file entry to compare to see if user changed it
#     self.l_useMdoMediaCtrls       - True to use my clunky controls; set false when ShowPlayerControls() works
#
#   local control variables
#     self.m_buttonEnterVidNum   - button to call DlgEnterVidNum() and manually enter video number
#     self.m_buttonLouder        - video control - louder
#     self.m_buttonPause         - video control - pause video play
#     self.m_buttonPlay          - video control - play video
#     self.m_buttonSofter        - video control - softer
#     self.m_buttonNextNum       - video select - move to next numerical mediafile
#     self.m_buttonPrevNum       - video select - move to previous numerical mediafile
#     self.m_buttonNextDbFile    - video select - move to next mediafile listed in media db text file
#     self.m_buttonPrevDbFile    - video select - move to previous mediafile listed in media db text file
#     self.m_listCtrlVidComments - list control to hold media db text file
#     self.m_mediactrl           - media control to play video
#     self.m_menubarMainFrame    - the "menu" bar
#     self.m_menuFile            - collection for "FILE" menu
#     self.m_menuItemFileOpen    - menu - open media db text file
#     self.m_menuItemFileSave    - menu - save media db text file using current name
#     self.m_menuItemFileSaveAs  - menu - save media db text file using new name
#     self.m_menuItemQuit        - menu - quit without save
#     self.m_menuItemExit        - menu - exit and save
#     self.m_menuHelp            - collection for "HELP" menu
#     self.m_menuItemHelpAbout   - menu - help/about
#     self.m_panel1              - video is displayed here
#     self.m_staticTextStatus    - info about video being displayed
#     self.m_textCtrlEntry       - enter/edit video comment here
#     self.m_timerMedia          - timer needed to move a few milliseconds into movie so not blank screen
#                                       see also self.l_mediaStartStopDisplay
#
#  to get list of l_ or m_
#    grep "self.l_.*[=]" MarkMedia.py | sed "s?self.l_?\nself.l_?g" | grep self.l_ | sed "s?[ ,\[\()].*??" | sort | uniq
#    grep "self.m_.*[=]" MarkMedia.py | sed "s?self.m_?\nself.m_?g" | grep self.m_ | sed "s?[ ,\[\()].*??" | sort | uniq
###########################################################################

class MainFrame ( wx.Frame ):
    def __init__( self, parent, absRunPath = "" ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition,
                            size = wx.Size( 1245,1193 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.l_absRunPath = absRunPath # absolute path we were run from
        self.l_dbMediaDescripPath = "UNKNOWN" # absolute path to open text file
        self.l_dbMediaDescripLines = []       # lines for open text file, stripped
        self.l_dbMediaDescripIdx = -1         # which line for open text file or -1
        self.l_dbMediaDescripModified = False # will be true when modifications are made
        self.l_mediaLength = None # the length of media file; appears to be in milliseconds
        self.l_mediaStartStopDisplay = False # yet another media load flag
        self.l_mediaCurrentWeirdNum = "_0001"
        self.l_mediaMtime = "" # time.ctime(os.path.getmtime(<<thepath>>))
        self.l_infoMaxImgMvi = {}   # filled with max nums, example {'THE_MAX_IMGNUM': 45065, 'THE_MAX_MVINUM': 3441}
        self.l_listCtrlInfo = {} # [validWeirdNum] = {"line": -1} , others TBD
        self.l_listCtrlSlctd = {"prev": "_0001", "curr": "_0001"}
        self.l_textCtrlEntry_unchanged = ""
        self.l_useMdoMediaCtrls = True # ShowPlayerControls does not seem to work
        self.l_dbFileName = ""
        self.l_dbDirName = ""
        self.l_rootDir = ""

        self.SetIcon(wx.Icon(os.path.join(self.l_absRunPath,"MadScience_256.ico"))) # Mark: set icon

        bSizerFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel1.SetToolTip( u"Video is displayed here" )

        bSizerPanel = wx.BoxSizer( wx.VERTICAL )

        self.m_staticTextStatus = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Status: ...",
                                                 wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextStatus.Wrap( -1 )

        self.m_staticTextStatus.SetToolTip( u"Status is displayed here" )

        bSizerPanel.Add( self.m_staticTextStatus, 0, wx.ALL|wx.EXPAND, 5 )
        self.m_mediactrl = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER, size=wx.Size( 800,800 ))
        # self.m_mediactrl = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER, size=wx.Size( 800,800 ), szBackend=wx.media.MEDIABACKEND_DIRECTSHOW)
        # self.m_mediactrl = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER, size=wx.Size( 800,800 ), szBackend=wx.media.MEDIABACKEND_WMP10)
        if not self.l_useMdoMediaCtrls:
            # Currently only implemented on the QuickTime and DirectShow backends. The function returns True on success
            # if not self.m_mediactrl.ShowPlayerControls(flags=wx.media.MEDIACTRLPLAYERCONTROLS_STEP):
            if not self.m_mediactrl.ShowPlayerControls(flags=wx.media.MEDIACTRLPLAYERCONTROLS_DEFAULT): # does not seem to work
                # it claims that it worked but there are no working controls
                print("ShowPlayerControls() failed")
        bSizerPanel.Add( self.m_mediactrl, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_buttonPrevDbFile = wx.Button(self.m_panel1, wx.ID_ANY, u"|<textfile", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_buttonPrevDbFile.SetToolTip( u"Previous in text file" )

        bSizer3.Add( self.m_buttonPrevDbFile, 0, wx.ALL, 5 )

        self.m_buttonPrevNum = wx.Button( self.m_panel1, wx.ID_ANY, u"|<", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonPrevNum.SetToolTip( u"Previous media file" )

        bSizer3.Add( self.m_buttonPrevNum, 0, wx.ALL, 5 )

        if self.l_useMdoMediaCtrls:
            self.m_buttonPlay = wx.Button( self.m_panel1, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
            self.m_buttonPlay.SetToolTip( u"Play" )

            bSizer3.Add( self.m_buttonPlay, 0, wx.ALL, 5 )

            self.m_buttonPause = wx.Button( self.m_panel1, wx.ID_ANY, u">][<", wx.DefaultPosition, wx.DefaultSize, 0 )
            self.m_buttonPause.SetToolTip( u"Pause" )

            bSizer3.Add( self.m_buttonPause, 0, wx.ALL, 5 )

        self.m_buttonNextNum = wx.Button( self.m_panel1, wx.ID_ANY, u">|", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonNextNum.SetToolTip( u"Next media file" )

        bSizer3.Add( self.m_buttonNextNum, 0, wx.ALL, 5 )

        self.m_buttonNextDbFile = wx.Button(self.m_panel1, wx.ID_ANY, u"textfile>|", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_buttonNextDbFile.SetToolTip( u"Next in text file" )

        bSizer3.Add( self.m_buttonNextDbFile, 0, wx.ALL, 5 )

        self.m_buttonEnterVidNum = wx.Button(self.m_panel1, wx.ID_ANY, u"Enter #...", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_buttonEnterVidNum.SetToolTip( u"Enter media number" )

        bSizer3.Add( self.m_buttonEnterVidNum, 0, wx.ALL, 5 )

        self.m_buttonLouder = wx.Button( self.m_panel1, wx.ID_ANY, u"Louder", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonLouder.SetToolTip( u"Louder" )

        bSizer3.Add( self.m_buttonLouder, 0, wx.ALL, 5 )

        self.m_buttonSofter = wx.Button( self.m_panel1, wx.ID_ANY, u"Softer", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonSofter.SetToolTip( u"Softer" )

        bSizer3.Add( self.m_buttonSofter, 0, wx.ALL, 5 )


        bSizerPanel.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_textCtrlEntry = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, wx.TE_NOHIDESEL | wx.TE_NO_VSCROLL | wx.TE_PROCESS_ENTER )
        self.m_textCtrlEntry.SetToolTip( u"Enter/Edit Comment" )

        bSizerPanel.Add( self.m_textCtrlEntry, 0, wx.ALL | wx.EXPAND, 5 )

        self.m_listCtrlVidComments = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ),
                                                  wx.LC_REPORT | wx.BORDER_SUNKEN )
        self.m_listCtrlVidComments.SetToolTip( u"List of existing Video txt comments" )
        self.m_listCtrlVidComments.SetMinSize( wx.Size( -1,300 ) )
# start copying here
        self.m_listCtrlVidComments.InsertColumn(0, 'MagicNum')
        self.m_listCtrlVidComments.InsertColumn(1, 'Comment')
        self.m_listCtrlVidComments.SetColumnWidth(0, 50)
        self.m_listCtrlVidComments.SetColumnWidth(1, 1500)


        bSizerPanel.Add( self.m_listCtrlVidComments, 0, wx.ALL | wx.EXPAND, 5 )


        self.m_panel1.SetSizer( bSizerPanel )
        self.m_panel1.Layout()
        bSizerPanel.Fit( self.m_panel1 )
        bSizerFrame.Add( self.m_panel1, 1, wx.EXPAND | wx.ALL, 5 )


        self.SetSizer( bSizerFrame )
        self.Layout()
        self.m_menubarMainFrame = wx.MenuBar( 0 )
        self.m_menuFile = wx.Menu()
        self.m_menuItemFileOpen = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"Open Video txt...",
                                               wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuFile.Append( self.m_menuItemFileOpen )

        self.m_menuItemFileSave = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"Save Video txt...",
                                               wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuFile.Append( self.m_menuItemFileSave )

        self.m_menuItemFileSaveAs = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"Save As Video txt..."
                                                 , wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuFile.Append( self.m_menuItemFileSaveAs )

        self.m_menuItemQuit = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"Quit without save...",
                                           wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuFile.Append( self.m_menuItemQuit )

        self.m_menuItemExit = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"Exit and save",
                                            wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuFile.Append( self.m_menuItemExit )

        self.m_menubarMainFrame.Append( self.m_menuFile, u"File" )

        self.m_menuHelp = wx.Menu()
        self.m_menuItemHelpAbout = wx.MenuItem( self.m_menuHelp, wx.ID_ANY, u"About...",
                                                wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuHelp.Append( self.m_menuItemHelpAbout )

        self.m_menubarMainFrame.Append( self.m_menuHelp, u"Help" )

        self.SetMenuBar( self.m_menubarMainFrame )

        self.m_timerMedia = wx.Timer()
        self.m_timerMedia.SetOwner( self, wx.ID_ANY )
        self.m_timerMedia.Start( 125 )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_buttonPrevDbFile.Bind( wx.EVT_BUTTON, self.onBtnPrevFile )
        self.m_buttonPrevNum.Bind( wx.EVT_BUTTON, self.onBtnPrev )
        if self.l_useMdoMediaCtrls:
            self.m_buttonPlay.Bind( wx.EVT_BUTTON, self.onBtnPlay )
            self.m_buttonPause.Bind( wx.EVT_BUTTON, self.onBtnPause )
        self.m_buttonNextNum.Bind( wx.EVT_BUTTON, self.onBtnNext )
        self.m_buttonNextDbFile.Bind( wx.EVT_BUTTON, self.onBtnNextFile )
        self.m_buttonEnterVidNum.Bind( wx.EVT_BUTTON, self.onBtnEnterVidNum )
        self.m_buttonLouder.Bind( wx.EVT_BUTTON, self.onBtnLouder )
        self.m_buttonSofter.Bind( wx.EVT_BUTTON, self.onBtnSofter )
        self.m_textCtrlEntry.Bind( wx.EVT_TEXT_ENTER, self.onTextCtrlEntry )
        self.m_listCtrlVidComments.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.onListCtrlActivated )
        self.Bind( wx.EVT_MENU, self.onFileOpen, id = self.m_menuItemFileOpen.GetId() )
        self.Bind( wx.EVT_MENU, self.onFileSave, id = self.m_menuItemFileSave.GetId() )
        self.Bind( wx.EVT_MENU, self.onFileSaveAs, id = self.m_menuItemFileSaveAs.GetId() )
        self.Bind( wx.EVT_MENU, self.onFileQuit, id = self.m_menuItemQuit.GetId() )
        self.Bind( wx.EVT_MENU, self.onFileExit, id = self.m_menuItemExit.GetId() )
        self.Bind( wx.EVT_MENU, self.onHelpAbout, id = self.m_menuItemHelpAbout.GetId() )
        self.Bind( wx.EVT_TIMER, self.onTimerMedia, id=wx.ID_ANY )
    # end class MainFrame().__init__()

    def __del__( self ):
        del self.m_mediactrl
        pass
    # end class MainFrame().__del__()


    # Virtual event handlers
    def onBtnPrevFile( self, event ):
        possibleIdx = self.doFindDirecTextFileUsableLine(-1)
        if possibleIdx >= 0:
            self.l_dbMediaDescripIdx = possibleIdx
            ignore = self.doLoadupNumMediaFile( mediaWeirdNum = self.l_dbMediaDescripLines[self.l_dbMediaDescripIdx][:5],
                                                statusText= self.l_dbMediaDescripLines[self.l_dbMediaDescripIdx] )
    # end class MainFrame().onBtnPrevFile()

    def onBtnPrev( self, event ):
        ignore, mediaDecNum = fromMarksWeirdNumbers(self.l_mediaCurrentWeirdNum)
        # print("fromMarksWeirdNumbers m_mediaCurrentWeirdNum: |%s| ignore: |%s| mediaDecNum: |%s|" % (self.l_mediaCurrentWeirdNum, ignore, mediaDecNum))
        if mediaDecNum > 1:
            mediaDecNum -= 1
        # print("decrement m_mediaCurrentWeirdNum: |%s| ignore: |%s| mediaDecNum: |%s|" % (self.l_mediaCurrentWeirdNum, ignore, mediaDecNum))
        ignore, weirdMediaNum = toMarksWeirdNumbers(mediaDecNum)
        # print("toMarksWeirdNumbers weirdMediaNum: |%s| ignore: |%s| mediaDecNum: |%s|" % (weirdMediaNum, ignore, mediaDecNum))
        self.doLoadupNumMediaFile( mediaWeirdNum = weirdMediaNum, statusText = "non-text-file %d" % mediaDecNum )
    # end class MainFrame().onBtnPrev()

    def onBtnPlay( self, event ):
        if not self.m_mediactrl.Play():
            wx.MessageBox("Unable to Play media : Unsupported format?",
                "ERROR", wx.ICON_ERROR | wx.OK)
        else:
            self.m_mediactrl.SetInitialSize()
            self.GetSizer().Layout()
    # end class MainFrame().onBtnPlay()

    def onBtnPause( self, event ):
        self.m_mediactrl.Pause()
    # end class MainFrame().onBtnPause()


    def onBtnNext( self, event ):
        ignore, mediaDecNum = fromMarksWeirdNumbers(self.l_mediaCurrentWeirdNum)
        # TODO FIXME Pix vs Movies
        if mediaDecNum < self.l_infoMaxImgMvi["THE_MAX_MVINUM"]:
            mediaDecNum += 1
            ignore, weirdMediaNum = toMarksWeirdNumbers(mediaDecNum)
            self.doLoadupNumMediaFile( mediaWeirdNum = weirdMediaNum, statusText = "non-text-file %d" % mediaDecNum )
    # end class MainFrame().onBtnNext()



    def onBtnNextFile( self, event ):
        possibleIdx = self.doFindDirecTextFileUsableLine(+1)
        if possibleIdx >= 0:
            self.l_dbMediaDescripIdx = possibleIdx
            ignore = self.doLoadupNumMediaFile( mediaWeirdNum = self.l_dbMediaDescripLines[self.l_dbMediaDescripIdx][:5],
                                                statusText= self.l_dbMediaDescripLines[self.l_dbMediaDescripIdx] )
    # end class MainFrame().onBtnNextFile()


    def onBtnEnterVidNum( self, event ):
        tmp = DlgEnterVidNum(self)
        tmp.ShowModal()
        if "UNKNOWN" != tmp.l_returnNumberWeird:
            self.doLoadupNumMediaFile(mediaWeirdNum=tmp.l_returnNumberWeird,
                                      statusText="non-text-file %d" % tmp.l_returnNumberDec)
    # end class MainFrame().onBtnEnterVidNum()

    def onBtnLouder( self, event ):
        # increase volume by 5 percent; makes assumption that current volume is valid
                self.m_mediactrl.SetVolume(min(1.0, self.m_mediactrl.GetVolume()+0.05))
    # end class MainFrame().onBtnLouder()

    def onBtnSofter( self, event ):
        # decrease volume by 5 percent; makes assumption that current volume is valid
                self.m_mediactrl.SetVolume(max(0.0, self.m_mediactrl.GetVolume()-0.05))
    # end class MainFrame().onBtnSofter()

    def onTextCtrlEntry( self, event ):
        event.Skip() # TODO need to write this one
    # end class MainFrame().onTextCtrlEntry()

    def onListCtrlActivated( self, event ):
        # print("OnItemActivated: %s - %s    TopItem: %s" % (event.Index, self.m_listCtrlVidComments.GetItemText(event.Index), self.m_listCtrlVidComments.GetTopItem()))
        # print("  GetColumnWidth() [0] [1]: [%s] [%s]" % (self.m_listCtrlVidComments.GetColumnWidth(0), self.m_listCtrlVidComments.GetColumnWidth(1)))
        # print("  GetItemPosition(event.Index): %s" % self.m_listCtrlVidComments.GetItemPosition(event.Index))
        # print("  GetItemRect(event.Index): %s" % self.m_listCtrlVidComments.GetItemRect(event.Index))
        myRow = event.Index
        myCol = -1
        myX, myY = self.m_listCtrlVidComments.ScreenToClient(wx.GetMousePosition())
        # print("myX=%d" % myX)
        numCols = self.m_listCtrlVidComments.GetColumnCount() # actually I know there are just two
        # print("numCols=%d" % numCols)
        for idx in range(numCols):
            # print("   idx=%d myX=%d" % (idx, myX))
            colWidth = self.m_listCtrlVidComments.GetColumnWidth(idx)
            # print("   colWidth=%d" % colWidth)
            if myX < colWidth:
               myCol = idx
               break
            myX -= colWidth
        print("myRow=%d myCol=%d" % (myRow, myCol))
        textNum = self.m_listCtrlVidComments.GetItemText(myRow,0)
        textString = self.m_listCtrlVidComments.GetItemText(myRow,1)
        # print("item=|%s| |%s|" % (textNum, textString))
        good = False
        if len(textNum) >= 5:
            good, ignore = fromMarksWeirdNumbers(textNum)
        if good:
            self.doLoadupNumMediaFile( mediaWeirdNum = textNum, statusText = "load %s" % textNum )
        else:
            good, ignore = fromMarksWeirdNumbers(textString[1:6])
            if good:
                self.doLoadupNumMediaFile(mediaWeirdNum=textString[1:6], statusText="alt-load %s" % textString[1:6])
    # end class MainFrame().onListCtrlActivated()

    def doAddListCtrlLine( self, line = "", posn = 0 ):
        # adds line to list control  before specified position
        mediaFlag, ignore = fromMarksWeirdNumbers(line, quiet=True)
        if mediaFlag:
            # media line
            self.m_listCtrlVidComments.InsertItem(posn, line[:5])
            self.m_listCtrlVidComments.SetItem(posn, 1, line[5:].strip())
            if line[:5] in self.l_listCtrlInfo.keys():
                self.l_listCtrlInfo[line[:5]]["line"].append(posn)
            else:
                self.l_listCtrlInfo[line[:5]] = {"line": [posn]}
        else:
            # comment
            self.m_listCtrlVidComments.InsertItem(posn, " ")
            self.m_listCtrlVidComments.SetItem(posn, 1, line)
            if " " in self.l_listCtrlInfo.keys():
                self.l_listCtrlInfo[" "]["line"].append(posn)
            else:
                self.l_listCtrlInfo[" "] = {"line": [posn]}
        # alternating colors
        if posn % 2:
            self.m_listCtrlVidComments.SetItemBackgroundColour(posn, "white")
        else:
            self.m_listCtrlVidComments.SetItemBackgroundColour(posn, "yellow")
    # end class MainFrame().doAddListCtrlLine()

    def onFileOpen(self, event):
        # TODO FIXME Pix vs Movies
        dlg = wx.FileDialog(self, message="Choose a NewMovie.txt file in complete Olson www folder",
                            defaultDir=r'X:\OlsonMedia\DigitalCamera\www_html', defaultFile="*.txt",
                            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            loadOK = True
            lcltmp_pathTxtFile = os.path.abspath(dlg.GetPath())
            self.l_dbFileName = dlg.GetFilename()
            self.l_dbDirName = os.path.dirname(lcltmp_pathTxtFile)
            lcltmp_pathTxtFile = os.path.join(self.l_dbDirName, self.l_dbFileName)
            l_pathMediaMaxInfo = os.path.join(self.l_dbDirName, "OlsonPictureInfo.php")
            if False == os.path.exists(l_pathMediaMaxInfo):
                wx.MessageBox("Unable to load required Info file %s: file does not exist" % l_pathMediaMaxInfo,
                              "ERROR", wx.ICON_ERROR | wx.OK)
                loadOK = False
            if loadOK:
                retn = self.doLoadMediaMaxFile(l_pathMediaMaxInfo)
                if "OK" != retn:
                    wx.MessageBox("Unable to load %s: %s" % (lcltmp_pathTxtFile, retn), "ERROR", wx.ICON_ERROR | wx.OK)
                    loadOK = False
            if loadOK:
                retn = self.doLoadMediaDescripFile(lcltmp_pathTxtFile)
                if "OK" != retn:
                    wx.MessageBox("Unable to load %s: %s" % (lcltmp_pathTxtFile, retn), "ERROR", wx.ICON_ERROR | wx.OK)
                    loadOK = False
            if loadOK:
                loadOK = self.doLoadupNumMediaFile(mediaWeirdNum=self.l_dbMediaDescripLines[self.l_dbMediaDescripIdx][:5],
                                                   statusText=self.l_dbMediaDescripLines[self.l_dbMediaDescripIdx])
    # end class MainFrame().onFileOpen()

    def doGetTxtFileLines(self, fname):
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
    # end class MainFrame()doGetTxtFileLines()

    def doLoadMediaMaxFile(self, fname):
        """gets last filenum for MVI and IMG"""
        # should contain lines that look like this:
        # define("THE_MAX_IMGNUM","45065");
        # define("THE_MAX_MVINUM","3441");
        self.l_infoMaxImgMvi = {}
        lcl_infoMediaMax = {"THE_MAX_IMGNUM": -1, "THE_MAX_MVINUM": -1}
        retn, lcltmp_infoLines = self.doGetTxtFileLines( fname )
        if "OK" != retn:
            return retn
        for line in lcltmp_infoLines:
            for key in lcl_infoMediaMax.keys():
                if -1 != line.find(key):
                    lsplit = line.split('"')
                    try:
                        lcl_infoMediaMax[key] = int(lsplit[-2])
                    except:
                        lcl_infoMediaMax[key] = -1
                        retn = "ERROR: file %s not in infoFile format" % fname
        if ("OK" == retn) and (lcl_infoMediaMax["THE_MAX_IMGNUM"] > 0) and (lcl_infoMediaMax["THE_MAX_MVINUM"] > 0):
            # lcl_infoMediaMax is good; store it
            self.l_infoMaxImgMvi = lcl_infoMediaMax
            # let's just see if the info in lcl_infoMediaMax is up to date, shall we?
            # TODO FIXME Pix vs Movies
            ignore, lcl_mediaWeirdNum = toMarksWeirdNumbers(lcl_infoMediaMax["THE_MAX_MVINUM"])
            lcl_mediaDirList = sorted(os.listdir((os.path.join(os.path.dirname(fname), 'movies', lcl_mediaWeirdNum[:2]))))
            lcl_mp4List = []
            for mDirFile in lcl_mediaDirList:
                if mDirFile.endswith(".MP4"):
                   lcl_mp4List.append(mDirFile)
            # TODO FIXME Pix vs Movies TODO
            lcl_expectedLastFile = "MVI"+lcl_mediaWeirdNum+".MP4"
            lcl_found = -1
            if lcl_expectedLastFile in lcl_mp4List:
                lcl_found = lcl_mp4List.index(lcl_expectedLastFile)
            if lcl_found < 0:
                # TODO FIXME Pix vs Movies
                wx.MessageBox("Warning: directory structure does not include \"%s\" media directory files per infoFile %s" % ("movie", fname), "ERROR", wx.ICON_ERROR | wx.OK)
            elif (lcl_found + 1) != len(lcl_mp4List):
                ignore, lcl_decNum =  fromMarksWeirdNumbers(lcl_mp4List[-1][3:3+5], quiet=True)
                wx.MessageBox("Warning: \"%s\" media directory files per infoFile %s\nExpected last file was %s (%d)\nActual last file in directory was %s (%d)" % ("movie", fname, lcl_expectedLastFile, lcl_infoMediaMax["THE_MAX_MVINUM"], lcl_mp4List[-1], lcl_decNum), "ERROR", wx.ICON_ERROR | wx.OK)
        return retn
    # end class MainFrame().doLoadMediaMaxFile()

    def doLoadMediaDescripFile(self, fname):
        """Opens text file"""
        self.l_dbMediaDescripIdx = -1
        retn, self.l_dbMediaDescripLines = self.doGetTxtFileLines( fname )
        if "OK" != retn:
            self.l_dbMediaDescripLines = []
            return retn
        if ("#" != self.l_dbMediaDescripLines[-1][0]) or (-1 == self.l_dbMediaDescripLines[-1].find("END OF FILE")):
            self.l_dbMediaDescripLines = []
            return "ERROR: file %s last line is not # ... END OF FILE" % fname
        self.l_dbMediaDescripPath = os.path.abspath(fname)
        self.l_rootDir = os.path.dirname(self.l_dbMediaDescripPath)
        for line in self.l_dbMediaDescripLines:
            self.doAddListCtrlLine(line, self.m_listCtrlVidComments.GetItemCount())
        self.l_dbMediaDescripIdx = len(self.l_dbMediaDescripLines)-1
        self.l_dbMediaDescripIdx = self.doFindDirecTextFileUsableLine(-1)
        if self.l_dbMediaDescripIdx < 0:
            self.l_dbMediaDescripLines = []
            retn = "ERROR: file %s has no non-comment lines" % fname
        self.m_listCtrlVidComments.EnsureVisible(self.l_dbMediaDescripIdx)
        return retn
    # end class MainFrame().doLoadMediaDescripFile()

    def doLoadupNumMediaFile( self, mediaWeirdNum = "_0001", statusText = "Status: ..." ):
        loadOK = True
        nowStatus = self.m_staticTextStatus.GetLabel()
        nowTextCtrlEntry = self.m_textCtrlEntry.GetValue()
        self.m_staticTextStatus.SetLabel("Status: loading %s ..." % mediaWeirdNum)
        # TODO FIXME Pix vs Movies
        self.l_mediaLength = None
        mediaFile = os.path.join(self.l_rootDir, 'movies', mediaWeirdNum[:2], "MVI"+mediaWeirdNum+".MP4")
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
                self.m_staticTextStatus.SetLabel("Status: %s (%s)" % (statusText, self.l_mediaMtime))
                self.m_mediactrl.SetInitialSize()
                self.GetSizer().Layout()
                self.l_mediaMtime = time.ctime(os.path.getmtime(mediaFile))
                self.l_mediaCurrentWeirdNum = mediaWeirdNum
        self.l_mediaStartStopDisplay = loadOK
        if not loadOK:
            self.m_staticTextStatus.SetLabel(nowStatus)
            self.m_textCtrlEntry.ChangeValue(nowTextCtrlEntry) # avoid generating wxEVT_TEXT with SetValue
        else:
            if nowTextCtrlEntry != self.l_textCtrlEntry_unchanged:
               pass # TODO FIXME save edited text
            self.l_listCtrlSlctd["prev"] = self.l_listCtrlSlctd["curr"]
            self.l_listCtrlSlctd["curr"] = mediaWeirdNum
            theListCtrlLine = self.getListCtrlLine(self.l_listCtrlSlctd["prev"])
            if theListCtrlLine >= 0:
                self.m_listCtrlVidComments.Select(theListCtrlLine, 0)
            bestMatchLine = self.getListCtrlLine(mediaWeirdNum)
            if bestMatchLine >= 0: # landed on a line in the text file
                self.l_dbMediaDescripIdx = bestMatchLine
                self.m_listCtrlVidComments.Select(self.l_dbMediaDescripIdx, 1)
                self.m_listCtrlVidComments.EnsureVisible(self.l_dbMediaDescripIdx)
                self.l_textCtrlEntry_unchanged = self.l_dbMediaDescripLines[bestMatchLine]
                self.m_textCtrlEntry.ChangeValue(self.l_textCtrlEntry_unchanged) # avoid generating wxEVT_TEXT with SetValue
            else: # did not land on a line in the text file
                self.l_textCtrlEntry_unchanged = ""
                self.m_textCtrlEntry.ChangeValue("") # avoid generating wxEVT_TEXT with SetValue
                pass
        return loadOK # we already notified the user as needed
    # end class MainFrame().doLoadupNumMediaFile()

    def getListCtrlLine(self, mediaWeirdNum):
        lineNum = -1
        # TODO FIXME make it choose the same one the user clicked if more than one of same in listctrl
        if mediaWeirdNum in self.l_listCtrlInfo.keys():
            lineNum = self.l_listCtrlInfo[mediaWeirdNum]["line"][0]
        return lineNum
    # end class MainFrame().getListCtrlLine()

    def doFindDirecTextFileUsableLine(self, direc):
        """finds m_txtFileLines Usable Line idx in direction direc or -1"""
        foundit = -1
        good = False
        idx = self.l_dbMediaDescripIdx
        while True:
            idx += direc
            if (idx < 0) or (idx >= len(self.l_dbMediaDescripLines)):
                break
            good, ignore = fromMarksWeirdNumbers(self.l_dbMediaDescripLines[idx], quiet=True)
            if good != True:
                continue
            else:
                foundit = idx
                break
        return foundit
    # end class MainFrame().doFindDirecTextFileUsableLine()

    def writeMediaFile(self):
        fPtr = None
        try:
            fPtr = open(os.path.join(self.l_dbDirName, self.l_dbFileName), 'wt')
            for myLnum in range(self.m_listCtrlVidComments.GetItemCount()):
                textNum = self.m_listCtrlVidComments.GetItemText(myLnum, 0)
                textString = self.m_listCtrlVidComments.GetItemText(myLnum, 1)
                mediaFlag, ignore = fromMarksWeirdNumbers(textNum, quiet=True)
                if mediaFlag:
                    fPtr.write("%s %s\n" % (textNum, textString))
                else:
                    fPtr.write("%s\n" % textString)
            fPtr.close()
            fPtr = None
        except:
            message = wx.MessageDialog(self, _("Could not save file; file not saved. Try again."),
                                       _("ERROR"), wx.OK | wx.ICON_ERROR)
            message.ShowModal()
            message.Destroy()
            if fPtr is not None:
                fPtr.close()
    # end MainFrame().writeMediaFile(self):

    def onFileSave( self, event ):
        event.Skip()            # TODO need to write this one
    # end class MainFrame().onFileSave()

    def onFileSaveAs( self, event ):
        dlg = None
        dlg = wx.FileDialog(self, "Save to file:", ".", "", "Text (*.txt)|*.txt", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            self.l_dbFileName = dlg.GetFilename()
            self.l_dbDirName = dlg.GetDirectory()
            self.writeMediaFile()
        dlg.Destroy()
        dlg = None
    # end class MainFrame().onFileSaveAs()

    def onFileQuit( self, event ):
        dlgRslt = wx.MessageBox("Are you sure? This will lose changes", "Are you sure?",
                                wx.YES|wx.NO|wx.CANCEL|wx.ICON_EXCLAMATION|wx.CENTRE)
        if wx.NO == dlgRslt:
            event.Skip() # OK; just keep going
        else:
            self.Close()
    # end class MainFrame().onFileQuit()

    def onFileExit( self, event ):
        event.Skip()            # TODO need to write this one
    # end class MainFrame().onFileExit()

    def onHelpAbout( self, event ):
        event.Skip()            # TODO need to write this one
    # end class MainFrame().onHelpAbout()

    """TODO FIXME TODO start/stop movie on click in movie window
    def onMouseUpLeftUp( self, event): # if click in movie window, toggle play-stop for movie
        myX, myY = self.m_mediactrl.ScreenToClient(wx.GetMousePosition())
        print("myX=%d, myY=%d" % (myX, myY))
        event.Skip()            # TODO need to write this one
    # end class MainFrame().onMouseUpLeftUp()
    """

    def onTimerMedia( self, event ):
        # the length is -1 if nothing is loaded
        # after the load it is length None
        # some time after loading it goes to 0
        # some time after that it goes to number of millisecs (ex: 9637)
        # then some time later it rounds off to the seconds (ex: 9000); I don't know why
        # we want to keep the 9637 from the example above
        if self.l_mediaStartStopDisplay: # set True to load to a bit past the start
            tmp = self.m_mediactrl.Length()
            if ((None == self.l_mediaLength) or (self.l_mediaLength <= 0)) and ((tmp > 0) and (self.l_mediaLength != tmp)):
                self.l_mediaLength = self.m_mediactrl.Length()
                # print("timer length %s" % self.l_mediaLength)
                if self.m_mediactrl.Play():
                    # print("timer: Play worked")
                    self.m_mediactrl.SetInitialSize()
                    self.GetSizer().Layout()
                    sleep(0.05) # sleep seconds
                    self.m_mediactrl.Pause()
                    self.l_mediaStartStopDisplay = False
    # end class MainFrame().onTimerMedia()



###########################################################################
## MAIN PROGRAM
###########################################################################

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame(None, os.path.dirname(os.path.realpath(__file__))).Show()
    app.MainLoop()

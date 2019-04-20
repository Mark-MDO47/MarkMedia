----------------------------------------------------------------------------
-- Lua code generated with wxFormBuilder (version Oct 26 2018)
-- http://www.wxformbuilder.org/
----------------------------------------------------------------------------

-- Load the wxLua module, does nothing if running from wxLua, wxLuaFreeze, or wxLuaEdit
package.cpath = package.cpath..";./?.dll;./?.so;../lib/?.so;../lib/vc_dll/?.dll;../lib/bcc_dll/?.dll;../lib/mingw_dll/?.dll;"
require("wx")

UI = {}


-- create MainFrame
UI.MainFrame = wx.wxFrame (wx.NULL, wx.wxID_ANY, "", wx.wxDefaultPosition, wx.wxSize( 1245,1193 ), wx.wxDEFAULT_FRAME_STYLE+wx.wxTAB_TRAVERSAL )
	UI.MainFrame:SetSizeHints( wx.wxDefaultSize, wx.wxDefaultSize )

	UI.bSizerFrame = wx.wxBoxSizer( wx.wxVERTICAL )

	UI.m_panel1 = wx.wxPanel( UI.MainFrame, wx.wxID_ANY, wx.wxDefaultPosition, wx.wxDefaultSize, wx.wxTAB_TRAVERSAL )
	UI.m_panel1:SetToolTip( "Video is displayed here" )

	UI.bSizerPanel = wx.wxBoxSizer( wx.wxVERTICAL )

	UI.m_staticTextStatus = wx.wxStaticText( UI.m_panel1, wx.wxID_ANY, "Status: ...", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_staticTextStatus:Wrap( -1 )

	UI.m_staticTextStatus:SetToolTip( "Status is displayed here" )

	UI.bSizerPanel:Add( UI.m_staticTextStatus, 0, wx.wxALL + wx.wxEXPAND, 5 )

	UI.m_notebookMediaCtrl = wx.wxNotebook( UI.m_panel1, wx.wxID_ANY, wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_notebookMediaCtrl:SetMinSize( wx.wxSize( 800,800 ) )


	UI.bSizerPanel:Add( UI.m_notebookMediaCtrl, 1, wx.wxALL + wx.wxALIGN_CENTER_HORIZONTAL, 5 )

	UI.bSizer3 = wx.wxBoxSizer( wx.wxHORIZONTAL )

	UI.m_buttonPrevfile = wx.wxButton( UI.m_panel1, wx.wxID_ANY, "|<textfile", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_buttonPrevfile:SetToolTip( "Previous in text file" )

	UI.bSizer3:Add( UI.m_buttonPrevfile, 0, wx.wxALL, 5 )

	UI.m_buttonPrev = wx.wxButton( UI.m_panel1, wx.wxID_ANY, "|<", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_buttonPrev:SetToolTip( "Previous media file" )

	UI.bSizer3:Add( UI.m_buttonPrev, 0, wx.wxALL, 5 )

	UI.m_buttonPlay = wx.wxButton( UI.m_panel1, wx.wxID_ANY, ">", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_buttonPlay:SetToolTip( "Play" )

	UI.bSizer3:Add( UI.m_buttonPlay, 0, wx.wxALL, 5 )

	UI.m_buttonPause = wx.wxButton( UI.m_panel1, wx.wxID_ANY, ">][<", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_buttonPause:SetToolTip( "Pause" )

	UI.bSizer3:Add( UI.m_buttonPause, 0, wx.wxALL, 5 )

	UI.m_buttonNext = wx.wxButton( UI.m_panel1, wx.wxID_ANY, ">|", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_buttonNext:SetToolTip( "Next media file" )

	UI.bSizer3:Add( UI.m_buttonNext, 0, wx.wxALL, 5 )

	UI.m_buttonNextFile = wx.wxButton( UI.m_panel1, wx.wxID_ANY, "textfile>|", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_buttonNextFile:SetToolTip( "Next in text file" )

	UI.bSizer3:Add( UI.m_buttonNextFile, 0, wx.wxALL, 5 )

	UI.m_buttonEnterVidNum = wx.wxButton( UI.m_panel1, wx.wxID_ANY, "Enter #...", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_buttonEnterVidNum:SetToolTip( "Enter media number" )

	UI.bSizer3:Add( UI.m_buttonEnterVidNum, 0, wx.wxALL, 5 )

	UI.m_buttonLouder = wx.wxButton( UI.m_panel1, wx.wxID_ANY, "Louder", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_buttonLouder:SetToolTip( "Louder" )

	UI.bSizer3:Add( UI.m_buttonLouder, 0, wx.wxALL, 5 )

	UI.m_buttonSofter = wx.wxButton( UI.m_panel1, wx.wxID_ANY, "Softer", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_buttonSofter:SetToolTip( "Softer" )

	UI.bSizer3:Add( UI.m_buttonSofter, 0, wx.wxALL, 5 )


	UI.bSizerPanel:Add( UI.bSizer3, 0, wx.wxALIGN_CENTER_HORIZONTAL, 5 )

	UI.m_textCtrl1 = wx.wxTextCtrl( UI.m_panel1, wx.wxID_ANY, "", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.m_textCtrl1:SetToolTip( "Enter/Edit Comment" )

	UI.bSizerPanel:Add( UI.m_textCtrl1, 0, wx.wxALL + wx.wxEXPAND, 5 )

	UI.m_listBoxVidCommentsChoices = {}
	UI.m_listBoxVidComments = wx.wxListBox( UI.m_panel1, wx.wxID_ANY, wx.wxDefaultPosition, wx.wxDefaultSize, UI.m_listBoxVidCommentsChoices, wx.wxLB_ALWAYS_SB + wx.wxLB_HSCROLL + wx.wxLB_SINGLE )
	UI.m_listBoxVidComments:SetToolTip( "List of existing Video txt comments" )
	UI.m_listBoxVidComments:SetMinSize( wx.wxSize( -1,300 ) )

	UI.bSizerPanel:Add( UI.m_listBoxVidComments, 0, wx.wxALL + wx.wxEXPAND, 5 )


	UI.m_panel1:SetSizer( UI.bSizerPanel )
	UI.m_panel1:Layout()
	UI.bSizerPanel:Fit( UI.m_panel1 )
	UI.bSizerFrame:Add( UI.m_panel1, 1, wx.wxEXPAND  + wx. wxALL, 5 )


	UI.MainFrame:SetSizer( UI.bSizerFrame )
	UI.MainFrame:Layout()
	UI.m_menubarMainFrame = wx.wxMenuBar( 0 )
	UI.m_menuFile = wx.wxMenu()
	UI.m_menuItemFileOpen = wx.wxMenuItem( UI.m_menuFile, wx.wxID_ANY, "Open Video txt...", "", wx.wxITEM_NORMAL )
	UI.m_menuFile:Append( UI.m_menuItemFileOpen )

	UI.m_menuItemFileSave = wx.wxMenuItem( UI.m_menuFile, wx.wxID_ANY, "Save Video txt...", "", wx.wxITEM_NORMAL )
	UI.m_menuFile:Append( UI.m_menuItemFileSave )

	UI.m_menuItemFileSaveAs = wx.wxMenuItem( UI.m_menuFile, wx.wxID_ANY, "Save As Video txt...", "", wx.wxITEM_NORMAL )
	UI.m_menuFile:Append( UI.m_menuItemFileSaveAs )

	UI.m_menuItemQuit = wx.wxMenuItem( UI.m_menuFile, wx.wxID_ANY, "Quit without save...", "", wx.wxITEM_NORMAL )
	UI.m_menuFile:Append( UI.m_menuItemQuit )

	UI.m_menuItemeExit = wx.wxMenuItem( UI.m_menuFile, wx.wxID_ANY, "Exit and save", "", wx.wxITEM_NORMAL )
	UI.m_menuFile:Append( UI.m_menuItemeExit )

	UI.m_menubarMainFrame:Append( UI.m_menuFile, "File" )

	UI.m_menuHelp = wx.wxMenu()
	UI.m_menuItemHelpAbout = wx.wxMenuItem( UI.m_menuHelp, wx.wxID_ANY, "About...", "", wx.wxITEM_NORMAL )
	UI.m_menuHelp:Append( UI.m_menuItemHelpAbout )

	UI.m_menubarMainFrame:Append( UI.m_menuHelp, "Help" )

	UI.MainFrame:SetMenuBar( UI.m_menubarMainFrame )


	UI.MainFrame:Centre( wx.wxBOTH )

	-- Connect Events

	UI.m_buttonPrevfile:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements onBtnPrevFile

	event:Skip()
	end )

	UI.m_buttonPrev:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements onBtnPrev

	event:Skip()
	end )

	UI.m_buttonPlay:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements onBtnPlay

	event:Skip()
	end )

	UI.m_buttonPause:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements onBtnPause

	event:Skip()
	end )

	UI.m_buttonNext:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements onBtnNext

	event:Skip()
	end )

	UI.m_buttonNextFile:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements onBtnNextFile

	event:Skip()
	end )

	UI.m_buttonEnterVidNum:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements onBtnEnterVidNum

	event:Skip()
	end )

	UI.m_buttonLouder:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements onBtnLouder

	event:Skip()
	end )

	UI.m_buttonSofter:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements onBtnSofter

	event:Skip()
	end )

	UI.m_listBoxVidComments:Connect( wx.wxEVT_COMMAND_LISTBOX_SELECTED, function(event)
	--implements onLBoxVidComments

	event:Skip()
	end )

	UI.m_listBoxVidComments:Connect( wx.wxEVT_COMMAND_LISTBOX_DOUBLECLICKED, function(event)
	--implements onListBoxDClickVidComments

	event:Skip()
	end )

	UI.MainFrame:Connect( wx.wxID_ANY ,wx.wxEVT_COMMAND_MENU_SELECTED , function(event)
	--implements OnFileOpen

	event:Skip()
	end)

	UI.MainFrame:Connect( wx.wxID_ANY ,wx.wxEVT_COMMAND_MENU_SELECTED , function(event)
	--implements onFileSave

	event:Skip()
	end)

	UI.MainFrame:Connect( wx.wxID_ANY ,wx.wxEVT_COMMAND_MENU_SELECTED , function(event)
	--implements onFileSaveAs

	event:Skip()
	end)

	UI.MainFrame:Connect( wx.wxID_ANY ,wx.wxEVT_COMMAND_MENU_SELECTED , function(event)
	--implements OnFileQuit

	event:Skip()
	end)

	UI.MainFrame:Connect( wx.wxID_ANY ,wx.wxEVT_COMMAND_MENU_SELECTED , function(event)
	--implements OnFileExit

	event:Skip()
	end)

	UI.MainFrame:Connect( wx.wxID_ANY ,wx.wxEVT_COMMAND_MENU_SELECTED , function(event)
	--implements onHelpAbout

	event:Skip()
	end)



--wx.wxGetApp():MainLoop()

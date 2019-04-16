----------------------------------------------------------------------------
-- Lua code generated with wxFormBuilder (version Oct 26 2018)
-- http://www.wxformbuilder.org/
----------------------------------------------------------------------------

-- Load the wxLua module, does nothing if running from wxLua, wxLuaFreeze, or wxLuaEdit
package.cpath = package.cpath..";./?.dll;./?.so;../lib/?.so;../lib/vc_dll/?.dll;../lib/bcc_dll/?.dll;../lib/mingw_dll/?.dll;"
require("wx")

UI = {}


-- create DlgEnterVidNum
UI.DlgEnterVidNum = wx.wxDialog (wx.NULL, wx.wxID_ANY, "", wx.wxDefaultPosition, wx.wxSize( 474,187 ), wx.wxDEFAULT_DIALOG_STYLE )
	UI.DlgEnterVidNum:SetSizeHints( wx.wxDefaultSize, wx.wxDefaultSize )

	UI.bSizer4 = wx.wxBoxSizer( wx.wxVERTICAL )

	UI.m_staticTextDlgEnterVidNum = wx.wxStaticText( UI.DlgEnterVidNum, wx.wxID_ANY, "Enter last 5 digits below. Example:  for IMG_P085 enter _P085, for MVI0C123 enter 0C123", wx.wxDefaultPosition, wx.wxDefaultSize, wx.wxALIGN_CENTER_HORIZONTAL )
	UI.m_staticTextDlgEnterVidNum:Wrap( -1 )

	UI.bSizer4:Add( UI.m_staticTextDlgEnterVidNum, 0, wx.wxALL + wx.wxALIGN_CENTER_HORIZONTAL, 5 )

	UI.m_textCtrl2 = wx.wxTextCtrl( UI.DlgEnterVidNum, wx.wxID_ANY, "", wx.wxDefaultPosition, wx.wxDefaultSize, 0 )
	UI.bSizer4:Add( UI.m_textCtrl2, 0, wx.wxALL + wx.wxALIGN_CENTER_HORIZONTAL, 5 )

	UI.m_staticTextDlgEnterVidNumStatus = wx.wxStaticText( UI.DlgEnterVidNum, wx.wxID_ANY, "Status: waiting for entry...", wx.wxDefaultPosition, wx.wxDefaultSize, wx.wxALIGN_CENTER_HORIZONTAL )
	UI.m_staticTextDlgEnterVidNumStatus:Wrap( -1 )

	UI.bSizer4:Add( UI.m_staticTextDlgEnterVidNumStatus, 0, wx.wxALL + wx.wxALIGN_CENTER_HORIZONTAL, 5 )

	UI.m_sdbSizer1 = wx.wxStdDialogButtonSizer()
	UI.m_sdbSizer1Apply = wx.wxButton( UI.DlgEnterVidNum, wx.wxID_APPLY, "" )
	UI.m_sdbSizer1:AddButton( UI.m_sdbSizer1Apply )
	UI.m_sdbSizer1Cancel = wx.wxButton( UI.DlgEnterVidNum, wx.wxID_CANCEL, "" )
	UI.m_sdbSizer1:AddButton( UI.m_sdbSizer1Cancel )
	UI.m_sdbSizer1:Realize();

	UI.bSizer4:Add( UI.m_sdbSizer1, 1, wx.wxALIGN_CENTER_HORIZONTAL, 5 )


	UI.DlgEnterVidNum:SetSizer( UI.bSizer4 )
	UI.DlgEnterVidNum:Layout()

	UI.DlgEnterVidNum:Centre( wx.wxBOTH )

	-- Connect Events

	UI.m_sdbSizer1Apply:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements onDlgBtnEnterVidNumApply

	event:Skip()
	end )

	UI.m_sdbSizer1Cancel:Connect( wx.wxEVT_COMMAND_BUTTON_CLICKED, function(event)
	--implements onDlgBtnEnterVidNumCancel

	event:Skip()
	end )



--wx.wxGetApp():MainLoop()

///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "MarkMedia.h"

///////////////////////////////////////////////////////////////////////////

MainFrame::MainFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* bSizerFrame;
	bSizerFrame = new wxBoxSizer( wxVERTICAL );

	m_panel1 = new wxPanel( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	m_panel1->SetToolTip( wxT("Video is displayed here") );

	wxBoxSizer* bSizerPanel;
	bSizerPanel = new wxBoxSizer( wxVERTICAL );

	m_staticTextStatus = new wxStaticText( m_panel1, wxID_ANY, wxT("Status: ..."), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextStatus->Wrap( -1 );
	m_staticTextStatus->SetToolTip( wxT("Status is displayed here") );

	bSizerPanel->Add( m_staticTextStatus, 0, wxALL|wxEXPAND, 5 );

	m_notebookMediaCtrl = new wxNotebook( m_panel1, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	m_notebookMediaCtrl->SetMinSize( wxSize( 800,800 ) );


	bSizerPanel->Add( m_notebookMediaCtrl, 1, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	wxBoxSizer* bSizer3;
	bSizer3 = new wxBoxSizer( wxHORIZONTAL );

	m_buttonPrevfile = new wxButton( m_panel1, wxID_ANY, wxT("|<textfile"), wxDefaultPosition, wxDefaultSize, 0 );
	m_buttonPrevfile->SetToolTip( wxT("Previous in text file") );

	bSizer3->Add( m_buttonPrevfile, 0, wxALL, 5 );

	m_buttonPrev = new wxButton( m_panel1, wxID_ANY, wxT("|<"), wxDefaultPosition, wxDefaultSize, 0 );
	m_buttonPrev->SetToolTip( wxT("Previous media file") );

	bSizer3->Add( m_buttonPrev, 0, wxALL, 5 );

	m_buttonPlay = new wxButton( m_panel1, wxID_ANY, wxT(">"), wxDefaultPosition, wxDefaultSize, 0 );
	m_buttonPlay->SetToolTip( wxT("Play") );

	bSizer3->Add( m_buttonPlay, 0, wxALL, 5 );

	m_buttonPause = new wxButton( m_panel1, wxID_ANY, wxT(">][<"), wxDefaultPosition, wxDefaultSize, 0 );
	m_buttonPause->SetToolTip( wxT("Pause") );

	bSizer3->Add( m_buttonPause, 0, wxALL, 5 );

	m_buttonNext = new wxButton( m_panel1, wxID_ANY, wxT(">|"), wxDefaultPosition, wxDefaultSize, 0 );
	m_buttonNext->SetToolTip( wxT("Next media file") );

	bSizer3->Add( m_buttonNext, 0, wxALL, 5 );

	m_buttonNextFile = new wxButton( m_panel1, wxID_ANY, wxT("textfile>|"), wxDefaultPosition, wxDefaultSize, 0 );
	m_buttonNextFile->SetToolTip( wxT("Next in text file") );

	bSizer3->Add( m_buttonNextFile, 0, wxALL, 5 );

	m_buttonEnterVidNum = new wxButton( m_panel1, wxID_ANY, wxT("Enter #..."), wxDefaultPosition, wxDefaultSize, 0 );
	m_buttonEnterVidNum->SetToolTip( wxT("Enter media number") );

	bSizer3->Add( m_buttonEnterVidNum, 0, wxALL, 5 );

	m_buttonLouder = new wxButton( m_panel1, wxID_ANY, wxT("Louder"), wxDefaultPosition, wxDefaultSize, 0 );
	m_buttonLouder->SetToolTip( wxT("Louder") );

	bSizer3->Add( m_buttonLouder, 0, wxALL, 5 );

	m_buttonSofter = new wxButton( m_panel1, wxID_ANY, wxT("Softer"), wxDefaultPosition, wxDefaultSize, 0 );
	m_buttonSofter->SetToolTip( wxT("Softer") );

	bSizer3->Add( m_buttonSofter, 0, wxALL, 5 );


	bSizerPanel->Add( bSizer3, 0, wxALIGN_CENTER_HORIZONTAL, 5 );

	m_textCtrl1 = new wxTextCtrl( m_panel1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_textCtrl1->SetToolTip( wxT("Enter/Edit Comment") );

	bSizerPanel->Add( m_textCtrl1, 0, wxALL|wxEXPAND, 5 );

	m_listBoxVidComments = new wxListBox( m_panel1, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, wxLB_ALWAYS_SB|wxLB_HSCROLL|wxLB_SINGLE );
	m_listBoxVidComments->SetToolTip( wxT("List of existing Video txt comments") );
	m_listBoxVidComments->SetMinSize( wxSize( -1,300 ) );

	bSizerPanel->Add( m_listBoxVidComments, 0, wxALL|wxEXPAND, 5 );


	m_panel1->SetSizer( bSizerPanel );
	m_panel1->Layout();
	bSizerPanel->Fit( m_panel1 );
	bSizerFrame->Add( m_panel1, 1, wxEXPAND | wxALL, 5 );


	this->SetSizer( bSizerFrame );
	this->Layout();
	m_menubarMainFrame = new wxMenuBar( 0 );
	m_menuFile = new wxMenu();
	wxMenuItem* m_menuItemFileOpen;
	m_menuItemFileOpen = new wxMenuItem( m_menuFile, wxID_ANY, wxString( wxT("Open Video txt...") ) , wxEmptyString, wxITEM_NORMAL );
	m_menuFile->Append( m_menuItemFileOpen );

	wxMenuItem* m_menuItemFileSave;
	m_menuItemFileSave = new wxMenuItem( m_menuFile, wxID_ANY, wxString( wxT("Save Video txt...") ) , wxEmptyString, wxITEM_NORMAL );
	m_menuFile->Append( m_menuItemFileSave );

	wxMenuItem* m_menuItemFileSaveAs;
	m_menuItemFileSaveAs = new wxMenuItem( m_menuFile, wxID_ANY, wxString( wxT("Save As Video txt...") ) , wxEmptyString, wxITEM_NORMAL );
	m_menuFile->Append( m_menuItemFileSaveAs );

	wxMenuItem* m_menuItemQuit;
	m_menuItemQuit = new wxMenuItem( m_menuFile, wxID_ANY, wxString( wxT("Quit without save...") ) , wxEmptyString, wxITEM_NORMAL );
	m_menuFile->Append( m_menuItemQuit );

	wxMenuItem* m_menuItemeExit;
	m_menuItemeExit = new wxMenuItem( m_menuFile, wxID_ANY, wxString( wxT("Exit and save") ) , wxEmptyString, wxITEM_NORMAL );
	m_menuFile->Append( m_menuItemeExit );

	m_menubarMainFrame->Append( m_menuFile, wxT("File") );

	m_menuHelp = new wxMenu();
	wxMenuItem* m_menuItemHelpAbout;
	m_menuItemHelpAbout = new wxMenuItem( m_menuHelp, wxID_ANY, wxString( wxT("About...") ) , wxEmptyString, wxITEM_NORMAL );
	m_menuHelp->Append( m_menuItemHelpAbout );

	m_menubarMainFrame->Append( m_menuHelp, wxT("Help") );

	this->SetMenuBar( m_menubarMainFrame );

	m_timerMedia.SetOwner( this, wxID_ANY );
	m_timerMedia.Start( 125 );


	this->Centre( wxBOTH );

	// Connect Events
	m_buttonPrevfile->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnPrevFile ), NULL, this );
	m_buttonPrev->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnPrev ), NULL, this );
	m_buttonPlay->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnPlay ), NULL, this );
	m_buttonPause->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnPause ), NULL, this );
	m_buttonNext->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnNext ), NULL, this );
	m_buttonNextFile->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnNextFile ), NULL, this );
	m_buttonEnterVidNum->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnEnterVidNum ), NULL, this );
	m_buttonLouder->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnLouder ), NULL, this );
	m_buttonSofter->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnSofter ), NULL, this );
	m_listBoxVidComments->Connect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( MainFrame::onLBoxVidComments ), NULL, this );
	m_listBoxVidComments->Connect( wxEVT_COMMAND_LISTBOX_DOUBLECLICKED, wxCommandEventHandler( MainFrame::onListBoxDClickVidComments ), NULL, this );
	m_menuFile->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrame::OnFileOpen ), this, m_menuItemFileOpen->GetId());
	m_menuFile->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrame::onFileSave ), this, m_menuItemFileSave->GetId());
	m_menuFile->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrame::onFileSaveAs ), this, m_menuItemFileSaveAs->GetId());
	m_menuFile->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrame::OnFileQuit ), this, m_menuItemQuit->GetId());
	m_menuFile->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrame::OnFileExit ), this, m_menuItemeExit->GetId());
	m_menuHelp->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( MainFrame::onHelpAbout ), this, m_menuItemHelpAbout->GetId());
	this->Connect( wxID_ANY, wxEVT_TIMER, wxTimerEventHandler( MainFrame::onTimerMedia ) );
}

MainFrame::~MainFrame()
{
	// Disconnect Events
	m_buttonPrevfile->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnPrevFile ), NULL, this );
	m_buttonPrev->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnPrev ), NULL, this );
	m_buttonPlay->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnPlay ), NULL, this );
	m_buttonPause->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnPause ), NULL, this );
	m_buttonNext->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnNext ), NULL, this );
	m_buttonNextFile->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnNextFile ), NULL, this );
	m_buttonEnterVidNum->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnEnterVidNum ), NULL, this );
	m_buttonLouder->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnLouder ), NULL, this );
	m_buttonSofter->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MainFrame::onBtnSofter ), NULL, this );
	m_listBoxVidComments->Disconnect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( MainFrame::onLBoxVidComments ), NULL, this );
	m_listBoxVidComments->Disconnect( wxEVT_COMMAND_LISTBOX_DOUBLECLICKED, wxCommandEventHandler( MainFrame::onListBoxDClickVidComments ), NULL, this );
	this->Disconnect( wxID_ANY, wxEVT_TIMER, wxTimerEventHandler( MainFrame::onTimerMedia ) );

}

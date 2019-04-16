///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "DialogEnterVidNum.h"

///////////////////////////////////////////////////////////////////////////

DlgEnterVidNum::DlgEnterVidNum( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxDialog( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* bSizer4;
	bSizer4 = new wxBoxSizer( wxVERTICAL );

	m_staticTextDlgEnterVidNum = new wxStaticText( this, wxID_ANY, _("Enter last 5 digits below. Example:  for IMG_P085 enter _P085, for MVI0C123 enter 0C123"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticTextDlgEnterVidNum->Wrap( -1 );
	bSizer4->Add( m_staticTextDlgEnterVidNum, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	m_textCtrl2 = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer4->Add( m_textCtrl2, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	m_staticTextDlgEnterVidNumStatus = new wxStaticText( this, wxID_ANY, _("Status: waiting for entry..."), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticTextDlgEnterVidNumStatus->Wrap( -1 );
	bSizer4->Add( m_staticTextDlgEnterVidNumStatus, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	m_sdbSizer1 = new wxStdDialogButtonSizer();
	m_sdbSizer1Apply = new wxButton( this, wxID_APPLY );
	m_sdbSizer1->AddButton( m_sdbSizer1Apply );
	m_sdbSizer1Cancel = new wxButton( this, wxID_CANCEL );
	m_sdbSizer1->AddButton( m_sdbSizer1Cancel );
	m_sdbSizer1->Realize();

	bSizer4->Add( m_sdbSizer1, 1, wxALIGN_CENTER_HORIZONTAL, 5 );


	this->SetSizer( bSizer4 );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	m_sdbSizer1Apply->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( DlgEnterVidNum::onDlgBtnEnterVidNumApply ), NULL, this );
	m_sdbSizer1Cancel->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( DlgEnterVidNum::onDlgBtnEnterVidNumCancel ), NULL, this );
}

DlgEnterVidNum::~DlgEnterVidNum()
{
	// Disconnect Events
	m_sdbSizer1Apply->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( DlgEnterVidNum::onDlgBtnEnterVidNumApply ), NULL, this );
	m_sdbSizer1Cancel->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( DlgEnterVidNum::onDlgBtnEnterVidNumCancel ), NULL, this );

}

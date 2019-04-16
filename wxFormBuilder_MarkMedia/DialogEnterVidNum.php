<?php

/*
* PHP code generated with wxFormBuilder (version Oct 26 2018)
* http://www.wxformbuilder.org/
*
* PLEASE DO *NOT* EDIT THIS FILE!
*/

/*
 * Class DlgEnterVidNum
 */

class DlgEnterVidNum extends wxDialog {

	function __construct( $parent=null ){
		parent::__construct( $parent, wxID_ANY, wxEmptyString, wxDefaultPosition, new wxSize( 474,187 ), wxDEFAULT_DIALOG_STYLE );

		$this->SetSizeHints( wxDefaultSize, wxDefaultSize );

		$bSizer4 = new wxBoxSizer( wxVERTICAL );

		$this->m_staticTextDlgEnterVidNum = new wxStaticText( $this, wxID_ANY, _("Enter last 5 digits below. Example:  for IMG_P085 enter _P085, for MVI0C123 enter 0C123"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
		$this->m_staticTextDlgEnterVidNum->Wrap( -1 );

		$bSizer4->Add( $this->m_staticTextDlgEnterVidNum, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

		$this->m_textCtrl2 = new wxTextCtrl( $this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
		$bSizer4->Add( $this->m_textCtrl2, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

		$this->m_staticTextDlgEnterVidNumStatus = new wxStaticText( $this, wxID_ANY, _("Status: waiting for entry..."), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
		$this->m_staticTextDlgEnterVidNumStatus->Wrap( -1 );

		$bSizer4->Add( $this->m_staticTextDlgEnterVidNumStatus, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

		$m_sdbSizer1 = new wxStdDialogButtonSizer();
		$this->m_sdbSizer1Apply = new wxButton( $this, wxID_APPLY );
		$m_sdbSizer1->AddButton( $this->m_sdbSizer1Apply );
		$this->m_sdbSizer1Cancel = new wxButton( $this, wxID_CANCEL );
		$m_sdbSizer1->AddButton( $this->m_sdbSizer1Cancel );
		$m_sdbSizer1->Realize();

		$bSizer4->Add( $m_sdbSizer1, 1, wxALIGN_CENTER_HORIZONTAL, 5 );


		$this->SetSizer( $bSizer4 );
		$this->Layout();

		$this->Centre( wxBOTH );

		// Connect Events
		$this->m_sdbSizer1Apply->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onDlgBtnEnterVidNumApply") );
		$this->m_sdbSizer1Cancel->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onDlgBtnEnterVidNumCancel") );
	}


	function __destruct( ){
	}


	// Virtual event handlers, overide them in your derived class
	function onDlgBtnEnterVidNumApply( $event ){
		$event->Skip();
	}

	function onDlgBtnEnterVidNumCancel( $event ){
		$event->Skip();
	}

}

?>

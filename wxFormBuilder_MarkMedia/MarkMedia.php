<?php

/*
* PHP code generated with wxFormBuilder (version Oct 26 2018)
* http://www.wxformbuilder.org/
*
* PLEASE DO *NOT* EDIT THIS FILE!
*/

/*
 * Class MainFrame
 */

class MainFrame extends wxFrame {

	function __construct( $parent=null ){
		parent::__construct ( $parent, wxID_ANY, wxEmptyString, wxDefaultPosition, new wxSize( 1245,1193 ), wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		$this->SetSizeHints( wxDefaultSize, wxDefaultSize );

		$bSizerFrame = new wxBoxSizer( wxVERTICAL );

		$this->m_panel1 = new wxPanel( $this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
		$this->m_panel1->SetToolTip( "Video is displayed here" );

		$bSizerPanel = new wxBoxSizer( wxVERTICAL );

		$this->m_staticTextStatus = new wxStaticText( $this->m_panel1, wxID_ANY, "Status: ...", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_staticTextStatus->Wrap( -1 );

		$this->m_staticTextStatus->SetToolTip( "Status is displayed here" );

		$bSizerPanel->Add( $this->m_staticTextStatus, 0, wxALL|wxEXPAND, 5 );

		$this->m_notebookMediaCtrl = new wxNotebook( $this->m_panel1, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_notebookMediaCtrl->SetMinSize( new wxSize( 800,800 ) );


		$bSizerPanel->Add( $this->m_notebookMediaCtrl, 1, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

		$bSizer3 = new wxBoxSizer( wxHORIZONTAL );

		$m_radioBox1Choices = array( "Pix", "Movies" );
		$this->m_radioBox1 = new wxRadioBox( $this->m_panel1, wxID_ANY, "wxRadioBox", wxDefaultPosition, wxDefaultSize, $m_radioBox1Choices, 2, wxRA_SPECIFY_COLS );
		$this->m_radioBox1->SetSelection( 0 );
		$bSizer3->Add( $this->m_radioBox1, 0, wxALL, 5 );

		$this->m_buttonPrev10 = new wxButton( $this->m_panel1, wxID_ANY, "|<<<", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonPrev10->SetToolTip( "10 Previous" );

		$bSizer3->Add( $this->m_buttonPrev10, 0, wxALL, 5 );

		$this->m_buttonPrev = new wxButton( $this->m_panel1, wxID_ANY, "|<", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonPrev->SetToolTip( "Previous" );

		$bSizer3->Add( $this->m_buttonPrev, 0, wxALL, 5 );

		$this->m_buttonPlay = new wxButton( $this->m_panel1, wxID_ANY, ">", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonPlay->SetToolTip( "Play" );

		$bSizer3->Add( $this->m_buttonPlay, 0, wxALL, 5 );

		$this->m_buttonStop = new wxButton( $this->m_panel1, wxID_ANY, ">][<", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonStop->SetToolTip( "Stop" );

		$bSizer3->Add( $this->m_buttonStop, 0, wxALL, 5 );

		$this->m_buttonNext = new wxButton( $this->m_panel1, wxID_ANY, ">|", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonNext->SetToolTip( "Next" );

		$bSizer3->Add( $this->m_buttonNext, 0, wxALL, 5 );

		$this->m_buttonNext10 = new wxButton( $this->m_panel1, wxID_ANY, ">>>|", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonNext10->SetToolTip( "10 Next" );

		$bSizer3->Add( $this->m_buttonNext10, 0, wxALL, 5 );

		$this->m_buttonEnterVidNum = new wxButton( $this->m_panel1, wxID_ANY, "Enter...", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonEnterVidNum->SetToolTip( "Enter video number" );

		$bSizer3->Add( $this->m_buttonEnterVidNum, 0, wxALL, 5 );

		$this->m_buttonLouder = new wxButton( $this->m_panel1, wxID_ANY, "^^^", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonLouder->SetToolTip( "Louder" );

		$bSizer3->Add( $this->m_buttonLouder, 0, wxALL, 5 );

		$this->m_buttonSofter = new wxButton( $this->m_panel1, wxID_ANY, "vvv", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonSofter->SetToolTip( "Softer" );

		$bSizer3->Add( $this->m_buttonSofter, 0, wxALL, 5 );


		$bSizerPanel->Add( $bSizer3, 0, wxALIGN_CENTER_HORIZONTAL, 5 );

		$this->m_textCtrl1 = new wxTextCtrl( $this->m_panel1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_textCtrl1->SetToolTip( "Enter/Edit Comment" );

		$bSizerPanel->Add( $this->m_textCtrl1, 0, wxALL|wxEXPAND, 5 );

		$m_listBoxVidCommentsChoices = array();
		$this->m_listBoxVidComments = new wxListBox( $this->m_panel1, wxID_ANY, wxDefaultPosition, wxDefaultSize, $m_listBoxVidCommentsChoices, wxLB_ALWAYS_SB|wxLB_HSCROLL|wxLB_SINGLE );
		$this->m_listBoxVidComments->SetToolTip( "List of existing Video txt comments" );
		$this->m_listBoxVidComments->SetMinSize( new wxSize( -1,300 ) );

		$bSizerPanel->Add( $this->m_listBoxVidComments, 0, wxALL|wxEXPAND, 5 );


		$this->m_panel1->SetSizer( $bSizerPanel );
		$this->m_panel1->Layout();
		$bSizerPanel->Fit( $this->m_panel1 );
		$bSizerFrame->Add( $this->m_panel1, 1, wxEXPAND | wxALL, 5 );


		$this->SetSizer( $bSizerFrame );
		$this->Layout();
		$this->m_menubarMainFrame = new wxMenuBar( 0 );
		$this->m_menuFile = new wxMenu();
		$this->m_menuItemFileOpen = new wxMenuItem( $this->m_menuFile, wxID_ANY, "Open Video txt...", wxEmptyString, wxITEM_NORMAL );
		$this->m_menuFile->Append( $this->m_menuItemFileOpen );

		$this->m_menuItemFileSave = new wxMenuItem( $this->m_menuFile, wxID_ANY, "Save Video txt...", wxEmptyString, wxITEM_NORMAL );
		$this->m_menuFile->Append( $this->m_menuItemFileSave );

		$this->m_menuItemFileSaveAs = new wxMenuItem( $this->m_menuFile, wxID_ANY, "Save As Video txt...", wxEmptyString, wxITEM_NORMAL );
		$this->m_menuFile->Append( $this->m_menuItemFileSaveAs );

		$this->m_menubarMainFrame->Append( $this->m_menuFile, "File" );

		$this->m_menuHelp = new wxMenu();
		$this->m_menuItemHelpAbout = new wxMenuItem( $this->m_menuHelp, wxID_ANY, "About...", wxEmptyString, wxITEM_NORMAL );
		$this->m_menuHelp->Append( $this->m_menuItemHelpAbout );

		$this->m_menubarMainFrame->Append( $this->m_menuHelp, "Help" );

		$this->SetMenuBar( $this->m_menubarMainFrame );


		$this->Centre( wxBOTH );

		// Connect Events
		$this->m_buttonPrev10->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnPrev10") );
		$this->m_buttonPrev->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnPrev") );
		$this->m_buttonPlay->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnPlay") );
		$this->m_buttonStop->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnStop") );
		$this->m_buttonNext->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnNext") );
		$this->m_buttonNext10->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnNext10") );
		$this->m_buttonEnterVidNum->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnEnterVidNum") );
		$this->m_buttonLouder->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnLouder") );
		$this->m_buttonSofter->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnSofter") );
		$this->m_listBoxVidComments->Connect( wxEVT_COMMAND_LISTBOX_SELECTED, array($this, "onLBoxVidComments") );
		$this->m_listBoxVidComments->Connect( wxEVT_COMMAND_LISTBOX_DOUBLECLICKED, array($this, "onListBoxDClickVidComments") );
		$this->Connect( $this->m_menuItemFileOpen->GetId(), wxEVT_COMMAND_MENU_SELECTED, array($this, "OnFileOpen") );
		$this->Connect( $this->m_menuItemFileSave->GetId(), wxEVT_COMMAND_MENU_SELECTED, array($this, "onFileSave") );
		$this->Connect( $this->m_menuItemFileSaveAs->GetId(), wxEVT_COMMAND_MENU_SELECTED, array($this, "onFileSaveAs") );
		$this->Connect( $this->m_menuItemHelpAbout->GetId(), wxEVT_COMMAND_MENU_SELECTED, array($this, "onHelpAbout") );
	}


	function __destruct( ){
	}


	// Virtual event handlers, overide them in your derived class
	function onBtnPrev10( $event ){
		$event->Skip();
	}

	function onBtnPrev( $event ){
		$event->Skip();
	}

	function onBtnPlay( $event ){
		$event->Skip();
	}

	function onBtnStop( $event ){
		$event->Skip();
	}

	function onBtnNext( $event ){
		$event->Skip();
	}

	function onBtnNext10( $event ){
		$event->Skip();
	}

	function onBtnEnterVidNum( $event ){
		$event->Skip();
	}

	function onBtnLouder( $event ){
		$event->Skip();
	}

	function onBtnSofter( $event ){
		$event->Skip();
	}

	function onLBoxVidComments( $event ){
		$event->Skip();
	}

	function onListBoxDClickVidComments( $event ){
		$event->Skip();
	}

	function OnFileOpen( $event ){
		$event->Skip();
	}

	function onFileSave( $event ){
		$event->Skip();
	}

	function onFileSaveAs( $event ){
		$event->Skip();
	}

	function onHelpAbout( $event ){
		$event->Skip();
	}

}

?>

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

		$this->m_buttonPrevfile = new wxButton( $this->m_panel1, wxID_ANY, "|<textfile", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonPrevfile->SetToolTip( "Previous in text file" );

		$bSizer3->Add( $this->m_buttonPrevfile, 0, wxALL, 5 );

		$this->m_buttonPrev = new wxButton( $this->m_panel1, wxID_ANY, "|<", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonPrev->SetToolTip( "Previous media file" );

		$bSizer3->Add( $this->m_buttonPrev, 0, wxALL, 5 );

		$this->m_buttonPlay = new wxButton( $this->m_panel1, wxID_ANY, ">", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonPlay->SetToolTip( "Play" );

		$bSizer3->Add( $this->m_buttonPlay, 0, wxALL, 5 );

		$this->m_buttonPause = new wxButton( $this->m_panel1, wxID_ANY, ">][<", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonPause->SetToolTip( "Pause" );

		$bSizer3->Add( $this->m_buttonPause, 0, wxALL, 5 );

		$this->m_buttonNext = new wxButton( $this->m_panel1, wxID_ANY, ">|", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonNext->SetToolTip( "Next media file" );

		$bSizer3->Add( $this->m_buttonNext, 0, wxALL, 5 );

		$this->m_buttonNextFile = new wxButton( $this->m_panel1, wxID_ANY, "textfile>|", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonNextFile->SetToolTip( "Next in text file" );

		$bSizer3->Add( $this->m_buttonNextFile, 0, wxALL, 5 );

		$this->m_buttonEnterVidNum = new wxButton( $this->m_panel1, wxID_ANY, "Enter #...", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonEnterVidNum->SetToolTip( "Enter media number" );

		$bSizer3->Add( $this->m_buttonEnterVidNum, 0, wxALL, 5 );

		$this->m_buttonLouder = new wxButton( $this->m_panel1, wxID_ANY, "Louder", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonLouder->SetToolTip( "Louder" );

		$bSizer3->Add( $this->m_buttonLouder, 0, wxALL, 5 );

		$this->m_buttonSofter = new wxButton( $this->m_panel1, wxID_ANY, "Softer", wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_buttonSofter->SetToolTip( "Softer" );

		$bSizer3->Add( $this->m_buttonSofter, 0, wxALL, 5 );


		$bSizerPanel->Add( $bSizer3, 0, wxALIGN_CENTER_HORIZONTAL, 5 );

		$this->m_textCtrl1 = new wxTextCtrl( $this->m_panel1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
		$this->m_textCtrl1->SetToolTip( "Enter/Edit Comment" );

		$bSizerPanel->Add( $this->m_textCtrl1, 0, wxALL|wxEXPAND, 5 );

		$this->m_listCtrlVidComments = new wxListCtrl( $this->m_panel1, wxID_ANY, wxDefaultPosition, new wxSize( -1,-1 ), wxLC_REPORT|wxBORDER_SUNKEN );
		$this->m_listCtrlVidComments->SetToolTip( "List of existing Video txt comments" );
		$this->m_listCtrlVidComments->SetMinSize( new wxSize( -1,300 ) );

		$bSizerPanel->Add( $this->m_listCtrlVidComments, 0, wxALL|wxEXPAND, 5 );


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

		$this->m_menuItemQuit = new wxMenuItem( $this->m_menuFile, wxID_ANY, "Quit without save...", wxEmptyString, wxITEM_NORMAL );
		$this->m_menuFile->Append( $this->m_menuItemQuit );

		$this->m_menuItemeExit = new wxMenuItem( $this->m_menuFile, wxID_ANY, "Exit and save", wxEmptyString, wxITEM_NORMAL );
		$this->m_menuFile->Append( $this->m_menuItemeExit );

		$this->m_menubarMainFrame->Append( $this->m_menuFile, "File" );

		$this->m_menuHelp = new wxMenu();
		$this->m_menuItemHelpAbout = new wxMenuItem( $this->m_menuHelp, wxID_ANY, "About...", wxEmptyString, wxITEM_NORMAL );
		$this->m_menuHelp->Append( $this->m_menuItemHelpAbout );

		$this->m_menubarMainFrame->Append( $this->m_menuHelp, "Help" );

		$this->SetMenuBar( $this->m_menubarMainFrame );

		$this->m_timerMedia = new wxTimer();
		$this->m_timerMedia->SetOwner( $this, wxID_ANY );
		$this->m_timerMedia->Start( 125 );


		$this->Centre( wxBOTH );

		// Connect Events
		$this->m_buttonPrevfile->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnPrevFile") );
		$this->m_buttonPrev->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnPrev") );
		$this->m_buttonPlay->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnPlay") );
		$this->m_buttonPause->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnPause") );
		$this->m_buttonNext->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnNext") );
		$this->m_buttonNextFile->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnNextFile") );
		$this->m_buttonEnterVidNum->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnEnterVidNum") );
		$this->m_buttonLouder->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnLouder") );
		$this->m_buttonSofter->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "onBtnSofter") );
		$this->m_listCtrlVidComments->Connect( wxEVT_COMMAND_LIST_ITEM_ACTIVATED, array($this, "onListCtrlActivated") );
		$this->Connect( $this->m_menuItemFileOpen->GetId(), wxEVT_COMMAND_MENU_SELECTED, array($this, "OnFileOpen") );
		$this->Connect( $this->m_menuItemFileSave->GetId(), wxEVT_COMMAND_MENU_SELECTED, array($this, "onFileSave") );
		$this->Connect( $this->m_menuItemFileSaveAs->GetId(), wxEVT_COMMAND_MENU_SELECTED, array($this, "onFileSaveAs") );
		$this->Connect( $this->m_menuItemQuit->GetId(), wxEVT_COMMAND_MENU_SELECTED, array($this, "OnFileQuit") );
		$this->Connect( $this->m_menuItemeExit->GetId(), wxEVT_COMMAND_MENU_SELECTED, array($this, "OnFileExit") );
		$this->Connect( $this->m_menuItemHelpAbout->GetId(), wxEVT_COMMAND_MENU_SELECTED, array($this, "onHelpAbout") );
		$this->Connect( wxID_ANY, wxEVT_TIMER, array($this, "onTimerMedia") );
	}


	function __destruct( ){
	}


	// Virtual event handlers, overide them in your derived class
	function onBtnPrevFile( $event ){
		$event->Skip();
	}

	function onBtnPrev( $event ){
		$event->Skip();
	}

	function onBtnPlay( $event ){
		$event->Skip();
	}

	function onBtnPause( $event ){
		$event->Skip();
	}

	function onBtnNext( $event ){
		$event->Skip();
	}

	function onBtnNextFile( $event ){
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

	function onListCtrlActivated( $event ){
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

	function OnFileQuit( $event ){
		$event->Skip();
	}

	function OnFileExit( $event ){
		$event->Skip();
	}

	function onHelpAbout( $event ){
		$event->Skip();
	}

	function onTimerMedia( $event ){
		$event->Skip();
	}

}

?>

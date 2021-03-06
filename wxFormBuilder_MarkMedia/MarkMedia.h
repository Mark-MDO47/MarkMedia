///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#pragma once

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/notebook.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/button.h>
#include <wx/sizer.h>
#include <wx/textctrl.h>
#include <wx/listctrl.h>
#include <wx/panel.h>
#include <wx/menu.h>
#include <wx/timer.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class MainFrame
///////////////////////////////////////////////////////////////////////////////
class MainFrame : public wxFrame
{
	private:

	protected:
		wxPanel* m_panel1;
		wxStaticText* m_staticTextStatus;
		wxNotebook* m_notebookMediaCtrl;
		wxButton* m_buttonPrevfile;
		wxButton* m_buttonPrev;
		wxButton* m_buttonPlay;
		wxButton* m_buttonPause;
		wxButton* m_buttonNext;
		wxButton* m_buttonNextFile;
		wxButton* m_buttonEnterVidNum;
		wxButton* m_buttonLouder;
		wxButton* m_buttonSofter;
		wxTextCtrl* m_textCtrlEntry;
		wxListCtrl* m_listCtrlVidComments;
		wxMenuBar* m_menubarMainFrame;
		wxMenu* m_menuFile;
		wxMenu* m_menuHelp;
		wxTimer m_timerMedia;

		// Virtual event handlers, overide them in your derived class
		virtual void onBtnPrevFile( wxCommandEvent& event ) { event.Skip(); }
		virtual void onBtnPrev( wxCommandEvent& event ) { event.Skip(); }
		virtual void onBtnPlay( wxCommandEvent& event ) { event.Skip(); }
		virtual void onBtnPause( wxCommandEvent& event ) { event.Skip(); }
		virtual void onBtnNext( wxCommandEvent& event ) { event.Skip(); }
		virtual void onBtnNextFile( wxCommandEvent& event ) { event.Skip(); }
		virtual void onBtnEnterVidNum( wxCommandEvent& event ) { event.Skip(); }
		virtual void onBtnLouder( wxCommandEvent& event ) { event.Skip(); }
		virtual void onBtnSofter( wxCommandEvent& event ) { event.Skip(); }
		virtual void onTextCtrlEntry( wxCommandEvent& event ) { event.Skip(); }
		virtual void onListCtrlActivated( wxListEvent& event ) { event.Skip(); }
		virtual void OnFileOpen( wxCommandEvent& event ) { event.Skip(); }
		virtual void onFileSave( wxCommandEvent& event ) { event.Skip(); }
		virtual void onFileSaveAs( wxCommandEvent& event ) { event.Skip(); }
		virtual void OnFileQuit( wxCommandEvent& event ) { event.Skip(); }
		virtual void OnFileExit( wxCommandEvent& event ) { event.Skip(); }
		virtual void onHelpAbout( wxCommandEvent& event ) { event.Skip(); }
		virtual void onTimerMedia( wxTimerEvent& event ) { event.Skip(); }


	public:

		MainFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 1245,1193 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~MainFrame();

};


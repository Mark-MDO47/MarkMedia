///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#pragma once

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/intl.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/sizer.h>
#include <wx/button.h>
#include <wx/dialog.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class DlgEnterVidNum
///////////////////////////////////////////////////////////////////////////////
class DlgEnterVidNum : public wxDialog
{
	private:

	protected:
		wxStaticText* m_staticTextDlgEnterVidNum;
		wxTextCtrl* m_textCtrl2;
		wxStaticText* m_staticTextDlgEnterVidNumStatus;
		wxStdDialogButtonSizer* m_sdbSizer1;
		wxButton* m_sdbSizer1Apply;
		wxButton* m_sdbSizer1Cancel;

		// Virtual event handlers, overide them in your derived class
		virtual void onDlgBtnEnterVidNumApply( wxCommandEvent& event ) { event.Skip(); }
		virtual void onDlgBtnEnterVidNumCancel( wxCommandEvent& event ) { event.Skip(); }


	public:

		DlgEnterVidNum( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 474,187 ), long style = wxDEFAULT_DIALOG_STYLE );
		~DlgEnterVidNum();

};


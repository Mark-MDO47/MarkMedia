
        # inserted by aftercopyfilefrom to be copied after "wx.Frame.__init__"
        self.m_absRunPath = absRunPath # absolute path we were run from
        self.m_txtFilePath = "UNKNOWN" # absolute path to open text file
        self.m_txtFileLines = []       # lines for open text file, stripped
        self.m_txtFileIdx = -1         # which line for open text file or -1
        self.m_mediaLength = None # the length of media file; appears to be in milliseconds
        self.m_mediaLoad = False  # True when media load done until timer processes it
        self.m_mediaStartStopDisplay = False # yet another media load flag
        self.m_mediaCurrentWeirdNum = "_0001"
        self.m_mediaMtime = "" # time.ctime(os.path.getmtime(<<thepath>>))
        self.m_infoFile = {}   # filled with max nums, example {'THE_MAX_IMGNUM': 45065, 'THE_MAX_MVINUM': 3441}
        
        self.SetIcon(wx.Icon(os.path.join(self.m_absRunPath,"MadScience_256.ico"))) # Mark: set icon

        # for historical reasons numbering is
        #   leftmost digit: _01...9A...Z
        #   next     digit: 01...9A...Z
        #   next 3  digits: 01...9
        #   (example: _0001 to _Z999 to 00000 to 99999 to 9A000 to 9Z999 to A0000 to ZZ999)
        self.MarksWeirdDigits = [ "_0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "0123456789",
            "0123456789",
            "0123456789"
        ]

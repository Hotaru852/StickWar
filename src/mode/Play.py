import wx


class Play(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.ask_for_input = wx.StaticText(self, label='Enter the number of players in each team')
        self.input = wx.TextCtrl(self)
        self.Start_button = wx.Button(self, label='Start')
        self.Back_button = wx.Button(self, label='Back')
        self.sizer.AddMany([(self.Back_button, 0, wx.ALL | wx.ALIGN_LEFT, 5),
                            (wx.StaticText(self), 0, wx.ALL, 5),
                            (wx.StaticText(self), 0, wx.ALL, 5),
                            (self.ask_for_input, 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (self.input, 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (self.Start_button, 0, wx.ALL | wx.ALIGN_CENTER, 5)])
        self.SetSizer(self.sizer)
        self.SetSize(600, 300)
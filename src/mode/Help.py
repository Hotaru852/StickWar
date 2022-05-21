import wx


class Help(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.Back_button = wx.Button(self, label='Back')
        self.sizer.AddMany([(self.Back_button, 0, wx.ALL | wx.ALIGN_LEFT, 5),
                            (wx.StaticText(self, label='1. Use arrow buttons to move your Stickman'), 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (wx.StaticText(self, label='2. Press 1 in battle to use your Bow'), 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (wx.StaticText(self, label='3. Press 2 in battle to use your Spear'), 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (wx.StaticText(self, label='4. Press 3 in battle to Heal'), 0, wx.ALL | wx.ALIGN_CENTER, 5)])
        self.SetSizer(self.sizer)
        self.SetSize(600, 300)
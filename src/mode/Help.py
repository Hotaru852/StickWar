import wx


#Help panel
class Help(wx.Panel):
    #Khoi chay help panel
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.Back_button = wx.Button(self, label='Back')
        self.sizer.AddMany([(self.Back_button, 0, wx.ALL | wx.ALIGN_LEFT, 5),
                            (wx.StaticText(self, label='1. Press left arrow to move your Stickman to the left'), 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (wx.StaticText(self, label='2. Press right arrow to move your Stickman to the right'), 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (wx.StaticText(self, label='3. Press space to make your Stickman jump'), 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (wx.StaticText(self, label='4. Press 1 to use your Bow'), 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (wx.StaticText(self, label='5. Press 2 to use your Spear'), 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (wx.StaticText(self, label='6. Press 3 to Heal'), 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (wx.StaticText(self, label='7. Click left mouse button to fire when you\'re done aiming'), 0, wx.ALL | wx.ALIGN_CENTER, 5)])
        self.SetSizer(self.sizer)
        self.SetSize(600, 300)
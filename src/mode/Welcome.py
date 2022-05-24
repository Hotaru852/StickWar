import wx


#Welcome panel
class Welcome(wx.Panel):
    #Khoi tao welcome panel
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.Login_button = wx.Button(self, label='Login')
        self.Signup_button = wx.Button(self, label='Signup')
        self.Quit_button = wx.Button(self, label='Quit')
        self.sizer.Add(wx.StaticText(self), 0, wx.ALL, 5)
        self.sizer.Add(wx.StaticText(self, label='Welcome!'), 0, wx.ALL | wx.ALIGN_CENTER, 5)
        self.sizer.Add(wx.StaticText(self), 0, wx.ALL, 5)
        self.sizer.AddMany([(self.Login_button, 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (self.Signup_button, 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (self.Quit_button, 0, wx.ALL | wx.ALIGN_CENTER, 5)])
        self.SetSizer(self.sizer)
        self.SetSize(600, 300)
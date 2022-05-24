import wx


#Login panel
class Login(wx.Panel):
    #Khoi tao login panel
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.Back_button = wx.Button(self, label='Back')
        self.sizer.Add(self.Back_button, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        self.sizer.Add(wx.StaticText(self), 0, wx.ALL, 5)
        self.sizer.Add(wx.StaticText(self), 0, wx.ALL, 5)
        self.input = wx.GridSizer(2, 2, 5, 5)
        self.username_label = wx.StaticText(self, label='Username: ')
        self.username_input = wx.TextCtrl(self)
        self.password_label = wx.StaticText(self, label='Password: ')
        self.password_input = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.input.AddMany([(self.username_label, 0, wx.ALIGN_RIGHT), (self.username_input, 0, wx.ALIGN_LEFT),
                            (self.password_label, 0, wx.ALIGN_RIGHT), (self.password_input, 0, wx.ALIGN_LEFT)])
        self.sizer.Add(self.input, 0, wx.ALL | wx.CENTER, 5)
        self.Login_button = wx.Button(self, label='Login')
        self.sizer.Add(self.Login_button, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(self.sizer)
        self.SetSize(600, 300)
import wx


#Signup panel
class Signup(wx.Panel):
    #Khoi tao signup panel
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.Back_button = wx.Button(self, label='Back')
        self.username_prompt_label = wx.StaticText(self, label='Your Username: ')
        self.password_prompt_label = wx.StaticText(self, label='Your Password: ')
        self.password_confirm_label = wx.StaticText(self, label='Confirm Password: ')
        self.username_prompt_input = wx.TextCtrl(self)
        self.password_prompt_input = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.password_confirm_input = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.Signup_button = wx.Button(self, label='Signup')
        self.input = wx.GridSizer(3, 2, 5, 5)
        self.input.AddMany([(self.username_prompt_label, 0, wx.ALIGN_RIGHT), (self.username_prompt_input, 0, wx.ALIGN_LEFT),
                            (self.password_prompt_label, 0, wx.ALIGN_RIGHT), (self.password_prompt_input, 0, wx.ALIGN_LEFT),
                            (self.password_confirm_label, 0, wx.ALIGN_RIGHT), (self.password_confirm_input, 0, wx.ALIGN_LEFT)])
        self.sizer.Add(self.Back_button, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        self.sizer.Add(wx.StaticText(self), 0, wx.ALL, 5)
        self.sizer.Add(self.input, 0, wx.ALL | wx.ALIGN_CENTER, 5)
        self.sizer.Add(self.Signup_button, 0, wx.ALL | wx.ALIGN_CENTER, 5)
        self.SetSizer(self.sizer)
        self.SetSize(600, 300)
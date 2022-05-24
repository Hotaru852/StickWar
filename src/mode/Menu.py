import wx


#Menu panel
class Menu(wx.Panel):
    #Khoi tao menu panel
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.Username_label = wx.StaticText(self)
        self.sizer.Add(self.Username_label, 0, wx.LEFT, 5)
        self.Logout_button = wx.Button(self, label='Logout')
        self.Help_button = wx.Button(self, label='Help')
        self.Inventory_button = wx.Button(self, label='Items')
        self.Play_button = wx.Button(self, label='Play')
        self.Scores_button = wx.Button(self, label='Scores')
        self.Quit_button = wx.Button(self, label='Quit')
        self.sizer.Add(wx.StaticText(self, label='Menu'), 0, wx.ALL | wx.ALIGN_CENTER, 5)
        self.sizer.AddMany([(self.Play_button, 0, wx.ALL | wx.CENTER, 5),
                            (self.Inventory_button, 0, wx.ALL | wx.CENTER, 5),
                            (self.Scores_button, 0, wx.ALL | wx.CENTER, 5),
                            (self.Help_button, 0, wx.ALL | wx.CENTER, 5),
                            (self.Logout_button, 0, wx.ALL | wx.CENTER, 5),
                            (self.Quit_button, 0, wx.ALL | wx.CENTER, 5)])
        self.SetSizer(self.sizer)
        self.SetSize(600, 300)
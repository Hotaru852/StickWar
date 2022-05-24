import wx


#Result panel
class Result(wx.Panel):
    #Khoi tao result panel
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.Ok_button = wx.Button(self, label='Ok')
        self.winner = None
        self.score = None
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.winner_label = wx.StaticText(self)
        self.score_label = wx.StaticText(self)
        self.coin_label = wx.StaticText(self)
        self.sizer.Add(wx.StaticText(self), 0, wx.ALL, 5)
        self.sizer.Add(wx.StaticText(self), 0, wx.ALL, 5)
        self.sizer.Add(wx.StaticText(self), 0, wx.ALL, 5)
        self.sizer.AddMany([(self.winner_label, 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (self.score_label, 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (self.coin_label, 0, wx.ALL | wx.ALIGN_CENTER, 5),
                            (self.Ok_button, 0, wx.ALL | wx.ALIGN_CENTER, 5)])
        self.SetSizer(self.sizer)
        self.SetSize(600, 300)

    #Khoi tao UI cua result panel
    def initUI(self):
        self.winner_label.SetLabel(self.winner + ' is the winner!')
        self.score_label.SetLabel('Your score is ' + str(self.score))
        self.coin_label.SetLabel('You earned ' + str(self.score) + ' coins')
import wx


def getBitmap(path):
    image = wx.Image(path)
    image.Rescale(65, 65, wx.IMAGE_QUALITY_HIGH)
    return image.ConvertToBitmap()


class Inventory(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.bow_level = None
        self.spear_level = None
        self.potion_level = None
        self.coins = None
        self.Back_button = wx.Button(self, label='Back')
        self.ui = wx.BoxSizer(wx.VERTICAL)
        self.first_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.Coin_display = wx.StaticText(self)
        self.Bow_image = wx.StaticBitmap(self)
        self.Spear_image = wx.StaticBitmap(self)
        self.Potion_image = wx.StaticBitmap(self, -1, getBitmap("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/Potion.png"))
        self.Bow_price_display = wx.StaticText(self, label='Price')
        self.Spear_price_display = wx.StaticText(self, label='Price')
        self.Potion_price_display = wx.StaticText(self, label='Price')
        self.Bow_upgrade_button = wx.Button(self, label='Upgrade')
        self.Bow_upgrade_button.Bind(wx.EVT_BUTTON, self.upgradeBow)
        self.Spear_upgrade_button = wx.Button(self, label='Upgrade')
        self.Spear_upgrade_button.Bind(wx.EVT_BUTTON, self.upgradeSpear)
        self.Potion_upgrade_button = wx.Button(self, label='Upgrade')
        self.Potion_upgrade_button.Bind(wx.EVT_BUTTON, self.upgradePotion)
        self.Bow_level_label = wx.StaticText(self)
        self.Spear_level_label = wx.StaticText(self)
        self.Potion_level_label = wx.StaticText(self)
        self.first_sizer.AddMany([(self.Back_button, 0, wx.LEFT, 5), (self.Coin_display, 0, wx.LEFT, 420)])
        self.second_sizer = wx.GridSizer(4, 3, 5, 5)
        self.second_sizer.AddMany([(self.Bow_image, 0, wx.ALIGN_CENTER), (self.Spear_image, 0, wx.ALIGN_CENTER), (self.Potion_image, 0, wx.ALIGN_CENTER),
                                   (self.Bow_level_label, 0, wx.ALIGN_CENTER), (self.Spear_level_label, 0, wx.ALIGN_CENTER), (self.Potion_level_label, 0, wx.ALIGN_CENTER),
                                   (self.Bow_price_display, 0, wx.ALIGN_CENTER), (self.Spear_price_display, 0, wx.ALIGN_CENTER), (self.Potion_price_display, 0, wx.ALIGN_CENTER),
                                   (self.Bow_upgrade_button, 0, wx.ALIGN_CENTER), (self.Spear_upgrade_button, 0, wx.ALIGN_CENTER),(self.Potion_upgrade_button, 0, wx.ALIGN_CENTER)])
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.AddMany([(self.first_sizer, 0, wx.ALL | wx.EXPAND, 5),
                            (self.second_sizer, 0, wx.ALL | wx.EXPAND, 5)])
        self.SetSizer(self.sizer)
        self.SetSize(600, 300)

    def initUI(self):
        self.Bow_image.SetBitmap(getBitmap("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/Bow level " + str(self.bow_level) + ".png"))
        self.Spear_image.SetBitmap(getBitmap("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/Spear level " + str(self.spear_level) + ".png"))
        self.Bow_price_display.SetLabel('Price: ' + str(100 * self.bow_level))
        self.Bow_level_label.SetLabel('Level: ' + str(self.bow_level))
        self.Spear_price_display.SetLabel('Price: ' + str(100 * self.spear_level))
        self.Spear_level_label.SetLabel('Level: ' + str(self.spear_level))
        self.Potion_price_display.SetLabel('Price: ' + str(100 * self.potion_level))
        self.Potion_level_label.SetLabel('Level: ' + str(self.potion_level))
        self.Coin_display.SetLabel('Coins: ' + str(self.coins))

    def upgradeBow(self, e):
        if self.bow_level <= 3 and self.coins >= self.bow_level * 100:
            self.coins -= 100 * self.bow_level
            self.Coin_display.SetLabel('Coins: ' + str(self.coins))
            self.bow_level += 1
            self.Bow_image.SetBitmap(getBitmap("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/Bow level " + str(self.bow_level) + ".png"))
            self.Bow_price_display.SetLabel('Price: ' + str(100 * self.bow_level))
            self.Bow_level_label.SetLabel('Level: ' + str(self.bow_level))
        else:
            wx.MessageBox('Can\'t upgrade', 'Error', wx.OK | wx.ICON_ERROR)

    def upgradeSpear(self, e):
        if self.spear_level <= 3 and self.coins >= self.spear_level * 100:
            self.coins -= 100 * self.spear_level
            self.Coin_display.SetLabel('Coins: ' + str(self.coins))
            self.spear_level += 1
            self.Spear_image.SetBitmap(getBitmap("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/Spear level " + str(self.spear_level) + ".png"))
            self.Spear_price_display.SetLabel('Price: ' + str(100 * self.spear_level))
            self.Spear_level_label.SetLabel('Level: ' + str(self.spear_level))
        else:
            wx.MessageBox('Can\'t upgrade', 'Error', wx.OK | wx.ICON_ERROR)

    def upgradePotion(self, e):
        if self.potion_level <= 3 and self.coins >= self.potion_level * 100:
            self.coins -= 100 * self.potion_level
            self.Coin_display.SetLabel('Coins: ' + str(self.coins))
            self.potion_level += 1
            self.Potion_price_display.SetLabel('Price: ' + str(100 * self.potion_level))
            self.Potion_level_label.SetLabel('Level: ' + str(self.potion_level))
        else:
            wx.MessageBox('Can\'t upgrade', 'Error', wx.OK | wx.ICON_ERROR)
import pygame.display
import wx
import sys
from src.config import *
from src.mode.Inventory import Inventory
from src.mode.Help import Help
from src.mode.Login import Login
from src.mode.Menu import Menu
from src.mode.Play import Play
from src.mode.Login_Signup import Login_Signup
from src.mode.Signup import Signup
from src.mode.Result import Result
from src.my_class.file_manager import file_manager
from play import Play_Scene

players = None
window = wx.App()
current_account = None
logging_out = False
users = None


def switch_display():
    window.ExitMainLoop()
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    play_scene = Play_Scene()
    play_scene.bow_level = control.inventory_panel.bow_level
    play_scene.spear_level = control.inventory_panel.spear_level
    play_scene.potion_level = control.inventory_panel.potion_level
    play_scene.setup(players)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        play_scene.draw(screen)
        play_scene.update(events)
        if not play_scene.active():
            break
        pygame.display.flip()
        clock.tick(FPS)
    control.result_panel.winner = play_scene.winner
    control.result_panel.score = play_scene.score
    control.inventory_panel.coins += play_scene.score
    pygame.display.quit()
    pygame.quit()
    control.result_panel.initUI()
    control.signup_panel.Hide()
    control.menu_panel.Hide()
    control.inventory_panel.Hide()
    control.help_panel.Hide()
    control.login_panel.Hide()
    control.play_panel.Hide()
    control.login_signup_panel.Hide()
    control.result_panel.Show()
    control.Layout()
    window.MainLoop()


class ModeControl(wx.Frame):
    def __init__(self, parent, title):
        super(ModeControl, self).__init__(parent, title=title)
        self.sizer = wx.BoxSizer()
        self.menu_panel = Menu(self)
        self.inventory_panel = Inventory(self)
        self.help_panel = Help(self)
        self.login_panel = Login(self)
        self.play_panel = Play(self)
        self.login_signup_panel = Login_Signup(self)
        self.signup_panel = Signup(self)
        self.result_panel = Result(self)
        self.sizer.AddMany([(self.menu_panel, 1, wx.EXPAND, 0),
                            (self.inventory_panel, 1, wx.EXPAND, 0),
                            (self.help_panel, 1, wx.EXPAND, 0),
                            (self.login_panel, 1, wx.EXPAND, 0),
                            (self.play_panel, 1, wx.EXPAND, 0),
                            (self.login_signup_panel, 1, wx.EXPAND, 0),
                            (self.signup_panel, 1, wx.EXPAND, 0),
                            (self.result_panel, 1, wx.EXPAND, 0)])
        self.inventory_panel.Back_button.Bind(wx.EVT_BUTTON, self.show_menu_panel)
        self.help_panel.Back_button.Bind(wx.EVT_BUTTON, self.show_menu_panel)
        self.menu_panel.Inventory_button.Bind(wx.EVT_BUTTON, self.show_inventory_panel)
        self.menu_panel.Help_button.Bind(wx.EVT_BUTTON, self.show_help_panel)
        self.menu_panel.Logout_button.Bind(wx.EVT_BUTTON, self.show_login_signup_panel)
        self.login_panel.Login_button.Bind(wx.EVT_BUTTON, self.onLogin)
        self.menu_panel.Quit_button.Bind(wx.EVT_BUTTON, self.exitGame)
        self.menu_panel.Play_button.Bind(wx.EVT_BUTTON, self.show_play_panel)
        self.play_panel.Back_button.Bind(wx.EVT_BUTTON, self.show_menu_panel)
        self.play_panel.Start_button.Bind(wx.EVT_BUTTON, self.switchDisplay)
        self.login_signup_panel.Quit_button.Bind(wx.EVT_BUTTON, self.exitGame)
        self.login_signup_panel.Login_button.Bind(wx.EVT_BUTTON, self.show_login_panel)
        self.login_panel.Back_button.Bind(wx.EVT_BUTTON, self.show_login_signup_panel)
        self.signup_panel.Back_button.Bind(wx.EVT_BUTTON, self.show_login_signup_panel)
        self.login_signup_panel.Signup_button.Bind(wx.EVT_BUTTON, self.show_signup_panel)
        self.signup_panel.Signup_button.Bind(wx.EVT_BUTTON, self.onSignup)
        self.result_panel.Ok_button.Bind(wx.EVT_BUTTON, self.show_menu_panel)
        self.SetSizer(self.sizer)
        self.inventory_panel.Hide()
        self.help_panel.Hide()
        self.menu_panel.Hide()
        self.play_panel.Hide()
        self.login_panel.Hide()
        self.signup_panel.Hide()
        self.result_panel.Hide()
        self.SetSize(600, 300)
        self.Centre()
        self.test = False

    def show_menu_panel(self, e):
        self.signup_panel.Hide()
        self.menu_panel.Show()
        self.inventory_panel.Hide()
        self.help_panel.Hide()
        self.login_panel.Hide()
        self.play_panel.Hide()
        self.login_signup_panel.Hide()
        self.result_panel.Hide()
        self.Layout()

    def show_inventory_panel(self, e):
        self.inventory_panel.initUI()
        self.signup_panel.Hide()
        self.menu_panel.Hide()
        self.inventory_panel.Show()
        self.help_panel.Hide()
        self.login_panel.Hide()
        self.play_panel.Hide()
        self.login_signup_panel.Hide()
        self.result_panel.Hide()
        self.Layout()

    def show_login_panel(self, e):
        self.login_panel.username_input.Clear()
        self.login_panel.password_input.Clear()
        self.signup_panel.Hide()
        self.menu_panel.Hide()
        self.inventory_panel.Hide()
        self.help_panel.Hide()
        self.login_panel.Show()
        self.play_panel.Hide()
        self.login_signup_panel.Hide()
        self.result_panel.Hide()
        self.Layout()

    def show_help_panel(self, e):
        self.signup_panel.Hide()
        self.menu_panel.Hide()
        self.inventory_panel.Hide()
        self.help_panel.Show()
        self.login_panel.Hide()
        self.play_panel.Hide()
        self.login_signup_panel.Hide()
        self.result_panel.Hide()
        self.Layout()

    def show_login_signup_panel(self, e):
        global logging_out
        if logging_out:
            self.save_account()
            logging_out = False
        self.signup_panel.Hide()
        self.menu_panel.Hide()
        self.inventory_panel.Hide()
        self.help_panel.Hide()
        self.login_panel.Hide()
        self.play_panel.Hide()
        self.login_signup_panel.Show()
        self.result_panel.Hide()
        self.Layout()

    def show_play_panel(self, e):
        self.play_panel.input.Clear()
        self.signup_panel.Hide()
        self.menu_panel.Hide()
        self.inventory_panel.Hide()
        self.help_panel.Hide()
        self.login_panel.Hide()
        self.play_panel.Show()
        self.login_signup_panel.Hide()
        self.result_panel.Hide()
        self.Layout()

    def show_signup_panel(self, e):
        self.signup_panel.username_prompt_input.Clear()
        self.signup_panel.password_prompt_input.Clear()
        self.signup_panel.password_confirm_input.Clear()
        self.signup_panel.Show()
        self.menu_panel.Hide()
        self.inventory_panel.Hide()
        self.help_panel.Hide()
        self.login_panel.Hide()
        self.play_panel.Hide()
        self.login_signup_panel.Hide()
        self.result_panel.Hide()
        self.Layout()

    # noinspection PyUnresolvedReferences
    def save_account(self):
        fm = file_manager()
        users[current_account][2] = self.inventory_panel.bow_level
        users[current_account][3] = self.inventory_panel.spear_level
        users[current_account][4] = self.inventory_panel.potion_level
        users[current_account][5] = self.inventory_panel.coins
        fm.save(users)

    def switchDisplay(self, e):
        check = str(self.play_panel.input.GetValue())
        if check == '':
            wx.MessageBox('Please fill in the field', 'Error', wx.OK | wx.ICON_ERROR)
        else:
            if not check.isnumeric():
                wx.MessageBox('Please enter a number', 'Error', wx.OK | wx.ICON_ERROR)
                self.play_panel.input.Clear()
            else:
                global players
                players = int(check)
                switch_display()

    def exitGame(self, e):
        self.save_account()
        self.Close()

    def onLogin(self, e):
        username = self.login_panel.username_input.GetValue()
        password = self.login_panel.password_input.GetValue()
        fm = file_manager()
        accounts = fm.load()
        if username == '' or password == '':
            wx.MessageBox('Please fill in all the fields', 'Error', wx.OK | wx.ICON_ERROR)
        else:
            for account in accounts:
                if username == account[0] and password == account[1]:
                    wx.MessageBox('Login successful!', 'Congratulations!', wx.OK | wx.ICON_NONE)
                    self.login_panel.username_input.Clear()
                    self.login_panel.password_input.Clear()
                    self.menu_panel.Username_label.SetLabel('User: ' + username)
                    self.menu_panel.Show()
                    self.login_panel.Hide()
                    self.inventory_panel.bow_level = int(account[2])
                    self.inventory_panel.spear_level = int(account[3])
                    self.inventory_panel.potion_level = int(account[4])
                    self.inventory_panel.coins = int(account[5])
                    global current_account, users, logging_out
                    logging_out = True
                    users = accounts
                    current_account = accounts.index(account)
                    return
                elif account == accounts[len(accounts) - 1]:
                    wx.MessageBox('Wrong username or password', 'Error', wx.OK | wx.ICON_ERROR)
                    self.login_panel.username_input.Clear()
                    self.login_panel.password_input.Clear()

    def onSignup(self, e):
        username = self.signup_panel.username_prompt_input.GetValue()
        password = self.signup_panel.password_prompt_input.GetValue()
        confirm_password = self.signup_panel.password_confirm_input.GetValue()
        if username == '' or password == '' or confirm_password == '':
            wx.MessageBox('Please fill in all the fields', 'Error', wx.OK | wx.ICON_ERROR)
        elif password != confirm_password:
            wx.MessageBox('Password doesn\'t match', 'Error', wx.OK | wx.ICON_ERROR)
            self.signup_panel.username_prompt_input.Clear()
            self.signup_panel.password_prompt_input.Clear()
            self.signup_panel.password_confirm_input.Clear()
        else:
            fm = file_manager()
            accounts = fm.load()
            for account in accounts:
                if username == account[0]:
                    wx.MessageBox('User already exist', 'Error', wx.OK | wx.ICON_ERROR)
                    self.signup_panel.username_prompt_input.Clear()
                    self.signup_panel.password_prompt_input.Clear()
                    self.signup_panel.password_confirm_input.Clear()
                elif account == accounts[len(accounts) - 1]:
                    accounts.append([username, password, 1, 1, 1, 0, []])
                    fm.save(accounts)
                    wx.MessageBox('Signup successful!', 'Congratulations!', wx.OK | wx.ICON_NONE)
                    self.signup_panel.username_prompt_input.Clear()
                    self.signup_panel.password_prompt_input.Clear()
                    self.signup_panel.password_confirm_input.Clear()
                    return


control = ModeControl(None, 'GUI')
control.Show()
window.MainLoop()
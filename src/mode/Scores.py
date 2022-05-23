import wx
import wx.lib.mixins.listctrl as listmix


class Scores(wx.Panel, listmix.ColumnSorterMixin):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.Back_button = wx.Button(self, label='Back')
        self.scores_list = wx.ListCtrl(self, 0, style=wx.LC_REPORT)
        self.scores = None
        self.itemDataMap = None
        self.sizer.AddMany([(self.Back_button, 0, wx.ALL | wx.ALIGN_LEFT, 5),
                            (self.scores_list, 1, wx.ALL | wx.EXPAND, 5)])
        listmix.ColumnSorterMixin.__init__(self, 2)
        self.SetSizer(self.sizer)
        self.SetSize(600, 300)

    def iniUI(self):
        data = []
        self.scores_list.ClearAll()
        self.scores_list.InsertColumn(0, 'Score', wx.LIST_FORMAT_CENTER)
        self.scores_list.InsertColumn(1, 'Date\\Time ▲', wx.LIST_FORMAT_CENTER)
        self.scores_list.SetColumnWidth(0, 295)
        self.scores_list.SetColumnWidth(1, 295)
        for entry in self.scores:
            score, date, time = entry.split('\'')
            data.append((score, date + ' ' + time))
        data = {data.index(entry) + 1: entry for entry in data}
        self.itemDataMap = data
        for key, entry in data.items():
            index = self.scores_list.InsertItem(self.scores_list.GetItemCount(), entry[0])
            self.scores_list.SetItem(index, 1, entry[1])
            self.scores_list.SetItemData(index, key)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.onColClick, self.scores_list)

    def onColClick(self, e):
        count = self.scores_list.GetItemCount()
        col1_data, col2_data = [], []
        for row in range(count):
            item1 = self.scores_list.GetItem(row, 0)
            item2 = self.scores_list.GetItem(row, 1)
            col1_data.append(item1.GetText())
            col2_data.append(item2.GetText())
        col1_ascending, col1_descending, col2_ascending, col2_descending = [True, True, True, True]
        for index in range(count - 1):
            if col1_data[index] > col1_data[index+1]:
                col1_ascending = False
            elif col1_data[index] < col1_data[index+1]:
                col1_descending = False
            if col2_data[index] > col2_data[index + 1]:
                col2_ascending = False
            elif col2_data[index] < col2_data[index + 1]:
                col2_descending = False
        col1 = self.scores_list.GetColumn(0)
        col2 = self.scores_list.GetColumn(1)
        if col1_ascending:
            col1.SetText('Score ▲')
        if col1_descending:
            col1.SetText('Score ▼')
        if col2_ascending:
            col2.SetText('Date\\Time ▲')
        if col2_descending:
            col2.SetText('Date\\Time ▼')
        if not col1_ascending and not col1_descending:
            col1.SetText('Score')
        if not col2_ascending and not col2_descending:
            col2.SetText('Date\\Time')
        self.scores_list.SetColumn(0, col1)
        self.scores_list.SetColumn(1, col2)

    def GetListCtrl(self):
        return self.scores_list
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"File directory", pos=wx.DefaultPosition,
                          size=wx.Size(645, 284), style=wx.DEFAULT_FRAME_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.Point(-1, -1), wx.DefaultSize, 0)
        self.m_textCtrl6.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_textCtrl6.SetMinSize(wx.Size(350, -1))

        fgSizer1.Add(self.m_textCtrl6, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Browse", wx.Point(-1, -1), wx.Size(100, 25), 0)
        fgSizer1.Add(self.m_button3, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        gSizer7 = wx.GridSizer(0, 3, 0, 0)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self.m_button13, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button14 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self.m_button14, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button15 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self.m_button15, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer1.Add(gSizer7, 1, wx.EXPAND, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        fgSizer1.Add(self.m_staticText6, 0, wx.ALL, 5)

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText51 = wx.StaticText(self, wx.ID_ANY, u"Estimation Method", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText51.Wrap(-1)

        fgSizer2.Add(self.m_staticText51, 0, wx.ALL, 5)

        self.m_staticText71 = wx.StaticText(self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)

        fgSizer2.Add(self.m_staticText71, 0, wx.ALL, 5)

        self.m_checkBox1 = wx.CheckBox(self, wx.ID_ANY, u"Standard", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.m_checkBox1, 0, wx.ALL, 5)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Start Date :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        gSizer3.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.m_textCtrl4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer2.Add(gSizer3, 1, wx.EXPAND, 5)

        self.m_checkBox2 = wx.CheckBox(self, wx.ID_ANY, u"Blume", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.m_checkBox2, 0, wx.ALL, 5)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"End Date: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        gSizer4.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        fgSizer2.Add(gSizer4, 1, wx.EXPAND, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, u"Estimate", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.m_button8, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer2, 1, wx.EXPAND, 5)

        gSizer9 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Optimization", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        self.m_staticText3.SetMinSize(wx.Size(100, 25))

        gSizer9.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        gSizer9.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Fixed return: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        gSizer9.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer9.Add(self.m_textCtrl7, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Risk-free rate: ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        gSizer9.Add(self.m_staticText7, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer9.Add(self.m_textCtrl8, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer9.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"Optimize", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer9.Add(self.m_button6, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        fgSizer1.Add(gSizer9, 1, wx.EXPAND, 5)

        bSizer3.Add(fgSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer3)
        self.Layout()
        self.m_statusBar2 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame1(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()
# encoding:utf-8

from healthTextTool01 import *
from function import *

if __name__ == "__main__":
    
    app = wx.App(False)
    frame = ToolFrame(None)
    frame.Show(True)
    app.MainLoop()
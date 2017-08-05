# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ToolFrame
###########################################################################

class ToolFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 811,655 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		mainFrame = wx.FlexGridSizer( 0, 2, 0, 0 )
		mainFrame.SetFlexibleDirection( wx.HORIZONTAL )
		mainFrame.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		left_mainFrame = wx.BoxSizer( wx.VERTICAL )
		
		left_mainFrame.SetMinSize( wx.Size( 100,-1 ) ) 
		self.btn_HealthPath = wx.Button( self, wx.ID_ANY, u"打开文件目录", wx.DefaultPosition, wx.DefaultSize, 0 )
		left_mainFrame.Add( self.btn_HealthPath, 0, wx.ALL, 5 )
		
		self.st_healthTextPath = wx.StaticText( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_healthTextPath.Wrap( -1 )
		left_mainFrame.Add( self.st_healthTextPath, 0, wx.ALL, 5 )
		
		left_idFrame = wx.BoxSizer( wx.HORIZONTAL )
		
		self.tc_fillNumberOpen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.tc_fillNumberOpen.SetMinSize( wx.Size( 20,-1 ) )
		
		left_idFrame.Add( self.tc_fillNumberOpen, 0, wx.ALL, 5 )
		
		self.st_fileNumberSlash = wx.StaticText( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_fileNumberSlash.Wrap( -1 )
		left_idFrame.Add( self.st_fileNumberSlash, 0, wx.ALL, 5 )
		
		self.st_fileNumberAll = wx.StaticText( self, wx.ID_ANY, u"文件总数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_fileNumberAll.Wrap( -1 )
		self.st_fileNumberAll.SetFont( wx.Font( 9, 70, 90, 90, False, "宋体" ) )
		self.st_fileNumberAll.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		self.st_fileNumberAll.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		left_idFrame.Add( self.st_fileNumberAll, 0, wx.ALL, 5 )
		
		
		left_mainFrame.Add( left_idFrame, 1, wx.EXPAND, 5 )
		
		self.btn_lastText = wx.Button( self, wx.ID_ANY, u"上一篇", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_lastText.SetMinSize( wx.Size( -1,45 ) )
		
		left_mainFrame.Add( self.btn_lastText, 0, wx.ALL, 5 )
		
		self.btn_nextText = wx.Button( self, wx.ID_ANY, u"下一篇", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_nextText.SetMinSize( wx.Size( -1,45 ) )
		
		left_mainFrame.Add( self.btn_nextText, 0, wx.ALL, 5 )
		
		
		mainFrame.Add( left_mainFrame, 1, wx.EXPAND, 5 )
		
		right_mainFrame = wx.BoxSizer( wx.VERTICAL )
		
		right_mainFrame.SetMinSize( wx.Size( 520,-1 ) ) 
		self.st_textTitle = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_textTitle.Wrap( -1 )
		right_mainFrame.Add( self.st_textTitle, 0, wx.ALL, 5 )
		
		self.tc_textContent = wx.TextCtrl( self, wx.ID_ANY, u"测试", wx.DefaultPosition, wx.Size( -1,250 ), wx.TE_MULTILINE|wx.TE_WORDWRAP|wx.VSCROLL )
		self.tc_textContent.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		right_mainFrame.Add( self.tc_textContent, 0, wx.ALL|wx.EXPAND, 5 )
		
		right_contentFrame = wx.BoxSizer( wx.HORIZONTAL )
		
		self.list_segResult = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,250 ), wx.LC_ICON|wx.LC_REPORT|wx.VSCROLL )
		self.list_segResult.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		right_contentFrame.Add( self.list_segResult, 0, wx.ALL|wx.SHAPED, 5 )
		
		self.list_bow = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		right_contentFrame.Add( self.list_bow, 0, wx.ALL, 2 )
		
		right_segFrame = wx.BoxSizer( wx.VERTICAL )
		
		right_segFrame.SetMinSize( wx.Size( -1,250 ) ) 
		self.st_stopword = wx.StaticText( self, wx.ID_ANY, u"停用词：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_stopword.Wrap( -1 )
		right_segFrame.Add( self.st_stopword, 0, wx.ALL, 5 )
		
		self.tc_sotpWordList = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL )
		right_segFrame.Add( self.tc_sotpWordList, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.st_healthword = wx.StaticText( self, wx.ID_ANY, u"医疗领域词：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_healthword.Wrap( -1 )
		right_segFrame.Add( self.st_healthword, 0, wx.ALL, 5 )
		
		self.tc_healthKeywordList = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		right_segFrame.Add( self.tc_healthKeywordList, 0, wx.ALL|wx.EXPAND, 5 )
		
		right_seg_controlFrame = wx.BoxSizer( wx.HORIZONTAL )
		
		
		right_seg_controlFrame.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn_refreshContent = wx.Button( self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0 )
		right_seg_controlFrame.Add( self.btn_refreshContent, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.btn_saveWordList = wx.Button( self, wx.ID_ANY, u"保存列表", wx.DefaultPosition, wx.DefaultSize, 0 )
		right_seg_controlFrame.Add( self.btn_saveWordList, 0, wx.ALL, 5 )
		
		
		right_segFrame.Add( right_seg_controlFrame, 1, wx.EXPAND, 5 )
		
		self.st_stateText = wx.StaticText( self, wx.ID_ANY, u"当前状态", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_stateText.Wrap( -1 )
		self.st_stateText.SetMinSize( wx.Size( -1,50 ) )
		
		right_segFrame.Add( self.st_stateText, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		right_contentFrame.Add( right_segFrame, 1, wx.EXPAND, 5 )
		
		
		right_mainFrame.Add( right_contentFrame, 1, wx.EXPAND, 5 )
		
		
		mainFrame.Add( right_mainFrame, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( mainFrame )
		self.Layout()
		
		self.Centre( wx.HORIZONTAL )
		
		# Connect Events
		self.btn_HealthPath.Bind( wx.EVT_BUTTON, self.openHealthPath )
		self.tc_fillNumberOpen.Bind( wx.EVT_TEXT_ENTER, self.onChangeText )
		self.btn_nextText.Bind( wx.EVT_BUTTON, self.goNextHealthText )
		self.list_segResult.Bind( wx.EVT_LIST_ITEM_RIGHT_CLICK, self.onDictWordSelected )
		self.list_segResult.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onStopWordSelected )
		self.btn_refreshContent.Bind( wx.EVT_BUTTON, self.refreshContent )
		self.btn_saveWordList.Bind( wx.EVT_BUTTON, self.saveAllListToFile )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def openHealthPath( self, event ):
		event.Skip()
	
	def onChangeText( self, event ):
		event.Skip()
	
	def goNextHealthText( self, event ):
		event.Skip()
	
	def onDictWordSelected( self, event ):
		event.Skip()
	
	def onStopWordSelected( self, event ):
		event.Skip()
	
	def refreshContent( self, event ):
		event.Skip()
	
	def saveAllListToFile( self, event ):
		event.Skip()
	


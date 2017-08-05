# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from function import *
from boto.ec2.instancestatus import Event
###########################################################################
## Class ToolFrame
###########################################################################

class ToolFrame ( wx.Frame ):
	
	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def openHealthPath( self, event ):
		self.st_stateText.SetLabel(u"文档加载中...")
		directory_name,self.filename_list = getDirectoryPath()
		if directory_name:self.st_healthTextPath.SetLabel(directory_name)
		else:self.st_healthTextPath.SetLabel(u"文档无名称")
		
		if not self.filename_list:
			self.st_stateText.SetLabel(u"无文件")
			return False
		self.st_fileNumberAll.SetLabel(str(len(self.filename_list)))
		# 设置当前id，表示工作进行状态
		self.id = 0
		self.refresh()
	
	def stateText(self,text):self.st_stateText.SetLabel(text)
	def refresh(self):	
		self.stateText(u"加载中...")
		showContentAndSeg(self.id,self.textCtl_openID,self.filename_list,\
                      self.st_textTitle,self.tc_textContent,self.list_segResultBow)
		self.tc_healthKeywordList.Value=u""
		self.tc_sotpWordList.Value = u""
		self.stateText(u"加载成功")
	def saveStopWordAndDict(self):
		self.saveStopWord()
		self.saveDict()

	def saveStopWord(self):
		stop_word = self.tc_sotpWordList.Value.strip()
		print "停用词："
		print stop_word
		if stop_word:
			words = stop_word.split()
			for word in words:
				if word not in self.stopword_list: 
					self.stopword_list.append(word)
		global stopword_file
		SaveWordToFile(stopword_file,self.stopword_list)
		
	def saveDict(self):
		self.stateText(u"保存中")
		# 将textctrl中存留的词语保存入文件
		health_keyword = self.tc_healthKeywordList.Value.strip()
		print "健康关键词："
		print health_keyword
		if health_keyword:
			words = health_keyword.split()
			for word in words:
				word += u" n"
				if word not in self.userdict_list:
					self.userdict_list.append(word)
		global userdict_file
		SaveWordToFile(userdict_file,self.userdict_list)
		self.stateText(u"词典保存成功！")
	def onChangeText(self,event):
		if self.id < 0: return
		self.id = (int)(self.textCtl_openID.Value) # String.parseInt(string)
		self.refresh()
	def goNextHealthText( self, event ):
		if self.id < 0: return
		self.id += 1
		self.saveStopWordAndDict()
		self.refresh()
	def goLastHealthText( self, event ):
		if self.id <= 0: return
		self.id -= 1
		self.refresh()
	def refreshContent( self, event ):
		if self.id < 0: return
		self.refresh()
	def saveAllListToFile( self, event ):
		self.saveStopWordAndDict()
	
	def onStopwordSelected( self, event ):	
		item = self.list_segResultBow.GetFocusedItem()
		word = self.list_segResultBow.GetItemText(item, col=0)
		self.tc_sotpWordList.Value +=  word + u" "
	def onDictSelected(self , event):
		item = self.list_segResultBow.GetFocusedItem()
		word = self.list_segResultBow.GetItemText(item, col=0)
		self.tc_healthKeywordList.Value += word + u" "	

	def __init__( self, parent ):
		
		self.id = -1
		self.filename_list = []
		global stopword_file,userdict_file
		self.stopword_list = LoadStopWordFromFile(stopword_file)
		self.userdict_list = LoadDictFromFile(userdict_file)
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,750 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		self.st_healthTextPath.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		left_mainFrame.Add( self.st_healthTextPath, 0, wx.ALL, 5 )
		
		left_idFrame = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textCtl_openID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.textCtl_openID.SetMinSize( wx.Size( 25,-1 ) )
		
		left_idFrame.Add( self.textCtl_openID, 0, wx.ALL, 5 )
		
		self.st_fileNumberSlash = wx.StaticText( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_fileNumberSlash.Wrap( -1 )
		self.st_fileNumberSlash.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		left_idFrame.Add( self.st_fileNumberSlash, 0, wx.ALL, 5 )
		
		self.st_fileNumberAll = wx.StaticText( self, wx.ID_ANY, u"文件总数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_fileNumberAll.Wrap( -1 )
		self.st_fileNumberAll.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
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
		
		right_mainFrame.SetMinSize( wx.Size( 900,-1 ) ) 
		self.st_textTitle = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_textTitle.Wrap( -1 )
		self.st_textTitle.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		right_mainFrame.Add( self.st_textTitle, 0, wx.ALL, 5 )
		
		self.tc_textContent = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,350 ), wx.TE_MULTILINE|wx.VSCROLL)
		self.tc_textContent.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		right_mainFrame.Add( self.tc_textContent, 0, wx.ALL|wx.EXPAND, 5 )
		
		right_contentFrame = wx.BoxSizer( wx.HORIZONTAL )
		
		# 词袋化，加快筛选速度
		self.list_segResultBow = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 190,400 ),wx.LC_REPORT|wx.VSCROLL )
		self.list_segResultBow.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString))
		self.list_segResultBow.InsertColumn(0, 'word_bow')  
		self.list_segResultBow.InsertColumn(1, 'flag')  
		right_contentFrame.Add( self.list_segResultBow, 0, wx.ALL|wx.EXPAND|wx.SHAPED, 5 )
		
		'''
		# 全部分词结果
		self.list_segResult = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 190,400 ),wx.LC_REPORT|wx.VSCROLL )
		self.list_segResult.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString))
		self.list_segResult.InsertColumn(0, 'word')  
		self.list_segResult.InsertColumn(1, 'flag')  
		right_contentFrame.Add( self.list_segResult, 0, wx.ALL|wx.EXPAND|wx.SHAPED, 5 )
		'''
		right_segFrame = wx.BoxSizer( wx.VERTICAL )
		
		right_segFrame.SetMinSize( wx.Size( -1,250 ))
		self.st_stopword = wx.StaticText( self, wx.ID_ANY, u"新停用词：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_stopword.Wrap( -1 )
		self.st_stopword.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		right_segFrame.Add( self.st_stopword, 0, wx.ALL, 5 )
		

		self.tc_sotpWordList = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,70 ), wx.TE_MULTILINE|wx.VSCROLL )
		right_segFrame.Add( self.tc_sotpWordList, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.st_healthword = wx.StaticText( self, wx.ID_ANY, u"新医疗领域词：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_healthword.Wrap( -1 )
		self.st_healthword.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		right_segFrame.Add( self.st_healthword, 0, wx.ALL, 5 )
		
		self.tc_healthKeywordList = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,70 ), wx.TE_MULTILINE|wx.VSCROLL )
		right_segFrame.Add( self.tc_healthKeywordList, 0, wx.ALL|wx.EXPAND, 5 )
		
		right_seg_controlFrame = wx.BoxSizer( wx.HORIZONTAL )
		
		#right_seg_controlFrame.AddSpacer(1, wx.EXPAND, 5 )
		
		self.btn_refreshContent = wx.Button( self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0 )
		right_seg_controlFrame.Add( self.btn_refreshContent, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.btn_saveWordList = wx.Button( self, wx.ID_ANY, u"=保存=", wx.DefaultPosition, wx.DefaultSize, 0 )
		right_seg_controlFrame.Add( self.btn_saveWordList, 0, wx.ALL, 5 )
		
		
		right_segFrame.Add( right_seg_controlFrame, 1, wx.EXPAND, 5 )
		
		self.st_stateText = wx.StaticText( self, wx.ID_ANY, u"当前状态", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_stateText.Wrap( -1 )
		self.st_stateText.SetMinSize( wx.Size( -1,50 ) )
		self.st_stateText.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString))
		self.st_stateText.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		right_segFrame.Add( self.st_stateText, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		right_contentFrame.Add( right_segFrame, 1, wx.EXPAND, 5 )
		
		right_mainFrame.Add( right_contentFrame, 1, wx.EXPAND, 5 )
		
		
		mainFrame.Add( right_mainFrame, 1, wx.EXPAND, 5 )
		
		self.SetSizer( mainFrame )
		self.Layout()
		
		self.Centre( wx.HORIZONTAL )
		
		# Connect Events
		self.btn_HealthPath.Bind( wx.EVT_BUTTON, self.openHealthPath )
		self.btn_nextText.Bind( wx.EVT_BUTTON, self.goNextHealthText )
		self.btn_lastText.Bind( wx.EVT_BUTTON, self.goLastHealthText )
		self.btn_refreshContent.Bind( wx.EVT_BUTTON, self.refreshContent )
		self.btn_saveWordList.Bind( wx.EVT_BUTTON, self.saveAllListToFile )
		#self.list_segResult.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onDictSelected )
		self.list_segResultBow.Bind( wx.EVT_LIST_ITEM_RIGHT_CLICK, self.onStopwordSelected )
		self.list_segResultBow.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.onDictSelected )
		self.textCtl_openID.Bind( wx.EVT_TEXT_ENTER, self.onChangeText )


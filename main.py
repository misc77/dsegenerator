import configProvider
import logger
import wx
from apscheduler.schedulers.background import BackgroundScheduler
from dseGenerator import DSEGenerator
from checklistParser import parseChecklist
from resources import Resources

class DSEGeneratorApp(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(DSEGeneratorApp, self).__init__(*args, **kwargs)
        # Read Config for UI
        self.display_log_size = configProvider.getConfigEntryOrDefault('UI Setup', 'DISPLAY_LOG_SIZE', -500)
        #Scheduler   
        self.log_scheduler = BackgroundScheduler()
        self.generator = DSEGenerator()
        self.initUI()
        self.log_scheduler.add_job(self.LogUpdate, 'interval', seconds=10, id='log_job')
        self.log_scheduler.start()
        
    
    def initUI(self):
        self.SetSize((800,600))
        self.SetTitle("DSEGenerator Application")
        self.Centre()
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(3,8)

        #Checklist Label
        checklistLabel = wx.StaticText(panel, label="Checklist Document:")
        sizer.Add(checklistLabel, pos=(0,0), flag=wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, border=8)
        #FileDialog Button
        filePicker = wx.FilePickerCtrl(panel, message="Please select a Checklist Document in *.docx Format:", wildcard="*.docx", style = wx.FLP_USE_TEXTCTRL )
        filePicker.SetTextCtrlGrowable(True)
        filePicker.SetTextCtrlProportion(20)
        sizer.Add(filePicker, pos=(0,1), span=(0,2), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=8)

        #Version of Document selected
        versionLabel = wx.StaticText(panel, label="Version:")
        sizer.Add(versionLabel, pos=(1,0), flag=wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, border=8)
        self.versionText = wx.TextCtrl(panel)
        self.versionText.SetEditable(False)
        sizer.Add(self.versionText, pos=(1,1),  flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=8)

        #Log 
        logLabel = wx.StaticText(panel, label="Log:")
        sizer.Add(logLabel, pos=(7,0), flag=wx.EXPAND|wx.LEFT|wx.RIGHT,  border=8)
        self.logView = wx.TextCtrl(panel, size=(200,200), style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY|wx.TE_BESTWRAP|wx.TE_RICH2, pos=wx.DefaultPosition)
        self.logView.SetEditable(False)
        sizer.Add(self.logView, pos=(8,0), span=(3,3), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=8)

        sizer.AddGrowableCol(2)
        #sizer.AddGrowableRow(0)
        panel.SetSizer(sizer)

        #Menubar
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Exit', 'Exit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        #Events
        self.Bind(wx.EVT_FILEPICKER_CHANGED, self.OnPickFile, filePicker)
        self.Bind(wx.EVT_MENU, self.OnExit, fileItem)


    #--- EVENT HANDLER
    def OnPickFile(self, e):
        log = logger.getLogger()
        if e.GetPath() != None:
            self.generator.checklistFile = e.GetPath()
            checklistDoc = parseChecklist(self.generator.checklistFile)
            self.generator.checklistObject = checklistDoc
            if checklistDoc.wordVersion != None:
                self.versionText.write(checklistDoc.wordVersion)
        else:
            log.warn("No file has been selected!")
    
    def LogUpdate(self):
        file_handle = open(Resources.getLogFile(), "r")
        self.logView.SetInsertionPoint(0)
        self.logView.SetValue(file_handle.read())
        self.logView.AppendText("")
        self.logView.Refresh()
        file_handle.close()

    def OnExit(self, e):
        dlg = wx.MessageDialog  (self, 
                                "Do you really want to close this application?",
                                "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Close()


def main():
   app = wx.App()
   ex = DSEGeneratorApp(None)
   ex.Show()
   app.MainLoop()     
    

if __name__ == '__main__':
    main()

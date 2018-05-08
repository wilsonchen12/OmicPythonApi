from OmicPythonApi.Core.OmicPythonApi import *
class TextDumpArrayLandSampleData(OmicPythonApi):
    """ A python api for TextDumpArrayLandSampleData proc
        See Oscript and Log fields in the class object for details of the oshell jobs.
        Please refer to Omicsoft Wiki pages for details of the commands in Oscript.
        Wilson Chen, Omicsoft, 20180313
    """
    def __init__(self):
        """
        Input:
			1. ServerAddress
			2. ServerUserId
			3. ServerUserPsw
			4. LandName
			5. DataMode
			6. Sample
			7. DownloadOriginalData (default=True)
			8. DownloadFullMetaData (defaul=False)
			9. DownloadGeneLevelData (default=False)
			10. OutputFolder
			11. Output
        Output: an initialized obj. Use obj.Run function to run the oscripts.
        """

        self.Land=''
        self.DataMode=''
        self.Sample=''
        self.OutputFolder=''
        self.Output=''

        self.ServerAddress=''
        self.ServerUserId=''
        self.ServerUserPsw=''

        self.DownloadOriginalData='True'
        self.DownloadFullMetaData='False'
        self.DownloadGeneLevelData='False'


        self.Config=self.LoadConfigFile()
        self.OscriptTemplate=self.SetOscriptTemplate()
        self.Oscript=''
        self.Log=''
        return

    def SetOscriptTemplate(self):
        print('Load Oscript template')
        self.OscriptTemplate="""
Begin TextDumpArrayLandSampleData /Namespace=Land;
Server "@ServerAddress@" /UserID=@ServerUserId@ /Password=@ServerUserPsw@;
Land @Land@;
DataMode @DataMode@;
Sample @Sample@;
Options /DownloadOriginalData=@DownloadOriginalData@ /DownloadFullMetaData=@DownloadFullMetaData@ /DownloadGeneLevelData=@DownloadGeneLevelData@
/OutputFolder="@OutputFolder@";
Output @Output@;
End;
        """
        return(self.OscriptTemplate)

    def MakeOscript(self):
        """Modify Oscript
        Wilson Chen, 20171218"""
        print('Make oscript')
        Oscript=self.OscriptTemplate
        Oscript=Oscript.replace('@Land@',self.Land)
        Oscript=Oscript.replace('@DataMode@',self.DataMode)
        Oscript=Oscript.replace('@Sample@',self.Sample)
        Oscript=Oscript.replace('@OutputFolder@',self.OutputFolder)
        Oscript=Oscript.replace('@Output@',self.Output)
        Oscript=Oscript.replace('@DownloadOriginalData@',self.DownloadOriginalData)
        Oscript=Oscript.replace('@DownloadFullMetaData@',self.DownloadFullMetaData)
        Oscript=Oscript.replace('@DownloadGeneLevelData@',self.DownloadGeneLevelData)

        Oscript=Oscript.replace('@ServerAddress@',self.ServerAddress)
        Oscript=Oscript.replace('@ServerUserId@',self.ServerUserId)
        Oscript=Oscript.replace('@ServerUserPsw@',self.ServerUserPsw)

        self.Oscript=Oscript

        return(self.Oscript)

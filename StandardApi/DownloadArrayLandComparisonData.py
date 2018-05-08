from OmicPythonApi.Core.OmicPythonApi import *
class DownloadArrayLandComparisonData(OmicPythonApi):
    """ A python api for DownloadArrayLandComparisonData proc .
        See Oscript and Log fields in the class object for details of the oshell jobs.
        Please refer to Omicsoft Wiki pages for details of the commands in Oscript.
        Wilson Chen, Omicsoft, 20180314
    """
    def __init__(self,ServerAddress='',ServerUserId='',ServerUserPsw='',Land='',ComparisonSet='',OutputFolder=''):
        """
		input:
            1. ServerAddress: array server address (eg: tcp:\\xxx.xxx.xxx:8065)
            2. ServerUserId: array server user id
            3. ServerUserPsw: array server user psw
            4. Land:
            5. ComparisonSet:
            6: DownloadOriginalData: default 'True'
            7. DownloadGeneLevelData: default 'True'
            8: DownloadFullMetaData: default 'True'
            9. OutputFolder:
            10. Output: default "DownloadArrayLandComparisonData"
        Output: an initialized obj. Use obj.Run function to run the oscripts.
		"""
        self.ServerUserId=ServerUserId
        self.ServerUserPsw=ServerUserPsw
        self.ServerAddress=ServerAddress

        self.Land=Land
        self.ComparisonSet=ComparisonSet
        self.DownloadOriginalData='True'
        self.DownloadGeneLevelData='True'
        self.DownloadFullMetaData='True'
        self.OutputFolder=OutputFolder
        self.Output='DownloadArrayLandComparisonData'

        self.Config=self.LoadConfigFile()
        self.OscriptTemplate=self.SetOscriptTemplate()
        self.Oscript=''
        self.Log=''
        return

    def SetOscriptTemplate(self):
        print('Load Oscript template')
        self.OscriptTemplate="""
Begin DownloadArrayLandComparisonData  /Namespace=Land;
Server "@ServerAddress@" /UserID=@ServerUserId@ /Password=@ServerUserPsw@;
Land  @Land@;
ComparisonSet @ComparisonSet@;
Options /DownloadOriginalData=@DownloadOriginalData@ /DownloadGeneLevelData=@DownloadGeneLevelData@ /DownloadFullMetaData=@DownloadFullMetaData@
/OutputFolder="@OutputFolder@";
Output @Output@;
End;
        """
        return(self.OscriptTemplate)

    def MakeOscript(self):
        """Modify Oscript
        Wilson Chen, 20180313"""
        print('Make oscript')
        Oscript=self.OscriptTemplate
        Oscript=Oscript.replace('@Land@',self.Land)
        Oscript=Oscript.replace('@OutputFolder@',self.OutputFolder)
        Oscript=Oscript.replace('@ComparisonSet@',self.ComparisonSet)
        Oscript=Oscript.replace('@DownloadOriginalData@',self.DownloadOriginalData)
        Oscript=Oscript.replace('@DownloadGeneLevelData@',self.DownloadGeneLevelData)
        Oscript=Oscript.replace('@DownloadFullMetaData@',self.DownloadFullMetaData)
        Oscript=Oscript.replace('@Output@',self.Output)
        Oscript=Oscript.replace('@ServerAddress@',self.ServerAddress)
        Oscript=Oscript.replace('@ServerUserId@',self.ServerUserId)
        Oscript=Oscript.replace('@ServerUserPsw@',self.ServerUserPsw)

        self.Oscript=Oscript

        return(self.Oscript)

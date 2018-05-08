from OmicPythonApi.Core.OmicPythonApi import *
class DownloadComparisonSet(OmicPythonApi):
    """ A python api for ConnectServer and DownloadComparisonSet proc .
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
            6. OutputFolder:
        Output: an initialized obj. Use obj.Run function to run the oscripts.
		"""
        self.ServerUserId=ServerUserId
        self.ServerUserPsw=ServerUserPsw
        self.ServerAddress=ServerAddress

        self.Land=Land
        self.ComparisonSet=ComparisonSet
        self.OutputFolder=OutputFolder

        self.Config=self.LoadConfigFile()
        self.OscriptTemplate=self.SetOscriptTemplate()
        self.Oscript=''
        self.Log=''
        return

    def SetOscriptTemplate(self):
        print('Load Oscript template')
        self.OscriptTemplate="""
Begin ConnectServer;
Server "@ServerAddress@" /User=@ServerUserId@ /Password=@ServerUserPsw@;
End;

Begin DownloadComparisonSet  /Namespace=Land;
Land  @Land@;
ComparisonSet @ComparisonSet@;
Options /OutputFolder="@OutputFolder@";
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
        Oscript=Oscript.replace('@ServerAddress@',self.ServerAddress)
        Oscript=Oscript.replace('@ServerUserId@',self.ServerUserId)
        Oscript=Oscript.replace('@ServerUserPsw@',self.ServerUserPsw)

        self.Oscript=Oscript

        return(self.Oscript)

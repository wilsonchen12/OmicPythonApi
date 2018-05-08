from OmicPythonApi.Core.OmicPythonApi import *
class FetchSampleSetMetaData(OmicPythonApi):
    """ A python api for FetchSampleSetMetaData proc.
        See Oscript and Log fields in the class object for details of the oshell jobs.
        Please refer to Omicsoft Wiki pages for details of the commands in Oscript.
        Wilson Chen, Omicsoft, 20181207
    """
    def __init__(self,ServerAddress='',ServerUserId='',ServerUserPsw='',SampleSetId='',OutputFile=''):
        """A python API that wraps FetchSampleSetMetaData webcommands. See Omicsoft wiki for the proc parameters.
		input:
            1. ServerAddress: array server address (eg: tcp:\\xxx.xxx.xxx:8065)
            2. ServerUserId: array server user id
            3. ServerUserPsw: array server user psw
            4. OutputFilePath
            5. SampleSetId
        Output: an initialized obj. Use obj.Run function to run the oscripts.
		"""
        self.ServerUserId=ServerUserId
        self.ServerUserPsw=ServerUserPsw
        self.ServerAddress=ServerAddress

        self.SampleSetId=SampleSetId
        self.OutputFile=OutputFile

        self.Config=self.LoadConfigFile()
        self.OscriptTemplate=self.SetOscriptTemplate()
        self.Oscript=''
        self.Log=''
        return

    def SetOscriptTemplate(self):
        print('Load Oscript template')
        self.OscriptTemplate="""
Begin ExecuteCommand /Namespace=Server;
Server "ServerAddress" /UserID=ServerUserId /Password=ServerUserPsw;
Command FetchSampleSetMetaData;
Options
"
SampleSetID=SampleSetId0
";
OutputFile "SampleSetMetaDataOutputFile";
End;
        """
        return(self.OscriptTemplate)

    def MakeOscript(self):
        """Modify Oscript
        Wilson Chen, 20171207"""
        print('Make oscript')
        Oscript=self.OscriptTemplate
        Oscript=Oscript.replace('SampleSetId0',self.SampleSetId)
        Oscript=Oscript.replace('SampleSetMetaDataOutputFile',self.OutputFile)
        Oscript=Oscript.replace('ServerAddress',self.ServerAddress)
        Oscript=Oscript.replace('ServerUserId',self.ServerUserId)
        Oscript=Oscript.replace('ServerUserPsw',self.ServerUserPsw)

        self.Oscript=Oscript

        return(self.Oscript)

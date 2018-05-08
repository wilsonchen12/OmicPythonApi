from OmicPythonApi.Core.OmicPythonApi import *
class AddArrayLandSampleSet(OmicPythonApi):
    """ A python api for ConnectServer and AddArrayLandSampleSet proc.
        See Oscript and Log fields in the class object for details of the oshell jobs.
        Please refer to Omicsoft Wiki pages for details of the Oscript.
        Wilson Chen, Omicsoft, 20180313
    """
    def __init__(self,ServerAddress='',ServerUserId='',ServerUserPsw='',Land='',SampleSetName='',File='',Tag=''):
        """A python API that wraps ConnectServer and ListLands. See Omicsoft wiki for the proc parameters.
		input:
            1. ServerAddress: array server address (eg: tcp:\\xxx.xxx.xxx:8065)
            2. ServerUserId: array server user id
            3. ServerUserPsw: array server user psw
            4. Land:
            5. SampleSetName
            6. File: sample list file
            7. Tag: sampleset tag
        Output: an initialized obj. Use obj.Run function to run the oscripts.
		"""
        self.ServerUserId=ServerUserId
        self.ServerUserPsw=ServerUserPsw
        self.ServerAddress=ServerAddress

        self.Land=Land
        self.SampleSetName=SampleSetName
        self.File=File
        self.Tag=Tag

        self.Readers=''
        self.Editors=''
        self.Replace='False'
        
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

Begin AddArrayLandSampleSet /Namespace=Land;
Land @Land@;
SampleSetName @SampleSetName@;
File "@File@" /Format=Txt;
Tag @Tag@;
Options /Readers=@Readers@ /Editors=@Editors@ /Replace=@Replace@;
End;
        """
        return(self.OscriptTemplate)

    def MakeOscript(self):
        """Modify Oscript
        Wilson Chen, 20180313"""
        print('Make oscript')
        Oscript=self.OscriptTemplate
        Oscript=Oscript.replace('@Land@',self.Land)
        Oscript=Oscript.replace('@SampleSetName@',self.SampleSetName)
        Oscript=Oscript.replace('@File@',self.File)
        Oscript=Oscript.replace('@Tag@',self.Tag)
        Oscript=Oscript.replace('@Readers@',self.Readers)
        Oscript=Oscript.replace('@Editors@',self.Editors)
        Oscript=Oscript.replace('@Replace@',self.Replace)
        Oscript=Oscript.replace('@ServerAddress@',self.ServerAddress)
        Oscript=Oscript.replace('@ServerUserId@',self.ServerUserId)
        Oscript=Oscript.replace('@ServerUserPsw@',self.ServerUserPsw)


        self.Oscript=Oscript

        return(self.Oscript)

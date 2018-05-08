from OmicPythonApi.Core.OmicPythonApi import *
class IA_SearchPublishedProjects(OmicPythonApi):
    """ A python api for SearchPublishedProjects proc, which produce a text file that lists search results
        See Oscript and Log fields in the class object for details of the oshell jobs.
        Please refer to Omicsoft Wiki pages for details of the commands in Oscript.
        Wilson Chen, Omicsoft, 20171207
    """
    def __init__(self,ServerAddress='',ServerUserId='',ServerUserPsw='',ProjectPattern='',OutputFile=''):
        """Input:
            1. ServerAddress
            2. ServerUserId
            3. ServerUserPsw
            4. ProjectPattern
            5. OutputFile
            Output: an initialized obj. Use obj.Run function to run the oscripts.
        """
        self.ProjectPattern=ProjectPattern
        self.ServerAddress=ServerAddress
        self.ServerUserId=ServerUserId
        self.ServerUserPsw=ServerUserPsw
        self.OutputFile=OutputFile

        self.Config=self.LoadConfigFile()
        self.OscriptTemplate=self.SetOscriptTemplate()
        self.Oscript=''
        return

    def SetOscriptTemplate(self):
        print('Load Oscript template')
        self.OscriptTemplate="""
Begin ExecuteCommand /Namespace=Server;
Server "@ServerAddress@" /UserID=@ServerUserId@ /Password=@ServerUserPsw@;
Command IA_SearchPublishedProjects;
Options
"
ProjectPattern=@ProjectPattern@
";
OutputFile "@OutputFile@";
End;
        """
        return(self.OscriptTemplate)

    def MakeOscript(self):
        """Modify Oscript
        Wilson Chen, 20171130"""
        print('Make oscript')
        Oscript=self.OscriptTemplate
        Oscript=Oscript.replace('@ServerAddress@',self.ServerAddress)
        Oscript=Oscript.replace('@ServerUserId@',self.ServerUserId)
        Oscript=Oscript.replace('@ServerUserPsw@',self.ServerUserPsw)
        Oscript=Oscript.replace('@ProjectPattern@',self.ProjectPattern)
        Oscript=Oscript.replace('@OutputFile@',self.OutputFile)

        self.Oscript=Oscript

        return(self.Oscript)

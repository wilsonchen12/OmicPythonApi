from OmicPythonApi.Core.OmicPythonApi import *

class ImportTableToLocalProject(OmicPythonApi):
    """ A python api for creating a local project and importing a table to the local project
        See Oscript and Log fields in the class object for details of the oshell jobs.
        Please refer to Omicsoft Wiki pages for details of the commands in Oscript.
        Wilson Chen, Omicsoft, 20180307
    """
    def __init__(self,ProjectId='',ProjectFolderPath='',InputTableFilePath='',NameOfTableInProject='ImportedTable'):
        """Input:
            1. ProjectId
		   2. ProjectFolderPath
		   3. InputTableFilePath
		   4. NameOfTableInProject
           Output: an initialized obj. Use obj.Run function to run the oscripts.
        """
        self.ProjectId=ProjectId
        self.ProjectFolderPath=ProjectFolderPath
        self.InputTableFilePath=InputTableFilePath
        self.NameOfTableInProject=NameOfTableInProject

        self.Config=self.LoadConfigFile()
        self.OscriptTemplate=self.SetOscriptTemplate()
        self.Log=''
        self.Oscript=''
        return

    def SetOscriptTemplate(self):
        print('Load Oscript template')
        self.OscriptTemplate="""
Begin NewProject;
Project @ProjectName@ /IsDistributed=False;
File "@ProjectFilePath@.osprj";
End;

Begin ImportTable /Namespace=Table;
Project @ProjectName@;
File "@InputTableFilePath@";
Options /Format=Txt;
Output @NameOfTableInProject@;
End;

Begin SaveProject;
File "@ProjectFilePath@.osprj";
Options /Distributed=True;
End;
        """
        return(self.OscriptTemplate)

    def MakeOscript(self):
        """Modify Oscript"""
        import os

        print('Make oscript')
        Oscript=self.OscriptTemplate
        Oscript=Oscript.replace('@ProjectName@',self.ProjectId)

        ProjectFilePath=os.path.join(self.ProjectFolderPath,self.ProjectId)
        Oscript=Oscript.replace('@ProjectFilePath@',ProjectFilePath)

        if self.InputTableFilePath=='':
            self.InputTableFilePath='TableData1'

        Oscript=Oscript.replace('@InputTableFilePath@',self.InputTableFilePath)
        Oscript=Oscript.replace('@NameOfTableInProject@',self.NameOfTableInProject)

        self.Oscript=Oscript

        return(self.Oscript)

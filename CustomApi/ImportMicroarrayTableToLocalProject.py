from OmicPythonApi.Core.OmicPythonApi import *

class ImportMicroarrayTableToLocalProject(OmicPythonApi):
    """ A python api for creating a local project and importing a microarray expression table to the local project, attach annotation and design table to the expression.
        See Oscript and Log fields in the class object for details of the oshell jobs.
        Please refer to Omicsoft Wiki pages for details of the commands in Oscript.
        Wilson Chen, Omicsoft, 20180427
    """
    def __init__(self,ProjectId='',ProjectFolderPath='',MicroarrayTableFilePath='',AnnotationTableFilePath='',DesignTableFilePath='',NameOfImportedOmicdata='ImportedOmicData'):
        """Input:
           1. ProjectId
		    2. ProjectFolderPath
		    3. MicroarrayTableFilePath
		    4. AnnotationTAbleFilePath
           5. DesignTableFilePath
           6. NameOfImportedOmicdata: the name of the imported omicdata in the project
           Output: an initialized obj. Use obj.Run function to run the oscripts.
        """
        self.ProjectId=ProjectId
        self.ProjectFolderPath=ProjectFolderPath
        self.MicroarrayTableFilePath=MicroarrayTableFilePath
        self.AnnotationTableFilePath=AnnotationTableFilePath
        self.DesignTableFilePath=DesignTableFilePath
        self.NameOfImportedOmicdata=NameOfImportedOmicdata

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


Begin ImportMicroArray /Namespace=MicroArray;
File "@MicroarrayTableFilePath@";
Options  /Format=Txt /RowsAreObservations=False /IgnoreDescriptiveColumns=False;
Output @NameOfImportedOmicdata@;
End;


Begin AttachDesign;
Target @NameOfImportedOmicdata@;
Project @ProjectName@;
Options  /Format=Txt /Append=False /ChangeOrders=False;
File "@DesignTableFilePath@";
End;


Begin AttachAnnotation;
Target @NameOfImportedOmicdata@;
Options  /Format=Txt /Append=False /ChangeOrders=False;
File "@AnnotationTableFilePath@";
End;

Begin SaveProject;
File "@ProjectFilePath@.osprj";
Options /Distributed=True;
End;

Begin CloseProject;
Project @ProjectName@;
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

        Oscript=Oscript.replace('@MicroarrayTableFilePath@',self.MicroarrayTableFilePath)
        Oscript=Oscript.replace('@DesignTableFilePath@',self.DesignTableFilePath)
        Oscript=Oscript.replace('@AnnotationTableFilePath@',self.AnnotationTableFilePath)
        Oscript=Oscript.replace('@NameOfImportedOmicdata@',self.NameOfImportedOmicdata)

        self.Oscript=Oscript

        return(self.Oscript)

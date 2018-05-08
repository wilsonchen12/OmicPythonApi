from OmicPythonApi.Core.OmicPythonApi import *
class RnaSeqPipelineInNewServerProject(OmicPythonApi):
    """ A python api for create a new server project and run RnaSeqPipeline
        See Oscript and Log fields in the class object for details of the oshell jobs.
        Please refer to Omicsoft Wiki pages for details of the commands in Oscript.
        Wilson Chen, Omicsoft, 20180101"""
    def __init__(self,ServerAddress='',ServerUserId='',ServerUserPsw='',ProjectId='',Files='',OutputFolder=''):
        """Input:
            1. ProjectId:
            2. Files:
            3. OutputFolder:
            (the rest needs to be reset via object properties directly)
            4. ParallelJobNumber:   default '1'
            5. ThreadNumber:        default '1'
            6. Reference:           default 'Human.B37.3'
            7. GeneModel:            default 'OmicsoftGene20130723'
            8. PairedEnd:           default 'True'
            9. Replace:             default 'True'
            10. PairedEndFusionAnalysis:   default 'True'
        """
        self.ProjectId=ProjectId
        self.Files=Files
        self.OutputFolder=OutputFolder

        self.ServerAddress=ServerAddress
        self.ServerUserId=ServerUserId
        self.ServerUserPsw=ServerUserPsw

        self.ParallelJobNumber='1'
        self.ThreadNumber='1'

        self.Reference='Human.B37.3' #'Mouse.B38'
        self.GeneModel='OmicsoftGene20130723'

        self.PairedEnd='True'
        self.Replace='True'
        self.PairedEndFusionAnalysis='True'


        self.Config=self.LoadConfigFile()
        self.OscriptTemplate=self.SetOscriptTemplate()
        self.Log=''
        self.Oscript=''

    def SetOscriptTemplate(self):
        print('Load Oscript template')
        self.OscriptTemplate="""

Begin ConnectServer;
Server "@ServerAddress@" /User=@ServerUserId@ /Password=@ServerUserPsw@;
End;

Begin NewProject;
ServerProject @ProjectName@;
Options /Distributed=True;
End;

Begin RnaSeqPipeline /Namespace=NgsLib /RunOnServer=True;
Files
"@FastqFilePath@";
Reference @Reference@;
GeneModel @GeneModel@;
NgsQCWizard /Run=True;
FilterNgsFiles /Run=True;
Count /Run=True /AutoTrimUtr=True;
RnaSeqQCMetrics /Run=True;
SummarizeExonJunction /Run=True;
SummarizeMutation2Snp /Run=True;
CombinedFusionAnalysis /Run=True;
PairedEndFusionAnalysis /Run=@PairedEndFusionAnalysis@;
GenerateBas /Run=True;
GenerateLandAlv /Run=False;
Options
/ParallelJobNumber=@ParallelJobNumber@  /ThreadNumberPerJob=@ThreadNumber@
/PairedEnd=@PairedEnd@ /FileFormat=AUTO
/OutputFolder="@OutputFolder@"
/CompressionMethod=None /Gzip=True /Replace=@Replace@;
Output test;
End;


Begin SaveProject;
Project @ProjectName@;
Options /Distributed=True;
End;

Begin CloseProject;
Project @ProjectName@;
End;
        """
        return(self.OscriptTemplate)

    def MakeOscript(self):
        """Modify Oscript"""
        print('Make oscript')
        Oscript=self.OscriptTemplate
        Oscript=Oscript.replace('@ProjectName@',self.ProjectId)
        Oscript=Oscript.replace('@FastqFilePath@',self.Files)
        Oscript=Oscript.replace('@OutputFolder@',self.OutputFolder)
        Oscript=Oscript.replace('@ParallelJobNumber@',self.ParallelJobNumber)
        Oscript=Oscript.replace('@ThreadNumber@',self.ThreadNumber)

        Oscript=Oscript.replace('@ServerAddress@',self.ServerAddress)
        Oscript=Oscript.replace('@ServerUserId@',self.ServerUserId)
        Oscript=Oscript.replace('@ServerUserPsw@',self.ServerUserPsw)

        Oscript=Oscript.replace('@Reference@',self.Reference)
        Oscript=Oscript.replace('@GeneModel@',self.GeneModel)
        Oscript=Oscript.replace('@PairedEnd@',self.PairedEnd)

        Oscript=Oscript.replace('@PairedEndFusionAnalysis@',self.PairedEndFusionAnalysis)

        self.Oscript=Oscript

        return(self.Oscript)

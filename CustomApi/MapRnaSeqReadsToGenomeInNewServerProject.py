from OmicPythonApi.Core.OmicPythonApi import *
class MapRnaSeqReadsToGenomeInNewServerProject(OmicPythonApi):
    """A python api that connect server, create new project and MapRnaSeqReadToGenome.
        See Oscript and Log fields in the class object for details of the oshell jobs.
        Please refer to Omicsoft Wiki pages for details of the commands in Oscript.
        Wilson Chen, Omicsoft, 20180101"""
    def __init__(self,ServerAddress='',ServerUserId='',ServerUserPsw='',ProjectId='',Files='',OutputFolder=''):
        """Input:
            1. ProjectId:       ProjectId
            2. Files:           input fastqfile path
            3. OutputFolder:    OutputFolder
            4. ServerAddress
            5. ServerUserId
            6. ServerUserPsw
            7. Reference:       default: 'Human.B37.3', and can be reset in object property
            8. GeneModel:       default: 'OmicsoftGene20130723', and can be reset in object property
            9. Replace:         default: 'True', and can be reset in object property
            10. ParallelJobNumber: default: '1', and can be reset in object property
            11. ThreadNumber:   default:  "4", and can be reset in object property
            Output: an initialized obj. Use obj.Run function to run the oscripts.
            """
        self.ProjectId=ProjectId
        self.Files=Files
        self.OutputFolder=OutputFolder

        self.ServerAddress=ServerAddress
        self.ServerUserId=ServerUserId
        self.ServerUserPsw=ServerUserPsw

        self.Reference=r'Human.B37.3'
        self.GeneModel=r'OmicsoftGene20130723'
        self.Replace='True'

        self.ParallelJobNumber='1'
        self.ThreadNumber="2"

        self.Config=self.LoadConfigFile()
        self.OscriptTemplate=self.SetOscriptTemplate()
        self.Log=''
        self.Oscript=''

        return

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

Begin MapRnaSeqReadsToGenome /Namespace=NgsLib /RunOnServer=True;
Files
"@FastqFilePath@";
Reference @Reference@;
GeneModel @GeneModel@;
Trimming /Mode=TrimByQuality /ReadTrimQuality=2;
Options
/ParallelJobNumber=@ParallelJobNumber@
/ThreadNumber=@ThreadNumber@
/PairedEnd=True /FileFormat=AUTO
/AutoPenalty=True /FixedPenalty=2 /Greedy=false /IndelPenalty=2
/DetectIndels=True /MaxMiddleInsertionSize=10 /MaxMiddleDeletionSize=10
/MaxEndInsertionSize=10 /MaxEndDeletionSize=10 /MinDistalEndSize=3
/ExcludeNonUniqueMapping=False /ReportCutoff=10
/OutputFolder="@OutputFolder@"
/InsertSizeStandardDeviation=40 /ExpectedInsertSize=300 /MatePair=False
/InsertOnSameStrand=False /InsertOnDifferentStrand=True /QualityEncoding=Automatic
/CompressionMethod=Gzip /Gzip=True /SearchNovelExonJunction=True /ExcludeUnmappedInBam=False
/KeepFullRead=False /Replace=@Replace@ /Platform=ILLUMINA /CompressBam=False;
Output RnaSeqBam;
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
        Oscript=Oscript.replace('@Reference@',self.Reference)
        Oscript=Oscript.replace('@GeneModel@',self.GeneModel)
        Oscript=Oscript.replace('@Replace@',self.Replace)
        Oscript=Oscript.replace('@ParallelJobNumber@',self.ParallelJobNumber)
        Oscript=Oscript.replace('@ThreadNumber@',self.ThreadNumber)

        Oscript=Oscript.replace('@ServerAddress@',self.ServerAddress)
        Oscript=Oscript.replace('@ServerUserId@',self.ServerUserId)
        Oscript=Oscript.replace('@ServerUserPsw@',self.ServerUserPsw)

        self.Oscript=Oscript

        return(self.Oscript)

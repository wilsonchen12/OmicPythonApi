from OmicPythonApi.Core.OmicPythonApi import *
class FetchSampleMetaDataAndSampleFilePath(OmicPythonApi):
    """A python api for that runs FetchSampleMetaData and SampleFilePath oscripts, add a FilePath column in sample metadata table, and save the combined table as a text file.
        See Oscript and Log fields in the class object for details of the oshell jobs.
        Please refer to Omicsoft Wiki pages for details of the commands in Oscript.
    Wilson Chen, Omicsoft, 20171201
    """
    def __init__(self,ServerAddress='',ServerUserId='',ServerUserPsw='',SampleSetId='',OutputFile=''):
        """Input:
            1. ServerAddress
            2. ServeruserId
            3. SampleSetId
            Output: an initialized obj. Use obj.Run function to run the oscripts.
        """
        self.ServerAddress=ServerAddress
        self.ServerUserId=ServerUserId
        self.ServerUserPsw=ServerUserPsw
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
Command FetchSampleMetaData;
Options
"
SampleSetID=SampleSetId0
";
OutputFile "SampleMetaDataOutputFile";
End;

Begin ExecuteCommand /Namespace=Server;
Server "ServerAddress" /UserID=ServerUserId /Password=ServerUserPsw;
Command FetchSampleFilePaths;
Options
"
SampleSetID=SampleSetId0
ReturnsTable=True
";
OutputFile "SampleFilePathOutputFile";
End;
        """
        return(self.OscriptTemplate)

    def MakeOscript(self,SampleSetId,SampleMetaDataOutputFile,SampleFilePathOutputFile):
        """Modify Oscript
        Wilson Chen, 20171130"""
        print('Make oscript')
        Oscript=self.OscriptTemplate
        Oscript=Oscript.replace('SampleSetId0',SampleSetId)
        Oscript=Oscript.replace('SampleMetaDataOutputFile',SampleMetaDataOutputFile)
        Oscript=Oscript.replace('SampleFilePathOutputFile',SampleFilePathOutputFile)
        Oscript=Oscript.replace('ServerAddress',self.ServerAddress)
        Oscript=Oscript.replace('ServerUserId',self.ServerUserId)
        Oscript=Oscript.replace('ServerUserPsw',self.ServerUserPsw)

        self.Oscript=Oscript

        return(self.Oscript)

    def MergeSampleMetaAndPathFile(self,SampleMetaDataFile,SampleFilePathFile,OutputFile):
        """Merge sample metadata and file path fetched from Arrray server
        Input: 1. SampleMetaDataFile - metadata output file from FetchSampleMetaData Proc
               2. SampleFilePathFile - filepath output file from FetchSampleMetaData Proc
        Output: OutputFile - A text file path that includes both Metadata and filepath (ready to use in Sample Registration)
        Wilson Chen, 20171130
               """
        import re

        print('Merge metadata and file path')
        SampleFilePath=dict()
        with open(SampleFilePathFile,'r') as fid:
            next(fid)
            for line in fid:
                if re.findall('\t',line):
                    SampleFilePath[line.split('\t')[0]]=line.split('\t')[1].replace('\n','')

        with open(OutputFile,'w') as fid0:
            with open(SampleMetaDataFile,'r') as fid:
                next(fid)
                for line in fid:
                    Id1=line.split('\t')[0]
                    if Id1=='\n':
                        continue
                    elif Id1=='SampleID':
                        line=line.replace(Id1,Id1+'\t'+SampleFilePath[Id1])
                    else:
                        line=line.replace(Id1,Id1+'\t'+SampleFilePath[Id1])
                    fid0.write(line)

    def Run(self):
        """Run the oscript from oshell
        Input: SampleSetId0 - sampleset id that will be queried in Array Server
        Output: OutputFile - A text file that have sample metadata and file path
        Wilson Chen, 20171130"""
        import os

        SampleMetaDataOutputFile=os.path.join(os.path.split(self.OutputFile)[0],'temmeta'+os.path.split(self.OutputFile)[-1])
        SampleFilePathOutputFile=os.path.join(os.path.split(self.OutputFile)[0],'tempath'+os.path.split(self.OutputFile)[-1])

        self.Oscript=self.MakeOscript(self.SampleSetId,SampleMetaDataOutputFile,SampleFilePathOutputFile)

        self.RunOscriptFromOshell(self.Oscript)

        self.MergeSampleMetaAndPathFile(SampleMetaDataOutputFile,SampleFilePathOutputFile,self.OutputFile)

        print('Remove temp files')
        os.remove(SampleMetaDataOutputFile)
        os.remove(SampleFilePathOutputFile)
        print(self.Log)
        return(self.Log)

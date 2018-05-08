#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Examples of running OmicPythonApi pacakge
Wilson Chen, Omicsoft, 2018-3-14
"""
#Load OmicPythonApi package
import site
#site.addsitedir(r'/IData/Users/wilson/document/Script_Library/Python/OmicPythonApi_001')
site.addsitedir(r'Z:\Users\wilson\document\Script_Library\Python\OmicPythonApi_Development')
import OmicPythonApi as Oapi

import os
import pandas as pd

# Set up parameters that will be used in the api
ServerAddress=r'tcp://192.168.3.226:9065'
ServerUserId='omicsoft'
ServerUserPsw='xxx'
SampleSet='OmicsoftTest_SampleSet_20171128'
ProjectPattern='2016'
OutputFolder='/local_data/tem'

ProjectId='20180309_test1'

FastqFilePath="""/IData/Users/QA_QC_Team/input/StandardDataset/RNA-Seq/Fastq/TestData1.1.fastq.gz
/IData/Users/QA_QC_Team/input/StandardDataset/RNA-Seq/Fastq/TestData1.2.fastq.gz"""

#Test in linux
#OutputFile='/IData/Users/wilson/tem1/20180308.txt'
#InputTableFile='/local/scratch/tem/TestSample.FullMetaData.txt'
#OutputFolderAbsPath='/local/data/tem'
#SampleSetFilePath=r'/IData/Users/wilson/document/Script_Library/Python/OmicPythonApi_001/OmicPythonApi/examples/testData/SampleNames_TCGA.txt'

#Test in windows
OutputFile=r'Z:\Users\wilson\tem1\20180308.txt'
InputTableFile=r'Z:\Users\wilson\tem1\TestSample.FullMetaData.txt'
OutputFolderAbsPath=r'Z:\Users\wilson\tem1'
SampleSetFilePath=r'Z:\Users\wilson\document\Script_Library\Python\OmicPythonApi_001\OmicPythonApi\examples\testData\SampleNames_TCGA.txt'

#Run listdatas api
a1=Oapi.ListLands()
a1.OutputFolder=OutputFolderAbsPath
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()
df1=pd.read_csv(os.path.join(OutputFolderAbsPath,'ListLands.txt'),sep='\t',header=None)
print(df1.head())

#Run ListSampleSets api, which export all sampletsets in TCGA_B37 to text files
a1=Oapi.ListSampleSets()
a1.Land='TCGA_B37'
a1.OutputFolder=OutputFolderAbsPath
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()

df1=pd.read_csv(os.path.join(OutputFolderAbsPath,'ListSampleSets.txt'),sep='\t')
print(df1.head())

#Run ListGeneSets api, which export all genesets in TCGA_B37 land to text files.
a1=Oapi.ListGeneSets()
a1.Land='TCGA_B37'
a1.OutputFolder=OutputFolderAbsPath
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()

df1=pd.read_csv(os.path.join(OutputFolderAbsPath,'ListGeneSets.txt'),sep='\t')
print(df1.head())

#Run AddArrayLandSampleSet api, which which add a sampleset to TCGA_B37 land.
a1=Oapi.AddArrayLandSampleSet()
a1.Land='TCGA_B37'
a1.SampleSetName='OmicPythonApi_Test2'
a1.File=SampleSetFilePath
a1.Tag='Wilson_test_20180314'
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()

#Run TextDumpArrayLandSampleData api, which which produce text files based on query results in TCGA_B37 land.
a1=Oapi.TextDumpArrayLandSampleData()
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Land='TCGA_B37'
a1.DataMode='Expression_Ratio'
a1.Sample=r'TCGA-01-0628-11A,TCGA-01-0629-11A'
a1.DownloadFullMetaData='True'
a1.OutputFolder=OutputFolderAbsPath
a1.Output='TestSample'
a1.Run()

print(os.listdir(a1.OutputFolder))

#Run TextDumpArrayLandSampleData api, which which produce text files based on query results in TCGA_B37 land.
a1=Oapi.TextDumpArrayLandGeneData()
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Land='TCGA_B37'
a1.DataMode='Expression_Ratio'
a1.SampleSet=r'OmicPythonApi_Test1'
a1.GeneSet='erg,mdm2'
a1.DownloadFullMetaData='True'
a1.OutputFolder=OutputFolderAbsPath
a1.Output='TestGeneSet'
a1.Run()

print(os.listdir(a1.OutputFolder))

#Run DownloadSampleSet api, which which produce text files based on query results in TCGA_B37 land.
a1=Oapi.DownloadSampleSet()
a1.Land='TCGA_B37'
a1.SampleSet='OmicPythonApi_Test1'
a1.OutputFolder=OutputFolderAbsPath
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()

df1=pd.read_csv(os.path.join(a1.OutputFolder,'DownloadSampleSet.txt'),sep='\t',header=None)
print(df1.head())

#Run DownloadGeneSet api, which which produce text files based on query results in TCGA_B37 land.
a1=Oapi.DownloadGeneSet()
a1.Land='TCGA_B37'
a1.GeneSet='LandRApiTest'
a1.OutputFolder=OutputFolderAbsPath
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()
df1=pd.read_csv(os.path.join(a1.OutputFolder,'DownloadGeneSet.txt'),sep='\t',header=None)
print(df1.head())

#Run DownloadMetaData api, which which produce text files based on query results in TCGA_B37 land.
a1=Oapi.DownloadMetaData()
a1.Land='TCGA_B37'
a1.OutputFolder=OutputFolderAbsPath
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()
df1=pd.read_csv(os.path.join(a1.OutputFolder,'DownloadMetaData.txt'),sep='\t',header=0)
print(df1.head())

#Run ListDataAvailability api, which which produce text files based on query results in TCGA_B37 land.
a1=Oapi.ListDataAvailability()
a1.Land='TCGA_B37'
a1.OutputFolder=OutputFolderAbsPath
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()
df1=pd.read_csv(os.path.join(a1.OutputFolder,'ListDataAvailability.txt'),sep='\t',header=0)
print(df1.head())

#Run DownloadArrayLandGeneComparison api, which which produce text files based on query results in HumanDisease_B37'.
a1=Oapi.DownloadArrayLandGeneComparison()
a1.Land='HumanDisease_B37'
a1.GeneSet='MET,egfr,braf,Kras'
a1.ComparisonSet=r'GSE13887.GPL570.test1,GSE13849.GPL570.test1,GSE13849.GPL570.test2'
a1.OutputFolder=OutputFolderAbsPath
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()
df1_CpGenes=pd.read_csv(os.path.join(a1.OutputFolder,a1.Output+'.Comparison.Genes.txt'),sep='\t',header=0)
df1_Cp=pd.read_csv(os.path.join(a1.OutputFolder,a1.Output+'.Comparison.txt'),sep='\t',header=0)
df1_Meta=pd.read_csv(os.path.join(a1.OutputFolder,a1.Output+'.FullComparisonMetaData.txt'),sep='\t',header=0)
print(df1_CpGenes.head())
#Run DownloadArrayLandComparisonData api, which which produce text files based on query results in HumanDisease_B37'.
a1=Oapi.DownloadArrayLandComparisonData()
a1.Land='HumanDisease_B37'
a1.ComparisonSet=r'GSE13887.GPL570.test1,GSE13849.GPL570.test1,GSE13849.GPL570.test2'
a1.OutputFolder=OutputFolderAbsPath
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()
df1_CpGenes=pd.read_csv(os.path.join(a1.OutputFolder,a1.Output+'.Comparison.Genes.txt'),sep='\t',header=0)
df1_CpGenes_Design=pd.read_csv(os.path.join(a1.OutputFolder,a1.Output+'.Comparison.Genes.txt'),sep='\t',header=0)
df1_Cp=pd.read_csv(os.path.join(a1.OutputFolder,a1.Output+'.Comparison.txt'),sep='\t',header=0)
df1_Meta=pd.read_csv(os.path.join(a1.OutputFolder,a1.Output+'.FullMetaData.txt'),sep='\t',header=0)
print(df1_Cp.head())
#Run TextDumpArrayLandGeneComparison api, which which produce text files based on query results in HumanDisease_B37'.
a1=Oapi.TextDumpArrayLandGeneComparison()
a1.Land='HumanDisease_B37'
a1.GeneSet='MET,egfr,braf,Kras'
a1.ComparisonSet=r'GSE13887.GPL570.test1,GSE13849.GPL570.test1,GSE13849.GPL570.test2'
a1.OutputFolder=OutputFolderAbsPath
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()
df1_Cp=pd.read_csv(os.path.join(a1.OutputFolder,a1.Output+'.Comparison.txt'),sep='\t',header=0)
df1_CpMx=pd.read_csv(os.path.join(a1.OutputFolder,'Comparison.matrix.txt'),sep='\t',header=0)
df1_Meta=pd.read_csv(os.path.join(a1.OutputFolder,a1.Output+'.FullMetaData.txt'),sep='\t',header=0)
print(df1_Cp.head())

#Run TextDumpArrayLandComparisonData api, which which produce text files based on query results in HumanDisease_B37'.
a1=Oapi.TextDumpArrayLandComparisonData()
a1.Land='HumanDisease_B37'
a1.ComparisonSet=r'GSE13887.GPL570.test1,GSE13849.GPL570.test1,GSE13849.GPL570.test2'
a1.OutputFolder=OutputFolderAbsPath
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()
df1_Cp=pd.read_csv(os.path.join(a1.OutputFolder,a1.Output+'.Comparison.txt'),sep='\t',header=0)
df1_CpMx=pd.read_csv(os.path.join(a1.OutputFolder,'Comparison.matrix.txt'),sep='\t',header=0)
df1_Meta=pd.read_csv(os.path.join(a1.OutputFolder,a1.Output+'.FullComparisonMetaData.txt'),sep='\t',header=0)
print(df1_Cp.head())
#Run DownloadComparisonSet api, which which produce text files based on query results in HumanDisease_B37'.
a1=Oapi.DownloadComparisonSet()
a1.Land='HumanDisease_B37'
a1.ComparisonSet=r'WilsonComparisonSetTest'
a1.OutputFolder=OutputFolderAbsPath
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()
df1_CpSet=pd.read_csv(os.path.join(a1.OutputFolder,'DownloadComparisonSet.txt'),sep='\t',header=0)
print(df1_CpSet.head())

#Run FetchSampleSetMetaData api, which which produce text file that contain sample metadata'.
a1=Oapi.FetchSampleSetMetaData()
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.SampleSetId=SampleSet
a1.OutputFile=OutputFile
a1.Run()

#Run IA_SearchPublishedProjects api, which which produce text files that (published) project ids in the array server'.
a1=Oapi.IA_SearchPublishedProjects()
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.ProjectPattern=ProjectPattern
a1.OutputFile=OutputFile
a1.Run()

#Run ImportTableToLocalProject api, which creates a local project and import a table to the local project'.
a1=Oapi.ImportTableToLocalProject()
a1.ProjectId='20180308_test_project'
a1.ProjectFolderPath=OutputFolderAbsPath
a1.InputTableFilePath=InputTableFile
a1.Run()

#Run FetchSampleMetaDataAndSampleFilePath api, which which produce text file that contain sample path and metadata'.
a1=Oapi.FetchSampleMetaDataAndSampleFilePath()
a1.SampleSetId=SampleSet
a1.OutputFile=OutputFile
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()

#Run MapRnaSeqReadsToGenomeInNewServerProject api, which which creates a server project and perform rnaseq alignment'.
a1=Oapi.MapRnaSeqReadsToGenomeInNewServerProject()
a1.ProjectId=ProjectId
a1.Files=FastqFilePath
a1.OutputFolder=OutputFolder
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()

#Run MapRnaSeqReadsToGenomeInNewServerProject api, which which creates a server project and rnaseq pipeline'.
a1=Oapi.RnaSeqPipelineInNewServerProject()
a1.ProjectId=ProjectId
a1.Files=FastqFilePath
a1.OutputFolder=OutputFolder
a1.ServerAddress=ServerAddress
a1.ServerUserId=ServerUserId
a1.ServerUserPsw=ServerUserPsw
a1.Run()

#Run ManageUsers_Add api, which which creates an user account in ArrayServer.
a1=Oapi.ManageUsers_Add()
a1.ServerAddress="tcp://192.168.3.226:9065"
a1.ServerUserId="admin"
a1.ServerUserPsw="omicsoft"

a1.UserID="wilson4"
a1.UserGroups="standard users,editors,curators, testusergroup2"
a1.Password="xxx"
a1.FullName ="Wilson Test"
a1.Organization="Omicsoft"
a1.Department="Support"
a1.Laboratory="lab1"
a1.Position="Scientist"
a1.Notes="notes"
a1.Email="test@qiagen.com"
a1.Phone="919-439-xxxx"
a1.Address="xxxx"

a1.Run()

#Run custom oscripts
a1=Oapi.OmicPythonApi()
a1.Oscript=r"""Begin ExecuteCommand /Namespace=Server;
Server "tcp://192.168.3.226:9065" /UserID=xxx /Password=xxx;
Command IA_FetchSampleIDs;
Options
"
SampleSetID=OmicsoftTest_SampleSet_20171128
";
OutputFile "Z:\Users\wilson\support\oscript\output\test_20180321.txt";
End;

Begin ConnectServer;
Server "tcp://192.168.3.226:9065" /UserID=xxx /Password=xxx;
End;

Begin ListDataAvailability /Namespace=Land;
Land TCGA_B38;
Options /OutputFolder="Z:\Users\wilson\support\oscript\output";
End;
"""
a1.Run()
print(a1.Log)


a1=Oapi.OmicPythonApi()
a1.Oscript="""
Begin ExecuteCommand /Namespace=Server;
Server "tcp://192.168.3.226:9065" /UserID=test /Password=xxx;
Command ManageUsers_Add;
Options
"
UserID=wilson3
UserGroups={standard users,test,test2}
Password=omicsoft
FullName =Wilson Test
Organization=Omicsoft
Department=Support
Laboratory=lab1
Position=Scientist
Notes=notes
Email=test@qiagen.com
Phone=919-439-xxxx
Address=xxxx
";
End;
"""
a1.Run()

a1=Oapi.ImportMicroarrayTableToLocalProject()
a1.MicroarrayTableFilePath=r'Z:\Users\QA_QC_Team\input\StandardDataset\Microarray\MicroArray_MatrixData1.txt'
a1.AnnotationTableFilePath=r'Z:\Users\QA_QC_Team\input\StandardDataset\Microarray\MicroArray_MatrixData1_Annotation.txt'
a1.DesignTableFilePath=r'Z:\Users\QA_QC_Team\input\StandardDataset\Microarray\AffyMetrixCell_dbpts_rat\dbpts.design.txt'
a1.ProjectId='test2'
a1.ProjectFolderPath=r'C:\Users\chenwi\tem'
a1.NameOfImportedOmicdata='test2'
a1.Run()
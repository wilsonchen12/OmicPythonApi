# OmicPythonApi
Wilson Chen, Omicsoft   
2018/03/09

# Description
OmicPythonApi was designed to be a python package that allows users to run oscript via oshell within Python. Input to OmicPythonApi normally is identical to the corresponding oscripts. The output of OmicPythonApi totally depends on the oscripts behind OmicPythonApi.

Users may retrieve the oscripts of an OmicPythonApi object in its Oscript field. Users may refer to Omicsoft Wiki for input parameters and output of the corresponding oscripts.

To perform land queries, users may use the apis in this package to download query results to text files, then use other Python packages ( (Pandas etc) to load the text files and perform downstream analysis.

The key field and functions in class OmicPythonApi and its child class are a oscriptTemplate field, a oscript field, a SetOscriptTemplate, a MakeOscript and a RunOscriptFromOshell function. OscriptTemplate holds a oscript template whose input parameters will be set by SetOscriptTemplat function. MakeOscript function modifies the input field in OscriptTemplate field using input from __init__. RunOscriptFromOshell submits oscripts to oshell.

Advanced users may also develop their in-house wrappers by extending the core class (OmicPythonApi) in the package. This can normally be done by overload __init__, SetOscriptTemplate and Makeoscript functions.

OmicPythonApi requires Oshell and Python 3.6.

OmicPythonApi was tested in Windows 10 and Centos7.

# Instruction
1. Unzip OmicPythonApi.zip to a desired location (called InstallationFolder).
2. Update the mono and oshell path in OmicPythonApi.cfg file. If Oshell was installed in windows, either comment MonoPath line with //, or set it to a space character.
3. Include the following lines into your python code in order to import OmicPythonApi package:
```
	import site
	import os
	OapiPkgLocation=os.path.split(InstallationFolder)
	site.addsitedir(OapiPkgLocation)
	import OmicPythonApi as Oapi
```
3. Use the Oapi as regular packages in your source code.

# Example 1: List all functions/values in OmicPythonApi and get help
```
dir(Oapi)
?Oapi.TextDumpArrayLandSampleData()
```

# Example 2: Use build-in APIs:
Below is an example to run TextDumpArrayLandSampleData (a python wrapper class of TextDumpArrayLandSampleData the oscript). More examples are in ./examples folder.

```
import site
import os
site.addsitedir(r'/IData/Users/wilson/document/Script_Library/Python/OmicPythonApi_001')
import OmicPythonApi as Oapi
a1=Oapi.TextDumpArrayLandSampleData()
a1.ServerAddress=r'tcp://192.168.3.226:9065'
a1.ServerUserId='omicsoft'
a1.ServerUserPsw='xxxx'
a1.LandName='TCGA_B37'
a1.DataMode='Expression_Ratio'
a1.Sample=r'TCGA-01-0628-11A,TCGA-01-0629-11A'
a1.DownloadFullMetaData='True'
a1.OutputFolder='/local_data/tem'
a1.Output='TestSample'
a1.Run()
#View oshell log
print(a1.Log)
#View results from oscripts.
os.listdir(a1.OutputFolder)
#User may load the text files that were generated from the api into Python, and perform custom analysis within Python environment
```
# Example 3: Run an oscript from python
```
a1=Oapi.OmicPythonApi()

a1.Oscript=r"""Begin ExecuteCommand /Namespace=Server;
Server "tcp://192.168.3.226:9065" /UserID=chenx57 /Password=omicsoft;
Command IA_FetchSampleIDs;
Options
"
SampleSetID=OmicsoftTest_SampleSet_20171128
";
OutputFile "Z:\Users\wilson\support\oscript\output\test_20180321.txt";
End;"""

a1.Run()

print(a1.Log)
```

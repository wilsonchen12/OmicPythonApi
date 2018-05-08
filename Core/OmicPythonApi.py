# -*- coding: utf-8 -*-
import os

class OmicPythonApi():
    """A prototype class for the Python Api. It runs oscripts (self.Oscript) from oshell (configured in self.Config)
    Child class will overload __init__, reload SetOscriptTemplate and MakeOscript functions for a specified oscript analysis
    The child Api will use Run function to launch oshell to run oscripts in obj.Oscript field
	Wilson Chen, Omicsoft, 20171201"""
    Version='1.1'
	ReleaseDate='20180502'
    Config=''
    OscriptTemplate=''
    Oscript=''
    Log=''

    def __init__(self):
        #Set parameters for oscript

        #__init__ialize class variables
        self.OscriptTemplate=self.SetOscriptTemplate()
        self.Config=self.LoadConfigFile()
        return

    def LoadConfigFile(self,ConfigFile=''):
        """Load Configuration file for the API, return a dictionary that has config parameters (mono)
        Wilson Chen, 20171201"""
        import re
        import os

        print('Load configuration...')

        if ConfigFile=='':
            ConfigDir=os.path.split(__file__)[0]
            ConfigDir=os.path.split(ConfigDir)[0]
            ConfigFile=os.path.join(ConfigDir,r'OmicPythonApi.cfg')

        self.Config=dict()
        with open(ConfigFile,'r') as fid:
            for line in fid:
                if re.findall('^//',line):
                    continue
                item=[x.strip() for x in line.split(r'=')]
                self.Config[item[0]]=item[1]
        return self.Config

    def SetOscriptTemplate(self):
        """A place holder for oscript template"""
        self.OscriptTemplate=''
        return(self.OscriptTemplate)

    def MakeOscript(self):
        """The function to customize the oscript by replacing parameter values with input from __init__ function """
        self.Oscript=''
        return(self.Oscript)

    def RunOscriptFromOshell(self,Oscript):
        """A Wrapper that lauch Oshell and Run oscript from Oshell in windows and linux
        Input: Oscript - A text string
        Wilson Chen, 20171201
"""

        from datetime import datetime
        import subprocess
        import os
        from random import randint
        from sys import platform

        print('Lauching Oshell and Running Oscript')
        if self.Config=='' or not self.Config:
            print('Config does not exit, please load config file')

        TempFolder=self.Config['OshellTempFolder']
        oshellPath=self.Config['OshellPath']
        basePath=self.Config['OshellBasePath']
        monoPath=self.Config['MonoPath']

        TempOscriptFileId=''.join([datetime.today().strftime('%Y%m%d%H%M'),str(randint(1,1000000))])
        TempOscriptPath=os.path.join(TempFolder,TempOscriptFileId+r'.oscript')
        with open(TempOscriptPath,'w') as fid:
            fid.write(Oscript)

        if 'win' in platform:
            result=subprocess.run([os.path.join(oshellPath,r'oshell.exe'),'--runscript',basePath,TempOscriptPath,TempFolder],shell=True,stdout = subprocess.PIPE,stderr=subprocess.STDOUT)
        elif 'linux' in platform:
            result=subprocess.run([monoPath,os.path.join(oshellPath,r'oshell.exe'),'--runscript',basePath,TempOscriptPath,TempFolder],shell=False,stdout = subprocess.PIPE,stderr=subprocess.STDOUT)
        else:
            print(platform + 'is NOT supported')

        stdout=result.stdout.decode('utf-8')
        err=result.stderr
        if err:
            log=err.decode('utf-8')
            print('Oshell run failed, err message is:\n'+log)

        else:
            print('Oshell run completed, no error message.')
            log=stdout

        with open(os.path.join(TempFolder,TempOscriptFileId+r'.log'),'w') as fid:
            fid.write(log)
        self.Log=log
        return(self.Log)

    def Run(self):
        """Run the oscript from oshell"""
        if self.Oscript=='':
            self.Oscript=self.MakeOscript()
        self.Log=self.RunOscriptFromOshell(self.Oscript)
#        print(self.Log)
        if r'[Error]' in self.Log or r'Error occurred' in self.Log:
            print(self.Log)
            print('Warning: Error in running the oscript')
        else:
            print('No error found in oshell log')
        return

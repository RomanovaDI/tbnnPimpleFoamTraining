import subprocess as sp
import numpy as np
import pandas as pd
import fileinput as fi

def timeStepsList(DNSfolder):
	sp.call('rm timeStepsList.txt; ls -1 -d '+DNSfolder+'[0-9]* |xargs -n1 basename > timeStepsList.txt', shell=True)
	timeStepsList = np.loadtxt("timeStepsList.txt", dtype=str)
	index = np.argsort(timeStepsList.astype(np.float))
	timeStepsList = timeStepsList[index]
	return timeStepsList[1:]

def prepareFolders(DNSfolder, RANSfolder, TSL):
	sp.run('rm -rf '+RANSfolder, shell=True, check=True)
	sp.run('cp -r '+RANSfolder+'_origBM '+RANSfolder, shell=True, check=True)
	sp.run('cd '+RANSfolder+'; '\
			'sed -i "s/timesPatterns/'+' '.join(TSL)+'/g\" run; '\
			'./run',
			shell=True, check=True)

def main():
	DNSfolder = 'preciseCalculationLES/'
	TSL = timeStepsList(DNSfolder)
	MLturbRANSfolder = 'TPF'
	KEturbRANSfolder = 'KEIF'
	KWturbRANSfolder = 'KWIF'
	prepareFolders(DNSfolder, MLturbRANSfolder, TSL)
#	prepareFolders(DNSfolder, KEturbRANSfolder, TSL)
#	prepareFolders(DNSfolder, KWturbRANSfolder, TSL)

if __name__ == "__main__":
	main()

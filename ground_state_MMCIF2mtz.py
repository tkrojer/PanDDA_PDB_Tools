#!/usr/bin/env python

import os,glob
import sys


def parseMMCIF(mmcif,targetDir):
    mmcifBlock = ''
    addLines = False
    nBlock = 1
    for line in open(mmcif):
        if line.startswith('data_') and addLines is True:
            addLines = False
            writeMMCIFblock(mmcifBlock,targetDir,nBlock)
            convertToMTZ(targetDir,nBlock)
            mmcifBlock = ''
            nBlock += 1
        if line.startswith('data_') and addLines is False:
            addLines = True
        if addLines:
            mmcifBlock += line

def writeMMCIFblock(mmcifBlock,targetDir,nBlock):
    n = (4-len(str(nBlock)))*'0'+str(nBlock)
    os.chdir(targetDir)
    if not os.path.isdir('crystal_' + str(n)):
        os.mkdir('crystal_' + str(n))
    os.chdir('crystal_' + str(n))
    f = open('crystal_' + str(n) + '.mmcif','w')
    f.write(mmcifBlock)
    f.close()

def getSymmFromMMCIF(mmcif):
    smiles = ''
    for line in open(mmcif):
        if line.startswith('_cell.length_a '):
            a = line.split()[1].replace('\n','').replace('\r','')
        if line.startswith('_cell.length_b '):
            b = line.split()[1].replace('\n','').replace('\r','')
        if line.startswith('_cell.length_c '):
            c = line.split()[1].replace('\n','').replace('\r','')
        if line.startswith('_cell.angle_alpha '):
            alpha = line.split()[1].replace('\n','').replace('\r','')
        if line.startswith('_cell.angle_beta '):
            beta = line.split()[1].replace('\n','').replace('\r','')
        if line.startswith('_cell.angle_gamma '):
            gamma = line.split()[1].replace('\n','').replace('\r','')
        if line.startswith('_symmetry.Int_Tables_number '):
            symm = line.split()[1].replace('\n','').replace('\r','')
        if line.startswith('_diffrn.details'):
            smiles = line[line.find('soaked compound:')+16:line.rfind('"')]
    unitCell = a + ' ' + b + ' ' + c + ' ' + alpha + ' ' + beta + ' ' + gamma
    return unitCell, symm, smiles

def saveSmailes(nBlock,smiles):
    if smiles != '':
        print('found information about soaked compound in MMCIF block; saving {0!s} in crystal_{1!s}.smiles'.format(smiles,nBlock))
        f = open('crystal_' + str(nBlock) + '.smiles','w')
        f.write(smiles)
        f.close()

def convertToMTZ(targetDir,nBlock):
    n = (4-len(str(nBlock)))*'0'+str(nBlock)
    os.chdir(os.path.join(targetDir,'crystal_' + str(n)))
    print('converting MMCIF block #{0!s} to MTZ in directory {1!s}'.format(nBlock,os.path.join(targetDir,'crystal_' + str(n))))
    unitCell, symm, smiles = getSymmFromMMCIF('crystal_' + str(n) + '.mmcif')
    cmd = ( 'cif2mtz hklin crystal_{0!s}.mmcif hklout crystal_{1!s}.mtz << eof > cif2mtz.log\n'.format(n,n) +
            ' symmetry %s\n' %symm +
            ' cell %s\n' %unitCell +
            'eof\n'  )
    os.system(cmd)
    saveSmailes(n,smiles)

if __name__ == '__main__':
    mmcif = sys.argv[1]
    targetDir = sys.argv[2]
    parseMMCIF(mmcif,targetDir)

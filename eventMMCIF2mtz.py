#!/usr/bin/env python

import os,glob
import sys

def parseMMCIF(mmcif,root):
    mmcifBlock = ''
    foundEvent = False
    nEvent = 1
    for line in open(mmcif):
        if line.startswith('data_'):
            if foundEvent:
                writeMMCIF(root,nEvent,mmcifBlock)
                nEvent += 1
                foundEvent = False
            mmcifBlock = ''
        if line.startswith('_diffrn.details') and 'PanDDA event map' in line:
            foundEvent = True
        mmcifBlock += line
    if mmcifBlock != '':
        writeMMCIF(root,nEvent,mmcifBlock)

def writeMMCIF(root,nEvent,mmcifBlock):
    f = open(root+ '_event_' + str(nEvent) + '.mmcif', 'w')
    f.write(mmcifBlock)
    f.close()

def getSymmFromMMCIF(mmcif):
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
    unitCell = a + ' ' + b + ' ' + c + ' ' + alpha + ' ' + beta + ' ' + gamma
    return unitCell, symm

def convertToMTZ(root):
    for mmcif in glob.glob(root + '_event_*.mmcif'):
        unitCell, symm = getSymmFromMMCIF(mmcif)
        cmd = ( 'cif2mtz hklin %s hklout %s << eof\n' %(mmcif,root + '.tmp.mtz') +
                ' symmetry %s\n' %symm +
                ' cell %s\n' %unitCell +
                'eof\n'
                'cad hklin1 %s hklout %s << eof\n' %(root + '.tmp.mtz',mmcif.replace('.mmcif','.mtz')) +
                ' labin file_number 1 E1=FWT E2=PHWT \n'
                ' labout file_number 1 E1=F_event E2=PH_event \n'
                'eof\n'
                '/bin/rm %s\n' %(root + '.tmp.mtz')                )
        os.system(cmd)
        print(cmd)

if __name__ == '__main__':
    mmcif = sys.argv[1]
    root = mmcif.replace('.mmcif','').replace('.cif','')
    parseMMCIF(mmcif,root)
    convertToMTZ(root)

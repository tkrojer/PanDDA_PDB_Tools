#!/usr/bin/env python

import os,glob
import sys


def run_dimple(refPDB,targetDir):
    for dirs in sorted(glob.glob(os.path.join(targetDir,'*'))):
        sampleDir = dirs[dirs.rfind('/')+1:]
        if os.path.isdir(dirs):
            os.chdir(dirs)
            if os.path.isfile(sampleDir+'.mtz'):
                print('running DIMPLE on {0!s}'.format(dirs))
                cmd = (
                    'dimple {0!s} {1!s} dimple\n'.format(sampleDir+'.mtz',refPDB) +
                    'ln -s dimple/final* .'
                )
                os.system(cmd)


if __name__ == '__main__':
    refPDB = os.path.realpath(sys.argv[1])
    targetDir = os.path.realpath(sys.argv[2])
    run_dimple(refPDB,targetDir)
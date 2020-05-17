# PanDDA_PDB_Tools
A collections of simple python scripts which help to convert different MMCIF files from PanDDA PDB group depositions into easy to work with MTZ files. Some general information regarding PanDDA PDB group depositions can be found on openlabnotebooks.org: https://openlabnotebooks.org/update-on-batch-deposition-of-xchem-structures.

### Installation
Download the python scipts from github; then make them executable:
```
e.g.
chmod +x eventMMCIF2mtz.py
```
If you want to use them repeatedly, add the directory containing the scripts to your PATH variable. 
```
export PATH=/path/to/script:$PATH
e.g.
export PATH=/Users/tobiaskrojer/Scripts/eventMMCIF2mtz:$PATH
```
Note: you need to add this line to your .bashrc or .bash_profile file.

### Requirements
You need to have the CCP4 program suite installed, because the scripts use cif2mtz, cad and dimple.



## eventMMCIF2mtz.py
A python script which enables extraction of PanDDA event maps from MMCIF files downloaded from the Protein Ddata Bank (PDB).

### usage

Download an MMCIF file from the PDB website (e.g. 5R7Z) and run the script:
```
./eventMMCIF2mtz.py 5r7z-sf.cif
```
This will result in an MTZ file for each PanDDA event map in the MMCIF file, e.g.:
```
5r7z-sf_event_1.mtz
```
Start COOT and select "Open MTZ, mmCIF, fcf or phs...", then choose F_event as Amplitudes and PH_event as Phases.

Please note that the map sigma level is not meaningful. Also keep in mind that PanDDA event maps are local maps and only valid in the immediate neighbourhood of the modelled ligand.


## ground_state_MMCIF2mtz
This script takes a mulit-dataset MMCIF file from a PanDDA ground_state deposition and creates a folder for each MMCIF data block in the selected project directory. It then converts the each MMCIF file into an MTZ file. The resulting folder structure is ready to run the next script (run_dimple.py).

### usage
```
ground_state_MMCIF2mtz.py <mmcif_file> <project_directory>
e.g.
ground_state_MMCIF2mtz.py ground_state_0_sf.mmcif /Users/tobiaskrojer/PanDDA
```

## run_dimple.py
This script runs DIMPLE on all files in a given project directory prepared with ground_state_MMCIF2mtz.py. This is necessary because PanDDA needs a PDB, as well as an MTZ file to run.

### usage
First, download the PDB file of the ground_state deposition; then run run_dimple.py
```
run_dimple.py <reference_PDB_file> <project_directory>
e.g.
run_dimple.py 5r7x.pdb /Users/tobiaskrojer/PanDDA
```
Please note that the script runs the jobs sequentially and uses only one core, so it may take a couple of hours to finish.


## Additional information
* Pearce, N. M. et al. A multi-crystal method for extracting obscured crystallographic states from conventionally uninterpretable electron density. Nat Commun 8, 15123 (2017).
* Pearce, N. M. et al. Partial-occupancy binders identified by the Pan-Dataset Density Analysis method offer new chemical opportunities and reveal cryptic binding sites. Struct Dyn 4, (2017).
* Pearce, N. M., Krojer, T. & von Delft, F. Proper modelling of ligand binding requires an ensemble of bound and unbound states. Acta Cryst D 73, 256–266 (2017).
* https://pandda.bitbucket.io


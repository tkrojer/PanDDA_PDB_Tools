# eventMMCIF2mtz
A simple python script which enables extraction of PanDDA event maps from MMCIF files downloaded from the Protein Ddata Bank (PDB).

## Usage
Download eventMMCIF2mtz.py from github; then make it executable:
```
chmod +x eventMMCIF2mtz.py
```
If you want to use it repeatedly, add the directory containing the script to your PATH variable. 
```
export PATH=/path/to/script:$PATH
e.g.
export PATH=/Users/tobiaskrojer/Scripts/eventMMCIF2mtz:$PATH
```
Note: you need to add this line to your .bashrc or .bash_profile file.

Next, download an MMCIF file from the PDB website (e.g. 5R7Z) and run the script:
```
./eventMMCIF2mtz.py 5r7z-sf.cif
```
This will result in an MTZ file for each PanDDA event map in the MMCIF file, e.g.:
```
5r7z-sf_event_1.mtz
```
Start COOT and select "Open MTZ, mmCIF, fcf or phs...", then choose F_event as Amplitudes and PH_event as Phases.

Please note that the map sigma level is not meaningful. Also keep in mind that PanDDA event maps are local maps and only valid in the immediate neighbourhood of the modelled ligand.

## Requirements
* You need to have the CCP4 program suite installed, because the script uses cif2mtz and cad.

## Additional information
* Pearce, N. M. et al. A multi-crystal method for extracting obscured crystallographic states from conventionally uninterpretable electron density. Nat Commun 8, 15123 (2017).
* Pearce, N. M. et al. Partial-occupancy binders identified by the Pan-Dataset Density Analysis method offer new chemical opportunities and reveal cryptic binding sites. Struct Dyn 4, (2017).
* Pearce, N. M., Krojer, T. & von Delft, F. Proper modelling of ligand binding requires an ensemble of bound and unbound states. Acta Cryst D 73, 256–266 (2017).
* https://pandda.bitbucket.io



> **NOTICE**: As of 10/25/23 the main branch of chiLife now uses a new rotamer library format that is incompatible with older versions
> of chiLife. All rotlibs in this directory have been updated to the new format. If you are using an older version of 
> chiLife you must check out ``chiLife_rotlibs`` commit [``82059f4``](https://github.com/StollLab/chiLife_rotlibs/tree/82059f44b319e0a6494394c52000ddf7c9d50e5b) 
> or earlier for compatible libraries. 


# chiLife Rotamer Libraries Repository

The repo contains rotamer libraries for chiLife (https://github.com/StollLab/chilife). The purpose of this repo is to 
maintain a centralized collection of curated rotamer libraries so that they can be accessed easily and to ensure that 
they are compatible with future versions of chiLife. Note that the rotamers and weights of the library may change over 
time due to improvements in rotamer library performance, but previous versions should always be accessible through the 
``git`` versions.

> **NOTE**: There may be many duplicate rotamer libraries between FluorLables and SpinLabels, specifically for metal
> based labels. This is due to the fact that some spin active metals can also act as FRET acceptors. Currently, these 
> rotamer libraries are exactly the same, since there is no explicit FluorLabel object yet in chiLife. In the future 
> they will be different to facilitate experimental differences.

## Using these rotamer libraries
These rotamer libraries can be used individually or the repository can be downloaded and directories added to the 
chiLife rotamer library search directories using the ``chilife.add_rotlib_dir`` function. Note that each individual directory should be added 
separately and will persist until removed by the user or chilife is updated.


## Rotamer library info
Many of the rotamer libraries have non-intuitive names. More information about a given rotamer library can be found 
using the ``chilife.rotlib_info`` function. 

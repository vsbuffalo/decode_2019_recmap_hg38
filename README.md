# Processing of Decode (2019) recombination map

This small repository converts the range-based recombination map from
Halldorsson et al. (2019, https://www.science.org/doi/10.1126/science.aau1043)
to a HapMap-formatted recombination file.

If you find a bug or issue in this, please report it as a GitHub issue. 

## Inputs

 - `data/aau1043_datas3.gz` from
   https://www.science.org/doi/suppl/10.1126/science.aau1043/suppl_file/aau1043_datas3.gz.
   This was downloaded manually since using `wget` does not work. The journal
   *Science*'s webserver gives a 403: Forbidden HTTP error when using `wget`.
   So I have included the file in the repository, since it is relatively small. 

## Outputs

 - `decode_2019_recmap_hg38.txt`: produced by running the script
   `tools/convert_bed_to_hapmap.py`.

## Requirements

 - Python 3 (version 3.11.5 used)

## Steps

In the main directory: 

    $ make 

## Caveats and Warnings

Halldorsson et al. do not, unfortunately, specify whether their coordinates are
0 or 1-based. Given the format is BED-like, I *assume* it follows BED
conventions (0-based, right exclusive). 





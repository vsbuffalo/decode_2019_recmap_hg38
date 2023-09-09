# convert_bed_to_hapmap.py
# Vince Buffalo (2023)
#
# Used to convert the range-based recombination map from
# Halldorsson et al. (2019, https://www.science.org/doi/10.1126/science.aau1043)
# to a HapMap-formatted recombination file.

# NOTE: Halldorsson et al. do not, unfortunately, specify whether their
# coordinates are 0 or 1-based. Given the format is BED-like, I *assume*
# it follows BED conventions (0-based, right exclusive).

import sys
import gzip


def readfile(filename):
    is_gzip = filename.endswith('.gz')
    if is_gzip:
        return gzip.open(filename, mode='rt')
    return open(filename, mode='r')


last_chrom = None
last_pos = None
print("Chromosome\tPosition(bp)\tRate(cM/Mb)")
for line in readfile(sys.argv[1]):
    if line.startswith('#') or line.startswith('Chr'):
        continue
    chrom, start, end, rate, cumrate = line.strip().split('\t')
    start, end = int(start), int(end)
    if last_pos is not None and (start != last_pos and (chrom == last_chrom)):
        raise ValueError(f"recmap is not full coverage, cannot convert ({chrom}:{start}-{end})")
    print(f"{chrom}\t{start}\t{rate}")
    last_chrom = chrom
    last_pos = end

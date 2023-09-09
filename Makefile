
decode_2019_recmap_hg38.txt: data/input/aau1043_datas3.gz
	python tools/convert_bed_to_hapmap.py $< > $@

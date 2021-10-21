# Data processing scripts usage


### Converting from CSV to NPZ
python conv_csv_npz.py -i /hpcgpfs01/scratch/kyu/QImanging/run1 -o /hpcgpfs01/scratch/kyu/QImanging/run1/npz


### Finding borders of the beams on
python plot_toa_border2.py -i /hpcgpfs01/work/qem/data/Beamline/wire/run1/npz


### Extracting beam-on data and save into NPZ
python extract_burst.py -i /hpcgpfs01/work/qem/data/Beamline/wire/run1/npz -o /hpcgpfs01/work/qem/data/Beamline/wire/run1/image


### Visualizing the extract beam-on data
python make_image.py -i /hpcgpfs01/work/qem/data/Beamline/wire/run1/image/




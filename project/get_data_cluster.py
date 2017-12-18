import os
import hdf5_getters3 as hdf5_getters
from pyspark import SparkContext
import pickle

sc = SparkContext()

rows = []
rows.append(','.join(['track_id', 'song_hotttnesss', 'tempo'])+"\n")

counter = 0

covers = pickle.load(open("/home/desplace/track_ids.p","rb"))
size = len(covers)
print("Size of dataset =", size)

for track in covers:
	folder1 = track[2]
	folder2 = track[3]
	folder3 = track[4]
	folder_path = "/buffer/million-song/dataset/" + folder1 + "/" + folder2 + "/" + folder3 + "/"
	track_path = folder_path + track + ".h5"

	h5 = hdf5_getters.open_h5_file_read(track_path)
	track_id = hdf5_getters.get_track_id(h5)
	song_hotttnesss = hdf5_getters.get_song_hotttnesss(h5)
	tempo = hdf5_getters.get_tempo(h5)

	counter += 1
	if counter % (size/100) == 0:
		print(str(100*counter/size) + "%")

	row = [track_id, song_hotttnesss, tempo]
	row = map(lambda x : str(x),row)
	rows.append(', '.join(row)+"\n")

with open('/home/desplace/tempo_and_popularity.csv', 'w+') as f:
	f.writelines(rows)
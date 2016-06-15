# import here
import csv
import numpy as np

# path definition
g_input_dir = "post_data/"
g_input_file_name = "area1.csv"
g_write_dir = "post_proc_data/"
g_feature_number = 13
g_area_feature = np.array([])

# classes here

# functions here
def Read2Area():
  print "read scv"
  area_feature = np.array([])
  with open(g_input_dir + g_input_file_name, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      row_np = np.array(row)
      area_feature = np.vstack([area_feature, row_np]) if area_feature.size>0 else row_np
  return area_feature

# test desc here
g_area_feature = Read2Area()
g_date = g_area_feature[:,0]
g_order = g_area_feature[:,1:3]
g_traff = g_area_feature[:,4:7]
g_other = g_area_feature[:,8:10]
g_y = g_area_feature[:,11:12]

for i in range(300,302):
  print g_date[i]
  print g_order[i]
  print g_traff[i]
  print g_other[i]
  print g_y[i]

# main here

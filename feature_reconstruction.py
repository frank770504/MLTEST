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

def DataStr2Int(mat):
  mat_int = mat.astype(int)
  _sz_r, _sz_c = mat_int.shape
  for i in range(0, _sz_r):
    if mat[i,0] == 'NULL':
      mat_int[i,:] = np.ones(_sz_c) * -1
  return mat_int
    
# test desc here
g_area_feature = Read2Area()
g_date = g_area_feature[:,0]
g_order = g_area_feature[:,1:4]
g_traff = g_area_feature[:,4:8]
g_other = g_area_feature[:,8:11]
g_y = g_area_feature[:,11:13]

#~ g_date_int = DataStr2Int(g_date)
g_order_int = DataStr2Int(g_order)
g_traff_int = DataStr2Int(g_traff)
g_other_int = DataStr2Int(g_other)
g_y_int = DataStr2Int(g_y)
# string to numbers
# detect NULL
# interpolation

for i in range(96,98):
  print "-----{}-----".format(i)
  print g_date[i]
  print g_order_int[i]
  print g_traff_int[i]
  print g_other_int[i]
  print g_y_int[i]

# main here

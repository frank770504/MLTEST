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
class FeatureInterpolation:
  def __init__(self, raw_mat, period=1008):
    self.period_ = period
    self.null_ind_ = np.array([])
    self.mat_ = raw_mat
    self.mat_int_ = self.mat_.astype(int)
    # fill mat_int and find null_ind
    self.sz_r_, self.sz_c_ = self.mat_int_.shape
    for i in range(0, _self.sz_r_):
      if self.mat_[i,0] == 'NULL':
        self.mat_int_[i,:] = np.ones(self.sz_c_) * -1
        self.null_ind_= np.hstack([self.null_ind_, i])\
          if self.null_ind_.size>0 else np.array(i)
  def PeriodicMean(self, i):
    # find all the index
    s = 10000 - i
    ind = (10000 - np.array(range(s,10000,1008)))
    ind_fl = ind[:1:-1]
    small = a[ind_fl] - 1
    large = a[r:-1:1008] - 1
    ind = np.concatenate((small, large))
    # exclude -1
    # mean
    a = 1
  def GetMatInt(self):
    return self.mat_int_
  def GetNullInd(self):
    return self.null_ind_

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
  null_ind = np.array([])
  for i in range(0, _sz_r):
    if mat[i,0] == 'NULL':
      mat_int[i,:] = np.ones(_sz_c) * -1
      null_ind = np.hstack([null_ind, i]) if null_ind.size>0 else i
  return mat_int, null_ind
    
# test desc here

#~ g_area_feature = Read2Area()
#~ g_date = g_area_feature[:,0]
#~ g_order = FeatureInterpolation(g_area_feature[:,1:4])
#~ g_traff = FeatureInterpolation(g_area_feature[:,4:8])
#~ g_other = FeatureInterpolation(g_area_feature[:,8:11])
#~ g_y = FeatureInterpolation(g_area_feature[:,11:13])
#~ 
#~ g_order_int = g_order.GetMatInt()
#~ g_traff_int = g_traff.GetMatInt()
#~ g_other_int = g_other.GetMatInt()
#~ g_y_int = g_y.GetMatInt()

print range(0,10000,1008)
a = np.cumsum(np.ones(10000))
print a[0:-1:1008] - 1
print a[range(0,10000,1008)] - 1

#6049
r = 6048
s = 10000 - r
ind = (10000 - np.array(range(s,10000,1008)))
ind_fl = ind[:1:-1]
small = a[ind_fl] - 1
print small
large = a[r:-1:1008] - 1
print large
aaa = np.concatenate((small, large))
print aaa


# string to numbers
# detect NULL
# interpolation

#~ for i in range(96,98):
  #~ print "-----{}-----".format(i)
  #~ print g_date[i]
  #~ print g_order_int[i]
  #~ print g_traff_int[i]
  #~ print g_other_int[i]
  #~ print g_y_int[i]

#~ print g_traff.GetNullInd()
#~ print g_other.GetNullInd()

# main here

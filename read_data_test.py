# import here
import csv
import numpy as np

# path definition
g_csv_file_name = "order_traffic_weather.csv" # <-----------------file name here
g_area_number = 66
g_feature_number = 13
g_area_piles = np.array([]) # should be located
g_write_dir = "post_data/" # <-----------------------------------define dir here

# classes here
class Area:
  def __init__(self, area_id):
    self.id_ = area_id
    self.data_ = np.array([])
  def GetData(self):
    return self.data_
  def PileUp(self, food):
      self.data_ = np.vstack([self.data_, food]) if self.data_.size>0 else food

# functions here
def AreaPilesLocator():
  for i in range(1, g_area_number + 1): # 1 ~ 66
    temp_area = Area(i)
    if i == 1:
      area_piles = temp_area
    else:
      area_piles = np.hstack([area_piles, temp_area])
  return area_piles

def WriteAreaCSV(name, area_arr):
  with open(name, 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in area_arr:
      spamwriter.writerow(row)
  print "write {} ok !".format(name)

def Read2Area(area_piles):
  print "read scv"
  area_arr_temp = np.array([])
  with open(g_csv_file_name, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      # skip the first row
      if row[0].strip('\"') == "date":
        continue
      # use the information that 
      # area_id is less than the index in the "g_area_piles" by 1
      # get the area_id -- 1
      _id = np.int(row[2])
      # append the row behide the data in each corr. data -- 2
      row_np = np.array(row)
      area_piles[_id - 1].PileUp(row_np)
  return area_piles

# test desc here

# main here
g_area_piles = Read2Area(AreaPilesLocator())
for i in range(0, g_area_number):
  WriteAreaCSV(g_write_dir + "area{}.csv".format(i+1), g_area_piles[i].GetData())

# recycle bin
#==1==#
#~ cnt_arr = np.zeros(g_feature_number)
  #~ for i in range(0,12):
    #~ if row[i] == 'NULL':
      #~ cnt_arr[i] = cnt_arr[i] + 1


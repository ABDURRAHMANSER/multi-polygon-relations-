#!/usr/bin/env python
# coding: utf-8

# In[27]:


#NOTE:  download fastkml
# I used jupyter for solving this problem so if you do not use jubter please 
#download fastkml library befor going on.


from fastkml import  kml  # imort library for read kml file data 
from shapely.geometry import Polygon, MultiPolygon  # this function is for check is the polygon is side polygon


# In[28]:


kml_buildingfile = 'C:/Users/samis/Downloads/buildings.kml'
kml_districtsfile = 'C:/Users/samis/Downloads/districts.kml'

building_num_list = []

with open(kml_buildingfile, 'rb') as my_building_file:
    building_doc=my_building_file.read()  # open the building KML file 
    
with open(kml_districtsfile, 'rb') as my_districts_file:
    districts_doc=my_districts_file.read() # open the districts KML file 

building_k = kml.KML() # read building KML fiel 
building_k.from_string(building_doc)
building_outerFeature = list(building_k.features())
building_innerFeature = list(building_outerFeature[0].features())
building_placemarks = list(building_innerFeature[0].features())

districts_k = kml.KML()  # read disyricts KML fiel 
districts_k.from_string(districts_doc)
districts_outerFeature = list(districts_k.features())
districts_innerFeature = list(districts_outerFeature[0].features())
districts_placemarks = list(districts_innerFeature[0].features())

for districts in districts_placemarks:
    building_number = 0
    for buildings in building_placemarks:
            #print(building)
            #print(district.contains(building))
            if districts.geometry.contains(buildings.geometry):
                building_number += 1  # if the builging within the district increse the builging number by one
                #print(building_number)
                #print(districts.name, building.sympledata)
    building_num_list.append([districts.name, building_number]) # we are append the name of district and the number of building

        
my_building_file.close()
my_districts_file.close()


# In[29]:


top3list = []  # in this part I am itrate our building list for three time 
                # which make the function more efishent in case of time for find the biggest 3
biggest_item_num = 3
while len(top3list) < biggest_item_num:
    biggest = 0
    item2add = None
    for buildings_number in building_num_list:
        if buildings_number[1] > biggest:
            item2add = buildings_number
            biggest = buildings_number[1]
            
    top3list.append(item2add)
    building_num_list.remove(item2add)  # remove the biggest one from the list.


# In[30]:


print(top3list)


# In[ ]:





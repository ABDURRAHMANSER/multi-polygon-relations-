#!/usr/bin/env python
# coding: utf-8

# In[10]:


#NOTE:  download fastkml
# I used jupyter for solving this problem so if you do not use jubter please 
#download fastkml library befor going on.


from fastkml import  kml  # imort library for read kml file data 


# In[37]:


kml_buildingfile = 'C:/Users/samis/Downloads/buildings.kml'
kml_districtsfile = 'C:/Users/samis/Downloads/districts.kml'


with open(kml_buildingfile, 'rb') as myfile:
    building_doc=myfile.read()

k = kml.KML()
k.from_string(building_doc)

building_outerFeature = list(k.features())
building_innerFeature = list(building_outerFeature[0].features())

building_placemarks = list(building_innerFeature[0].features())

for buildings in building_placemarks:
    print( buildings.geometry)


# In[ ]:





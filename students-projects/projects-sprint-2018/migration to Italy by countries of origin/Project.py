
# coding: utf-8

# In[1]:


import csv

with open('/home/redi/Downloads/project.csv') as f:
    print(f.read())


# In[2]:


# # 2 Step - creating a dictionary with countries of origin
# def dictionary_countries_of_origin(data, country):
#     countries_of_origin_dict = []
#     for row in data:
#         if row[1] not in countries_of_origin_dict and row[7] == country:
#             countries_of_origin_dict.append(row[1])
#     return countries_of_origin_dict
# print(dictionary_countries_of_origin(data, 'ITA'))
# x = dictionary_countries_of_origin(data, 'ITA')

# 3 Step - calculating total arrivals for each country of origin
# def step_three(data, country):
#     total = 0
#     #totals_list = []
    
#     for i in x:
#         for row in data:
#             if row[1] == i and row[7] == country:
#                 total += int(row[2])
#     return total
# print(step_three(data, 'ITA'))


# In[14]:


import csv

# 1 Step - removing header and rewriting data without header
def data_without_header(filename):
    with open(filename) as f:
        data = csv.reader(f)
        header = next(data)    
        rows = []
        for x in data:
            rows.append(x)
            
    return header, rows
header, data = data_without_header('/home/redi/Downloads/project.csv')
#print(data)

# 2 Step - getting counties of arrivals and total arrivals
def function(country, data):
    total_arrivals = {}
    for row in data:
        if row[7] == country:
            country_of_origin = row[1]
            total = int(row[2].replace(',',''))
            total_arrivals[country_of_origin] = total + total_arrivals.get(country_of_origin, 0)
            
    return total_arrivals
print(function('ITA', data))

# 3 Step - drawing bar chart
import matplotlib.pyplot as plt
import random
from matplotlib import colors as mcolors

#def random_color():
    #return random.choice(list(mcolors.cnames.values()))
    #return random.choice(['b', 'r'])

plt.figure(figsize = (30,15))
new_var = function('ITA', data)
#plt.bar(new_var.keys(), new_var.values(), 0.7, color = [random_color() for x in new_var.keys()])

plt.bar(new_var.keys(), new_var.values(), 0.7, color = '#2574B0')
plt.xlabel('Country of origin',fontsize= '15')
plt.ylabel('Amount of arrivals', fontsize= '15')
plt.title('Total arrivals of migrants to Italy in 2017',fontsize= '25')

# Text on the top of each barplot
#for i in range(new_var.keys):
    #plt.text(x = new_var.keys[i]-0.5 , y = ew_var.values[i]+0.1, s = label[i], size = 6)
plt.show()


# In[4]:


import csv

# 1 Step - removing header and rewriting data without header
def data_without_header(filename):
    with open(filename) as f:
        data = csv.reader(f)
        header = next(data)    
        rows = []
        for x in data:
            rows.append(x)
            
    return header, rows
header, data = data_without_header('/home/redi/Downloads/project.csv')
#print(data)

# 2 Step - getting counties of arrivals and total arrivals
def function(country, data):
    total_arrivals = {}
    for row in data:
        if row[7] == country:
            country_of_origin = row[1]
            total = int(row[2].replace(',',''))
            total_arrivals[country_of_origin] = total + total_arrivals.get(country_of_origin, 0)
            
    return total_arrivals
print(function('GRC', data))

# 3 Step - drawing bar chart
import matplotlib.pyplot as plt

plt.figure(figsize = (20,10))
new_var = function('GRC', data)
plt.bar(new_var.keys(), new_var.values(), 0.7, color = 'b')
plt.xlabel('Code of original countries',fontsize= '13')
plt.ylabel('Total arrivals', fontsize= '13')
plt.title('Total arrivals of Migration to Greece in 2017',fontsize= '22')
plt.show()


# In[5]:


def gender_m_of_arrivals(data):
    result = {}
    for row in data:
        country = row[1]
        if row[3] != '':
            male = int(row[3])
            result[country] = male + result.get(male, 0)
        
    return result
print(gender_m_of_arrivals(data))

def gender_f_of_arrivals(data):
    result = {}
    for row in data:
        country = row[1]
        if row[4] != '':
            female = int(row[4])
            result[country] = female + result.get(female, 0)
        
    return result
print(gender_f_of_arrivals(data))


# In[6]:


import numpy as np
import matplotlib.pyplot as plt


N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()


# In[7]:


import numpy as np

import matplotlib.pyplot as plt

np.random.seed(0)


n_bins = 10

x = np.random.randn(1000, 2)


fig, ax = plt.subplots()


colors = ['red', 'blue']

ax.hist(x, color=colors, label=['Men', 'Women']) #[m,f]

ax.legend(prop={'size':10})

plt.show()


# In[8]:


import matplotlib.pyplot as plt

male_dict = gender_m_of_arrivals(data)

female_dict = gender_f_of_arrivals(data)

countries = male_dict.keys()
all_the_x = []
all_the_y = []

for country in countries:
    all_the_x.append(country+' male')
    all_the_x.append(country+' female')
    all_the_y.append(male_dict[country])
    all_the_y.append(female_dict[country])

print(all_the_x)

plt.figure(figsize=(20,10))
plt.xlabel('Country of origin')
plt.ylabel('Amounts of arrivals')
plt.title('Total arrivals to Italy in 2017 by genders',fontsize= '20')

plt.bar(all_the_x,all_the_y, 1, color=['#2574B0','#FFD900'])
plt.xticks(rotation='vertical')
plt.show()


# In[9]:


import csv
def get_country_names():
    header, data = data_without_header('/home/redi/Downloads/countries.codes.csv')
    data.append(header)
    iso_to_countries = {}
    for row in data:
        iso_to_countries[row[1]] = row[0]
    return iso_to_countries

code_dict = get_country_names()
print(code_dict['BRA'])
print(code_dict['TUR'])

print("The name for CIV is", code_dict["CIV"] +'.')


# In[10]:


import folium

from  geopy.geocoders import Nominatim
europe = [41.87194, 12.56738]
fmap = folium.Map(location=europe, zoom_start=3)
folium.CircleMarker(location=europe, 
    radius=20, color='black', fill=True).add_to(fmap)

### circles of ORIGINAL countries
# BGD=[23.684994,90.356331]
# folium.CircleMarker(location=BGD, 
#                    radius=20, color='red', fill=True).add_to(fmap)

def arrivals(country, data):
    total_arrivals = 0
    for row in data:
        if row[7] == "ITA" and row[1] == country:
            total_arrivals += int(row[2].replace(',',''))
            
    return total_arrivals


Country_Codes = ['BGD','CIV','CMR','CIV','ERI','GIN','GMB','IRQ','MAR','MLI','NGA','OOO','PAK','SDN','SEN','SOM','TUN']
Country_Names = [code_dict[x] for x in Country_Codes]
# Country_Names = [code_dict['CMR'],code_dict['CIV'],code_dict['ERI'],code_dict['GIN'],code_dict['GMB'],code_dict['IRQ']
                 
print(Country_Names)
                 
gloc = Nominatim()
for i,x in enumerate(Country_Names):
    floc = gloc.geocode(x)
    country_code = Country_Codes[i]
    migration = arrivals(country_code, data)
    folium.CircleMarker(popup = x + ' ' + str(migration), location=[floc.latitude, floc.longitude], 
radius=20, color='#2574B0', fill=True).add_to(fmap)
'''
# which countries do I want to show
countries = ['Greece', 'Italy', 'Germany']
colors = ['red', 'yellow', 'green']
folium.Map?
comb = zip(countries, colors)
folium.CircleMarker(location=europe, 
                    radius=20, color='black', fill=True).add_to(fmap)
gloc = Nominatim()
for x in comb:
    floc = gloc.geocode(x[0])
    folium.CircleMarker(location=[floc.latitude, floc.longitude], 
                    radius=20, color=x[1], fill=True).add_to(fmap)
'''
fmap


# In[11]:


import csv

new_list = []
for row in data:
    newrow = [x for x in row]
    newrow.append(code_dict[row[1]])
    new_list.append(newrow)
print(new_list)


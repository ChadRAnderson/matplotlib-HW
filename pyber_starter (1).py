#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# File to Load (Remember to change these)
city_data_to_load = "data/city_data.csv"
ride_data_to_load = "data/ride_data.csv"

# Read the City and Ride Data
city_df = pd.read_csv('data/city_data.csv')
city_df.head()
ride_df = pd.read_csv('data/ride_data.csv')
ride_df.head()

# Combine the data into a single dataset
ride_df = ride_df.dropna(axis=1)
city_rides = city_df.merge(ride_df, on='city')
city_rides.to_csv("output.csv", index=False)

# # Display the data table for preview
city_rides.head()


# In[3]:


city_rides = city_rides.drop_duplicates('ride_id')
city_rides.head()


# ## Bubble Plot of Ride Sharing Data

# In[4]:


# Obtain the x and y coordinates for each of the three city types

#city types
city_type = city_rides.set_index('city')['type']
city_type.value_counts()


# In[5]:


#average cost per ride
average_cost = city_rides.groupby("city")["fare"].mean()
average_cost.head()


# In[6]:


# Incorporate the other graph properties
#rides per city
rides_per_city = city_rides.groupby("city")["ride_id"].count()
rides_per_city.head()

#not sure why these are only giving '1' as the rides per city


# In[7]:



#drivers per city
drivers_per_city = city_rides.groupby("city")["driver_count"].count()
drivers_per_city.head()
#not sure why these are only giving '1' as the drivers per city


# In[8]:


urban = city_rides[(city_rides["type"] == "Urban")]
suburban = city_rides[(city_rides["type"] == "Suburban")]
rural = city_rides[(city_rides["type"] == "Rural")]

urban_avg = urban.groupby("city")["fare"].mean()
sub_avg = suburban.groupby("city")["fare"].mean()
rural_avg = rural.groupby("city")["fare"].mean()
urban_rides = urban.groupby("city")["ride_id"].count()
sub_rides = suburban.groupby("city")["ride_id"].count()
rural_rides = rural.groupby("city")["ride_id"].count()


urban_plot=plt.scatter(urban_rides, urban_avg, s=drivers_per_city, c='pink' , linewidths=1, edgecolor='black')
suburban_plot=plt.scatter(sub_rides, sub_avg, s=drivers_per_city, c="yellow" , linewidths=1, edgecolor='black')
rural_plot=plt.scatter(rural_rides, rural_avg, s=drivers_per_city, c="green" , linewidths=1, edgecolor='black')
plt.xlabel("Total Number of Rides Per City")
plt.ylabel("Average Fare ($)")
plt.title("Pyber Ride Sharing Data")
plt.legend(handles=[urban_plot,suburban_plot,rural_plot], labels=['Urban','Suburban','Rural'])

plt.show()


# Create a legend

# Incorporate a text label regarding circle size

# Save Figure


# In[9]:


# Calculate Type Percents

urban_cost=urban["fare"].sum()
sub_cost=suburban["fare"].sum()
rural_cost=rural["fare"].sum()

# Build Pie Chart

total_fare =[urban_cost, sub_cost, rural_cost]
explode = [.1,0,0]
labels =["Urban","Suburban","Rural"]
colors = ["red","yellow","green"]
plt.pie(total_fare,labels=labels,colors=colors,autopct='%1.2f%%',shadow=True,explode=explode)
plt.title("Percentage of Fares")
#show & save
plt.show()


# In[10]:


# Show plot
plt.show()


# In[ ]:





# 

# In[11]:


# Calculate Type Percents

# Build Pie Chart

# Save Figure


# In[12]:


# Show Figure
plt.show()


# ## Total Rides by City Type

# In[13]:


urban_rides=urban["ride_id"].count()
sub_rides=suburban["ride_id"].count()
rural_rides=rural["ride_id"].count()

total_rides =[urban_rides, sub_rides, rural_rides]
explode = [.1,0,0]
labels =["Urban","Suburban","Rural"]
colors = ["red","yellow","green"]
plt.pie(total_rides,labels=labels,colors=colors,autopct='%1.2f%%',startangle=55,explode=explode,shadow=True)
plt.title("Percentage of Rides")
plt.show()


# In[14]:


# Calculate Driver Percents
urban_drivers=urban["driver_count"].sum()
sub_drivers=suburban["driver_count"].sum()
rural_drivers=rural["driver_count"].sum()

# Build Pie Charts
total_drivers = [urban_drivers, sub_drivers, rural_drivers]
explode = [.1,0,0]
labels =["Urban","Suburban","Rural"]
colors = ["red","yellow","green"]

plt.pie(total_drivers,labels=labels,colors=colors,autopct='%1.2f%%',explode=explode,shadow=True)
plt.title("Percentage of Drivers by City Type")
plt.show()


#  

# In[ ]:





# In[25]:





# In[ ]:





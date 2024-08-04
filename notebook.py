#!/usr/bin/env python
# coding: utf-8

# # Proyek Analisis Data: [Bike Sharing]
# - **Nama:** [Ridho Setiawan]
# - **Email:** [ridhosetiawan24406@gmail.com]
# - **ID Dicoding:** [ridho_setiawan]

# ## Menentukan Pertanyaan Bisnis

# - Bagaimana Pengaruh Musim terhadap Penggunaan Bike Sharing?
# - Kapan Waktu Puncak Penggunaan Bike Sharing dalam Sehari Berdasarkan Rata-rata?

# ## Import Semua Packages/Library yang Digunakan

# In[1636]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn


# ## Data Wrangling

# ### Gathering Data

# In[1637]:


day_df = pd.read_csv("data/day.csv")
day_df.head()


# In[1638]:


hour_df = pd.read_csv("data/hour.csv")
hour_df.head()


# ### Assessing Data

# #### Menilai tabel `day_df`

# In[1639]:


day_df.info()


# In[1640]:


day_df.isna().sum()


# In[1641]:


print("Jumlah duplikasi: ", day_df.duplicated().sum())


# In[1642]:


day_df.describe()


# #### Menilai tabel `hour_df`

# In[1643]:


hour_df.info()


# In[1644]:


hour_df.isna().sum()


# In[1645]:


print("Jumlah duplikasi: ", hour_df.duplicated().sum())


# In[1646]:


hour_df.describe()


# ### Cleaning Data

# In[ ]:





# ## Exploratory Data Analysis (EDA)

# ### Explore `day_df`

# In[1647]:


day_df.sample(5)


# In[1648]:


day_df.describe(include="all")


# In[1649]:


print(f"Total penggunaan bike sharing oleh pengguna casual: {day_df['casual'].sum()}")


# In[1650]:


'''
jumlah penggunaan bike sharing berdasarkan pengguna casual 
1 = musim semi
2 = musim panas
3 = musim gugur
4 = musim dingin
'''

# Memfilter data untuk musim semi (springer, season == 1)
springer_df = day_df[day_df['season'] == 1]
# Mengelompokkan data berdasarkan 'casual'
casual_usage_springer = springer_df['casual'].sum()
# Menampilkan hasil
print(f"Jumlah penggunaan bike sharing oleh pengguna casual di musim semi: {casual_usage_springer}")

# Memfilter data untuk musim panas (summer, season == 2)
summer_df = day_df[day_df['season'] == 2]

casual_usage_summer = summer_df['casual'].sum()

print(f"Jumlah penggunaan bike sharing oleh pengguna casual di musim panas: {casual_usage_summer}")

# Memfilter data untuk musim gugur (fall, season == 3)
fall_df = day_df[day_df['season'] == 3]

casual_usage_fall = fall_df['casual'].sum()

print(f"Jumlah penggunaan bike sharing oleh pengguna casual di musim gugur: {casual_usage_fall}")

# Memfilter data untuk musim dingin (winter, season == 4)
winter_df = day_df[day_df['season'] == 4]
# Mengelompokkan data berdasarkan 'casual'

casual_usage_winter = winter_df['casual'].sum()
print(f"Jumlah penggunaan bike sharing oleh pengguna casual di musim dingin: {casual_usage_winter}")


# In[1651]:


print(f"Total penggunaan bike sharing oleh pengguna registered: {day_df['registered'].sum()}")


# In[1652]:


'''
jumlah penggunaan bike sharing berdasarkan pengguna registered 
1 = musim semi
2 = musim panas
3 = musim gugur
4 = musim dingin
'''

# Memfilter data untuk musim semi (springer, season == 1)
springer_df = day_df[day_df['season'] == 1]
# Mengelompokkan data berdasarkan 'registered'
registered_usage_springer = springer_df['registered'].sum()
# Menampilkan hasil
print(f"Jumlah penggunaan bike sharing oleh pengguna registered di musim semi: {registered_usage_springer}")

# Memfilter data untuk musim panas (summer, season == 2)
summer_df = day_df[day_df['season'] == 2]

registered_usage_summer = summer_df['registered'].sum()

print(f"Jumlah penggunaan bike sharing oleh pengguna registered di musim panas: {registered_usage_summer}")

# Memfilter data untuk musim gugur (fall, season == 3)
fall_df = day_df[day_df['season'] == 3]

registered_usage_fall = fall_df['registered'].sum()

print(f"Jumlah penggunaan bike sharing oleh pengguna registered di musim gugur: {registered_usage_fall}")

# Memfilter data untuk musim dingin (winter, season == 4)
winter_df = day_df[day_df['season'] == 4]
# Mengelompokkan data berdasarkan 'registered'

registered_usage_winter = winter_df['registered'].sum()
print(f"Jumlah penggunaan bike sharing oleh pengguna registered di musim dingin: {registered_usage_winter}")


# In[1653]:


print(f"Total penggunaan bike sharing oleh pengguna cnt: {day_df['cnt'].sum()}")


# In[1654]:


'''
jumlah penggunaan bike sharing berdasarkan pengguna cnt 
1 = musim semi
2 = musim panas
3 = musim gugur
4 = musim dingin
'''

# Memfilter data untuk musim semi (springer, season == 1)
springer_df = day_df[day_df['season'] == 1]
# Mengelompokkan data berdasarkan 'cnt'
cnt_usage_springer = springer_df['cnt'].sum()
# Menampilkan hasil
print(f"Jumlah penggunaan bike sharing oleh pengguna cnt di musim semi: {cnt_usage_springer}")

# Memfilter data untuk musim panas (summer, season == 2)
summer_df = day_df[day_df['season'] == 2]

cnt_usage_summer = summer_df['cnt'].sum()

print(f"Jumlah penggunaan bike sharing oleh pengguna cnt di musim panas: {cnt_usage_summer}")

# Memfilter data untuk musim gugur (fall, season == 3)
fall_df = day_df[day_df['season'] == 3]

cnt_usage_fall = fall_df['cnt'].sum()

print(f"Jumlah penggunaan bike sharing oleh pengguna cnt di musim gugur: {cnt_usage_fall}")

# Memfilter data untuk musim dingin (winter, season == 4)
winter_df = day_df[day_df['season'] == 4]
# Mengelompokkan data berdasarkan 'cnt'

cnt_usage_winter = winter_df['cnt'].sum()
print(f"Jumlah penggunaan bike sharing oleh pengguna cnt di musim dingin: {cnt_usage_winter}")


# ### Explore `hour_df`

# In[1655]:


hour_df.sample(5)


# In[1656]:


hour_df.describe(include="all")


# In[1657]:


# Mengelompokkan data berdasarkan jam dan menghitung rata-rata penggunaan
hourly_usage = hour_df.groupby('hr').agg({
    'casual': 'mean',
    'registered': 'mean',
    'cnt': 'mean'
}).reset_index()

# Mengurutkan DataFrame berdasarkan kolom 'cnt'
hourly_usage_sorted = hourly_usage.sort_values(by='cnt', ascending=False)

# Menampilkan hasil
print(hourly_usage_sorted)


# In[1658]:


main_data_df = pd.merge(
    left=day_df,
    right=hour_df,
    how="left",
    left_on="instant",
    right_on="instant"
)
main_data_df.head()


# ## Visualization & Explanatory Analysis

# ### Pertanyaan 1:

# In[1659]:


import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd

# Mengelompokkan data berdasarkan musim dan menghitung jumlah penggunaan
seasonal_usage = day_df.groupby('season').agg({
    'casual': 'sum',
    'registered': 'sum',
    'cnt': 'sum'
}).reset_index()

# Mapping season ke string
season_mapping = {
    1: 'Semi',
    2: 'Panas',
    3: 'Gugur',
    4: 'Dingin'
}
seasonal_usage['season'] = seasonal_usage['season'].map(season_mapping)

# Mengubah format DataFrame untuk visualisasi
seasonal_usage_melted = seasonal_usage.melt(id_vars=['season'], value_vars=['casual', 'registered', 'cnt'],
                                            var_name='Jenis Pengguna', value_name='Jumlah')

# Definisikan palette warna yang diinginkan
bar_colour = {
    'Semi': 'yellow',
    'Panas': 'red',
    'Gugur': 'orange',
    'Dingin': 'blue'
}

fig, ax = plt.subplots(figsize=(10, 6))
sn.barplot(data=seasonal_usage_melted, x='Jenis Pengguna', y='Jumlah', hue='season', palette=bar_colour, errorbar=None, ax=ax)
ax.set_title('Jumlah Penggunaan Bike Sharing oleh Pengguna Casual dan Registered di Setiap Musim')
ax.set_xlabel('Jenis Pengguna')
ax.set_ylabel('Jumlah (juta)')

# Mengatur batas sumbu y secara manual untuk memberikan ruang ekstra
max_y = seasonal_usage_melted['Jumlah'].max()
padding = 0.1 * max_y  # Tambahkan 10% dari nilai maksimum sebagai ruang ekstra
ax.set_ylim(0, max_y + padding)


# ### Pertanyaan 2:

# In[1660]:


# Mengelompokkan data berdasarkan jam dan menghitung rata-rata penggunaan
hourly_usage = hour_df.groupby('hr').agg({
    'casual': 'mean',
    'registered': 'mean',
    'cnt': 'mean'
}).reset_index()

# Mengurutkan DataFrame berdasarkan kolom 'cnt'
hourly_usage_sorted = hourly_usage.sort_values(by='cnt', ascending=False)

# Visualisasi menggunakan bar chart
plt.figure(figsize=(12, 6))
sn.barplot(data=hourly_usage_sorted, x='hr', y='cnt')
plt.title('Rata-rata Penggunaan Bike Sharing per Jam')
plt.xlabel('Jam')
plt.ylabel('Rata-rata Jumlah Penggunaan')
plt.show()


# ## Conclusion

# - Musim memiliki pengaruh yang besar terhadap penggunaan bike sharing, musim gugur adalah musim dengan jumlah penggunaan terbanyak dan musim semi dengan penggunaan paling sedikit
# - Puncak penggunaan bike sharing tertinggi berada di pukul 17 dan penggunaan terendah berada di pukul 4

# In[1661]:


main_data_df.to_csv("main_data.csv", index=False)


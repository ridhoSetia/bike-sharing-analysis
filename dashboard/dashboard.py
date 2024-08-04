import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st

day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

st.title('Bike Sharing Dashboard')

st.subheader('Penggunaan Bike Sharing berdasarkan jenis pengguna di tiap musim')

# Memfilter data untuk musim semi (springer, season == 1)
springer_df = day_df[day_df['season'] == 1]
cnt_usage_springer = springer_df['cnt'].sum()

# Memfilter data untuk musim panas (summer, season == 2)
summer_df = day_df[day_df['season'] == 2]
cnt_usage_summer = summer_df['cnt'].sum()

# Memfilter data untuk musim gugur (fall, season == 3)
fall_df = day_df[day_df['season'] == 3]
cnt_usage_fall = fall_df['cnt'].sum()

# Memfilter data untuk musim dingin (winter, season == 4)
winter_df = day_df[day_df['season'] == 4]
cnt_usage_winter = winter_df['cnt'].sum()

# Membuat kolom untuk menampilkan hasil
col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Jumlah Penggunaan di Musim Semi",
        value=f"{cnt_usage_springer:,.0f}"
    )

with col2:
    st.metric(
        label="Jumlah Penggunaan di Musim Panas",
        value=f"{cnt_usage_summer:,.0f}"
    )

with col1:
    st.metric(
        label="Jumlah Penggunaan di Musim Gugur",
        value=f"{cnt_usage_fall:,.0f}"
    )

with col2:
    st.metric(
        label="Jumlah Penggunaan di Musim Dingin",
        value=f"{cnt_usage_winter:,.0f}"
    )

# Mengelompokkan data berdasarkan musim dan menghitung jumlah penggunaan
seasonal_usage = day_df.groupby('season').agg({
    'casual': 'sum',
    'registered': 'sum',
    'cnt': 'sum'
}).reset_index()

seasonal_usage.rename(columns={'cnt': 'casual dan registrasi'}, inplace=True)

# Mapping season ke string
season_mapping = {
    1: 'Semi',
    2: 'Panas',
    3: 'Gugur',
    4: 'Dingin'
}
seasonal_usage['season'] = seasonal_usage['season'].map(season_mapping)

# Mengubah format DataFrame untuk visualisasi
seasonal_usage_melted = seasonal_usage.melt(id_vars=['season'], value_vars=['casual', 'registered', 'casual dan registrasi'],
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

ax.legend(title='Musim')
st.pyplot(fig)
st.subheader('Rata-rata penggunaan Bike Sharing berdasarkan jam')

col1, col2 = st.columns(2)

# Mengelompokkan data berdasarkan jam dan menghitung rata-rata penggunaan
hourly_usage = hour_df.groupby('hr').agg({
    'casual': 'mean',
    'registered': 'mean',
    'cnt': 'mean'
}).reset_index()

# Mengurutkan DataFrame berdasarkan kolom 'cnt'
hourly_usage_sorted = hourly_usage.sort_values(by='cnt', ascending=False)

# Menampilkan hanya yang paling tinggi dan rendah
top_usage = hourly_usage_sorted.head(1)
bottom_usage = hourly_usage_sorted.tail(1)

# Membuat kolom untuk menampilkan hasil
col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Jam dengan rata-rata penggunaan tertinggi",
        value=f"Pukul {top_usage['hr'].values[0]}",
        delta=f"{top_usage['cnt'].values[0]:,.0f} penggunaan"
    )

with col2:
    st.metric(
        label="Jam dengan rata-rata penggunaan terendah",
        value=f"Pukul {bottom_usage['hr'].values[0]}",
        delta=f"{bottom_usage['cnt'].values[0]:,.0f} penggunaan",
    )
    
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
st.pyplot(plt)  # Use Streamlit to display the plot
plt.close()  # Close the plot to avoid display issues
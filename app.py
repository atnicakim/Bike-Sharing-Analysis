import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
day_df = pd.read_csv("cleaned_day.csv")
day_df["dteday"] = pd.to_datetime(day_df["dteday"])

# Streamlit Dashboard
st.title("Bike Sharing Analysis Dashboard")

# Sidebar untuk filter waktu
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", day_df["dteday"].min())
end_date = st.sidebar.date_input("End Date", day_df["dteday"].max())

filtered_df = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & (day_df["dteday"] <= pd.to_datetime(end_date))]

# Tren Peminjaman Sepeda
st.subheader("Tren Peminjaman Sepeda Sepanjang Tahun")
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x=filtered_df["dteday"], y=filtered_df["cnt"], ax=ax)
ax.set_xlabel("Tanggal")  # Mengubah label sumbu X
ax.set_ylabel("Jumlah Peminjaman")  # Mengubah label sumbu Y
st.pyplot(fig)

# Pengaruh Cuaca terhadap Peminjaman
st.subheader("Pengaruh Cuaca terhadap Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(12, 5))
sns.boxplot(x=filtered_df["weathersit"], y=filtered_df["cnt"], ax=ax)
ax.set_xlabel("Kondisi Cuaca")  # Mengubah label sumbu X
ax.set_ylabel("Jumlah Peminjaman")  # Mengubah label sumbu Y
st.pyplot(fig)


# Kesimpulan
st.subheader("Kesimpulan")
st.write("""
1. **Tren Peminjaman Sepeda**: Pola musiman terlihat jelas, di mana peminjaman sepeda cenderung meningkat pada bulan tertentu saat cuaca lebih nyaman. Pihak pengelola bisa meningkatkan jumlah sepeda saat musim sibuk untuk mengakomodasi permintaan tinggi.
2. **Pengaruh Cuaca**: Peminjaman sepeda menurun drastis pada kondisi cuaca buruk. Perusahaan dapat menawarkan diskon atau promosi pada hari-hari hujan untuk menjaga tingkat penggunaan tetap stabil.
""")

st.caption('Mikacinta Gustina Amalan Toyibah, 2025')

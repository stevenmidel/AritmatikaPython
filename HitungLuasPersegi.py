import streamlit as st
from streamlit_option_menu import option_menu

# Navigasi SideBar
with st.sidebar:
    selected = option_menu('Hitung Luas Bangun', ['Hitung Luas Persegi Panjang', 'Hitung Luas Segitiga'], default_index=0)

# Halaman Hitung Luas Persegi Panjang
if selected == 'Hitung Luas Persegi Panjang':
    st.title("Hitung Luas Persegi Panjang")
    panjang = st.number_input("Masukkan Nilai Panjang", 0)
    lebar = st.number_input("Masukkan Nilai Lebar", 0)
    hitung = st.button("Hitung Luas")
    # Fungsi Persegi Panjang
    if hitung:
        luas = panjang * lebar
        st.success(f"Luas Persegi Panjang Adalah = {luas}")

# Halaman Hitung Segitiga
elif selected == 'Hitung Luas Segitiga':
    st.title('Hitung Luas Segitiga')
    alas = st.number_input('Masukkan Nilai Alas', 0)
    tinggi = st.number_input('Masukkan Nilai Tinggi', 0)
    hitung1 = st.button('Hitung Luas')
    # Fungsi Luas Segitiga
    if hitung1:
        luas1 = 0.5 * alas * tinggi
        st.success(f"Luas Segitiga Adalah = {luas1}")

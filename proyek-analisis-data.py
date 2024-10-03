import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
import io

st.title("PROYEK ANALISIS DATA")
st.header("DATA WRANGLING")
st.caption(
    """
    Background

Dicoding Collection atau sering disingkat DiCo merupakan sebuah perusahaan yang bergerak di bidang fashion. Ia memproduksi berbagai item fashion dan menjualnya melalui platform online.

Sebagai perusahaan kekinian, DiCo menyadari betapa pentingnya data bagi perkembangan sebuah bisnis. Oleh karena itu, ia menyimpan semua history penjualan beserta informasi terkait produk dan customers dalam sebuah database. Database ini terdiri dari empat buah tabel, antara lain customers, orders, products, dan sales.

Tabel customers: tabel ini menyimpan berbagai informasi terkait customer, seperti customer_id, customer_name, gender, age, home_address, zip_code, city, state, dan country.

Tabel orders: tabel ini menyimpan berbagai informasi terkait sebuah order yang terdiri dari order_id, customer_id, payment, order_date, dan delivery_date.

Tabel products: tabel ini berisi berbagai informasi terkait sebuah produk, seperti product_id, product_type, product_name, size, colour, price, quantity, dan description.

Tabel sales: tabel ini mengandung informasi detail terkait penjualan, seperti sales_id, order_id, product_id, price_per_unit, quantity, dan total_price.

Tujuan First of all, kita akan mulai proyek analisis data ini dengan menjalankan proses data wrangling terlebih dahulu. Proses ini memiliki tujuan antara lain

mengumpulkan seluruh data yang dibutuhkan; menilai kualitas dari data yang telah dikumpulkan; dan membersihkan data tersebut sehingga siap untuk dianalisis.

Alur Latihan Berikut merupakan tahapan dalam latihan ini.

Tahap persiapan.

Tahap gathering data.

Tahap assessing data.

Tahap cleaning data.
    """
)
st.write(
    """
    import semua library yang dibutuhkan dalam analisis data
    """
)
code = """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""
st.code(code, language='python')
st.caption(
    """Ada tiga tahapan Data Wrangling

1. Gathering Data
2. Assesing Data
3. Cleaning Data
    """
)

st.subheader("Gathering Data")
st.caption("customers_df")
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")
st.dataframe(data=customers_df)

buffer = io.StringIO()
customers_df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")
st.dataframe(data=orders_df)

buffer = io.StringIO()
orders_df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

products_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")
st.dataframe(data=products_df)

buffer = io.StringIO()
products_df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")
st.dataframe(data=sales_df)

buffer = io.StringIO()
sales_df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

# st.subheader("Assesing Data")
# st.caption("customers_df")
# customers_df
# buffer = io.StringIO()
# customers_df.info(buf=buffer)
# s = buffer.getvalue(buf=buffer)
# st.text(s)

# # st.write(customers_df.isna().sum())

# st.caption("products_df")
# buffer = io.StringIO()
# products_df.info(buf=buffer)
# s = buffer.getvalue()
# st.text(s)

# st.caption("orders_df")
# buffer = io.StringIO()
# orders_df.info(buf=buffer)
# s = buffer.getvalue()
# st.text(s)

# st.caption("sales_df")
# buffer = io.StringIO()
# sales_df.info(buf=buffer)
# s = buffer.getvalue()
# st.text(s)
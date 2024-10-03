import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
st.write(pd.DataFrame({

    
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

st.metric(label="Temperature", value="28 °C", delta="1.2 °C")


st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})


st.title('Belajar Analisis Data')
st.header('Pengembangan Dashboard')
st.subheader('Pengembangan Dashboard')

code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.text('Halo, calon praktisi data masa depan.')

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)


name = st.text_input(label="Nama Lengkap", value="")
st.write("Nama: ", name)

text = st.text_area('Feedback')
st.write('Feedback: ', text)

number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)


uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    
# picture = st.camera_input('Take a picture')
# if picture:
#     st.image(picture)
    
if st.button('Say hello'):
    st.write('Hello there')
    
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)


st.title('Belajar Analisis Data')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
 
with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.caption('Copyright (c) 2023')
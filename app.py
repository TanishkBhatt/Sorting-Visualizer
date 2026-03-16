import streamlit as st
from utils import *

st.set_page_config(page_title='Sorting Visualizer - TanishkBhatt')
st.title("SORTING VISUALIZER")
algo = st.selectbox("SELECT THE ALGORITHM TO SIMULATE",
              ["BUBBLE SORT", "SELECTION SORT", "INSERTION SORT"])

col1, col2, col3 = st.columns(3)
with col2:
    do_sort = st.button(f"SIMULATE {algo}")
st.divider()

arr = [42, 85, 17, 93, 58, 21, 74, 36, 60, 10, 12, 56, 79, 25, 50]
fig = st.bar_chart(arr)

def update_plot(arr: list[int]):
    fig.bar_chart(arr)

if do_sort:
    match algo:
        case "BUBBLE SORT":
            bubble_sort(arr, update_plot)
        case "SELECTION SORT":
            selection_sort(arr, update_plot)
        case "INSERTION SORT":
            insertion_sort(arr, update_plot)

st.divider()
st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")
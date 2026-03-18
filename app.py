import streamlit as st
from utils import *

st.set_page_config(page_title='Sorting Visualizer - TanishkBhatt')

st.title("SORTING VISUALIZER")
algo = st.selectbox(
        "SELECT THE ALGORITHM TO VISUALIZE", 
        ["BUBBLE SORT", "SELECTION SORT", "INSERTION SORT"]
    )
st.divider()

arr = [42, 85, 93, 58, 21, 74, 36, 60, 12, 56, 79, 10]
def update_plot(arr: list[int]):
    fig.bar_chart(arr)

match algo:
    case "BUBBLE SORT":
        code = bubble_sort_code()
    case "SELECTION SORT":
        code = selection_sort_code()
    case "INSERTION SORT":
        code = insertion_sort_code()
    case _:
        code = ""

st.subheader(f"{algo} CODE")
st.code(code)
st.divider()
st.subheader("SORTING SIMULATOR")
do_sort = st.button(f"SIMULATE {algo}")
st.markdown("")
fig = st.bar_chart(arr)

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
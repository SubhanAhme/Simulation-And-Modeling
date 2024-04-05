import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected=option_menu(
        menu_title="Main Menu",
        options=["MMC","MGC","GMC","GGC"],
        default_index=0,
        menu_icon="cast",
        orientation="horizontal",
    )
    if selected=="MMC":
        st.title(f"You Have Selected {selected}")
    if selected=="MGC":
        st.title(f"You Have Selected {selected}")
    if selected=="GMC":
        st.title(f"You Have Selected {selected}")
    if selected=="GGC":
        st.title(f"You Have Selected {selected}")
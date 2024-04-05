import streamlit as st

from streamlit_option_menu import option_menu


import main, MMC,GGC,GMC,MGC,MMCp
st.set_page_config(
        page_title="Simulation And Modeling")



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Options',
                options=['MMCp','MMC','MGC','GMC','GGC'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'white'},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color":"#006DA4" },
        "nav-link-selected": {"background-color": "#004D74"},}
                
                )

        
        if app == "Home":
            main.app()
        if app == "MMC":
            MMC.app()    
        if app == "MGC":
            MGC.app()        
        if app == 'GMC':
            GMC.app()
        if app == 'GGC':
            GGC.app()
        if app == 'MMCp':
            MMCp.app()    
             
          
             
    run()            
         

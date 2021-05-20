
import streamlit as st 
st.set_page_config(
    page_title = 'Power BI Dashboard',
    page_icon = 'Power-BI-Logo.png',
    layout = 'wide'
)

html_temp = """
    <div style ="background-color:#9071CE;padding:13px">
    <h1 style ="color:white;text-align:center;">Power BI Dashboard</h1>
    </div>
    """ 
st.markdown(html_temp, unsafe_allow_html = True)
st.title(" ")
 
st.markdown('<iframe width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=19fb8c01-1443-48d0-85fb-ac80a558920e&autoAuth=true&ctid=c7ba5b1a-41b6-43e9-a120-6ff654ada137&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLXdlc3QtZXVyb3BlLXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0LyJ9" frameborder="0" allowFullScreen="true"></iframe>',unsafe_allow_html=True)




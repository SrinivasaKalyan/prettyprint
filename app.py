import json
import clipboard
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

lottie_animation = load_lottie_file("ani.json")
lottie_animation1 = load_lottie_file("dolphin.json")


def create_copy_button(text_to_copy):
    button_id = "copyButton" + text_to_copy
    
    button_html = f"""<button id="{button_id}">Copy</button>
    <script>
    document.getElementById("{button_id}").onclick = function() {{
        navigator.clipboard.writeText("{text_to_copy}").then(function() {{
            console.log('Async: Copying to clipboard was successful!');
        }}, function(err) {{
            console.error('Async: Could not copy text: ', err);
        }});
    }}
    </script>"""
    
    st.markdown(button_html, unsafe_allow_html=True)


def main():
    st.set_page_config(
    page_title="Pretty Print",
    page_icon="logo.png", 
    layout="wide",     
    initial_sidebar_state="auto"
)
    # st.title("Geo Spatial Insights")
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Grey+Qo&family=Zeyada&display=swap" rel="stylesheet">
    <style>
        .grey-qo-regular {
            font-family: 'Grey Qo', cursive;
            font-weight: 400;
            font-style: normal;
        }
        .zeyada-regular {
            font-family: 'Zeyada', cursive;
        }
    </style>
""", unsafe_allow_html=True)

        # Use the Grey Qo font in your HTML
    st.markdown("<p class='grey-qo-regular' style='text-align: center;color:white;font-size:90px;'>json Formatter</p>", unsafe_allow_html=True)     
    st.markdown("<p </p>", unsafe_allow_html=True)     
 
    st.markdown(
        """
        <style>
        /* Reduce width of dropdown */
        .css-1e5mbc4 {
            width: 120px !important;
        }
        /* Increase height of text areas */
        .css-1cpxqw2, .css-1d391kg {
            height: 500px !important;
        }
        /* Center the Lottie animation */
        .centered-lottie {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        </style>
        """, unsafe_allow_html=True
    )

    if "formatted_json" not in st.session_state:
        st.session_state.formatted_json = ""

    col1, col2, col3 = st.columns([3, 0.5, 3])  

    with col1:
        st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Grey+Qo&family=Zeyada&display=swap" rel="stylesheet">
    <style>
        .grey-qo-regular {
            font-family: 'Grey Qo', cursive;
            font-weight: 400;
            font-style: normal;
            font-size:70px;
            color:darkorange;
        }
        .zeyada-regular {
            font-family: 'Zeyada', cursive;
        }
    </style>
""", unsafe_allow_html=True)

        # Use the Grey Qo font in your HTML
        st.markdown("<h1 class='grey-qo-regular' style='text-align: center;'>Input json</h1>", unsafe_allow_html=True)     
        json_data = st.text_area("Paste your JSON here", height=500, key="input_json")
        if st.button("About creator 🧐"):
            with st.expander("Kalyan Kanchumarthi"):
                        st.image("mypic.jpg", use_column_width=True)
                        st.write("""
                        Hello! I'm Kalyan Kanchumarthi, \n
                        a passionate developer exploring the world of AI and programming.

                        - I love building applications that make life easier.
                        - I'm good at Python and data analysis.
                        - Don't misunderstand me as a nerd; I'm socially adept too! 😄
                        - Thank you for checking out my app!

                        Do check out my [LinkedIn](https://www.linkedin.com/in/kalyan-kanchumarthi-a6320a235/) and [GitHub](https://github.com/SrinivasaKalyan).
                        """)

    with col2:
        st.text("")  
        st.text("")  
        st.text("")  
        st.text("")  
        st.text("")  
        st.text("")  
        st.text("")  
        st.text("")  
        st.text("")  
        st.text("")  
        st.text("")  
        
        indent_options = st.selectbox("INDENTATION", options=[2, 4, 6, 8], index=1, key="indent_select")
        pretty_print = st.button("Pretty Print")
        
        if pretty_print and json_data:
            try:
                json_object = json.loads(json_data)
                st.session_state.formatted_json = json.dumps(json_object, indent=indent_options)
                
                
                

            except json.JSONDecodeError:
                st.error("Invalid JSON")    
        
        if st.session_state.formatted_json:
            st.download_button(
                label="Download JSON",
                data=st.session_state.formatted_json,
                file_name="formatted_json.txt",
                mime="text/plain"
            )
        
        # Centering the Lottie animation
        with st.container():
            st.markdown('<div class="centered-lottie">', unsafe_allow_html=True)
            st_lottie(lottie_animation, height=100, key="lottie_animation")
            st_lottie(lottie_animation1, height=100, key="lottie_animation1")
            st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Grey+Qo&family=Zeyada&display=swap" rel="stylesheet">
    <style>
        .grey-qo-regular {
            font-family: 'Grey Qo', cursive;
            font-weight: 400;
            font-style: normal;
            font-size:70px;
            color:darkorange;
        }
        .zeyada-regular {
            font-family: 'Zeyada', cursive;
        }
    </style>
""", unsafe_allow_html=True)

        # Use the Grey Qo font in your HTML
        st.markdown("<h1 class='grey-qo-regular' style='text-align: center;'>Pretty json</h1>", unsafe_allow_html=True)   
        formatted_json = st.text_area("Formatted JSON", value=st.session_state.formatted_json, height=500, key="output_json")
        st.markdown(f'<textarea id="formatted_json" style="display:none;">{st.session_state.formatted_json}</textarea>', unsafe_allow_html=True)
       
if __name__ == "__main__":
    main()

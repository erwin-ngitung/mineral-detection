from streamlit import session_state as state
import streamlit as st
from PIL import Image
from pathlib import Path
import logging

st.set_page_config(
    page_title="Home | C-MIND 1.0 App",
    page_icon="🏠",
)

PATH = '.'
# PATH = Path(Path(__file__).resolve()).parent
# logger = logging.getLogger(__name__)

state['login'] = False
state['PATH'] = PATH

image = Image.open(f'{PATH}/data/images/logo_md.jpeg')
st1, st2, st3 = st.columns(3)

with st2:
    st.image(image)

st.markdown('<h3 style=\'text-align:center;\'>Welcome to C-MIND 1.0! 👋</h3>', unsafe_allow_html=True)

st.markdown(
    """
    ### Want to learn more and purchase it?
    - Check out [C-MIND 1.0 Website] (https://github.com/erwin-ngitung/c-mind-1.0)
    - Jump into our [Documentation] (https://github.com/erwin-ngitung/c-mind-1.0)
    - Ask a question in our software (salsabilsudharta0724@gmail.com)
    """
)

import streamlit as st

st.markdown("# Main page π")
st.sidebar.markdown("# Main page π")

import seaborn as sns

mpg = sns.load_dataset("mpg")

st.write("""
### μλμ°¨ μ°λΉ
""")

st.dataframe(mpg)

st.line_chart(mpg["mpg"])
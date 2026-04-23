import streamlit as st
st.markdown('<style>[data-testid="stAppViewContainer"]{background-color:black;} *{color:#00FF00 !important;}</style>', unsafe_allow_html=True)
data = st.text_area("🎯 رادار القناص - أدخل البيانات:")
if st.button("🚀 تحليل"): st.success("✅ جاري الفحص... الاحتمال: هدف قريب!")

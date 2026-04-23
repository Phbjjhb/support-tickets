import streamlit as st

st.set_page_config(page_title="رادار القناص", layout="wide")

# كود خلفية الهكر
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXNoZ3VvNHVvNHVvNHVvNHVvNHVvNHVvNHVvNHVvNHVvNHVvJmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/13HBDT4QSTpveU/giphy.gif");
        background-size: cover;
        }
        * { color: #00FF00 !important; font-family: 'Courier New'; }
        textarea { background: rgba(0,20,0,0.8) !important; border: 1px solid #00FF00 !important; }
        </style>
        """, unsafe_allow_html=True)

        st.title("🎯 رادار القناص للهكر")
        data = st.text_area("ضع بيانات الماتش هنا:")
        if st.button("🚀 ابدأ التحليل"):
            st.success("✅ جاري اختراق البيانات... الاحتمال: هدف قريب!")
            
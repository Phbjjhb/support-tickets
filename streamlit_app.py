import streamlit as st
import google.generativeai as genai

# إعدادات الواجهة الاحترافية
st.set_page_config(page_title="نظام القناص 99%", layout="centered")

# كود الخلفية المتحركة (الهكر)
page_bg_hacker = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXZueXZueXZueXZueXZueXZueXZueXZueXZueXZueXZueZCZpZD1nZmlmJmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/YQitE4YNQWayDnD6dW/giphy.gif");
        background-size: cover;
            background-position: center;
                background-attachment: fixed;
                }
                .stTextArea textarea { background-color: rgba(0, 0, 0, 0.8) !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; font-size: 16px !important; }
                .stButton button { width: 100%; background-color: #28a745 !important; color: white !important; font-weight: bold; height: 60px; font-size: 20px; border-radius: 10px; }
                h1 { color: #00ff00 !important; text-shadow: 2px 2px 15px #000; text-align: center; direction: rtl; }
                label { color: #00ff00 !important; font-weight: bold; direction: rtl; text-align: right; display: block; }
                </style>
                '''
                st.markdown(page_bg_hacker, unsafe_allow_html=True)

                # تفعيل الذكاء الاصطناعي بمفتاحك
                genai.configure(api_key="AIzaSyAcDOI7FJpbpoxEEUvTwuFLr5ee4_5zxMk")
                model = genai.GenerativeModel('gemini-1.5-pro')

                st.markdown("<h1>💻 رادار القناص (نسخة الشبح)</h1>", unsafe_allow_html=True)

                # المربع بالعربي
                matches_data = st.text_area("📥 ارمي بيانات الماتشات هنا يا وحش:")

                if st.button("🎯 قنص المضمون (99%)"):
                    if matches_data:
                            with st.spinner("⚡ جاري اختراق قاعدة البيانات واستخراج الزتونة..."):
                                        prompt = f"حلل الماتشات دي وطلع لي الخلاصة المضمونة 99% باللهجة المصرية كأنك هكر محترف: {matches_data}"
                                                    try:
                                                                    response = model.generate_content(prompt)
                                                                                    st.success("✅ تم الاختراق بنجاح:")
                                                                                                    st.markdown(f"<div style='background:rgba(0,0,0,0.7); padding:15px; border-radius:10px; color:#00ff00; direction:rtl;'>{response.text}</div>", unsafe_allow_html=True)
                                                                                                                except:
                                                                                                                                st.error("❌ السيرفر مضغوط، جرب تاني يا بطل.")
                                                                                                                                    else:
                                                                                                                                            st.warning("⚠️ دخل الماتشات الأول!")
import streamlit as st

st.set_page_config(page_title="Low-code AI Chatbot", layout="wide")

st.title("🤖 Low-code AI Chatbot")
st.write("Chào mừng bạn! Hãy đặt câu hỏi về AI.")

# Tạo session để lưu lịch sử hội thoại
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lịch sử hội thoại
for msg in st.session_state.messages:
    role, text = msg
    if role == "user":
        st.markdown(f"**Bạn:** {text}")
    else:
        st.markdown(f"**Bot:** {text}")

# Nhập tin nhắn
user_input = st.text_input("Nhập tin nhắn của bạn:", "")

if st.button("Gửi"):
    if user_input:
        st.session_state.messages.append(("user", user_input))
        bot_reply = "💡 (Placeholder) Chatbot đang xử lý..."  # Sẽ thay bằng backend sau này
        st.session_state.messages.append(("bot", bot_reply))
        st.rerun()
    else:
        st.warning("Vui lòng nhập tin nhắn trước khi gửi.")

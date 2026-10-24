"""
FastAPI ye bağlanan basit bir chatbot arayüzü geliştirme
"""

import streamlit as st
import requests

# canlı backend adresi
BACKEND_URL= "https://smart-assistant-backend-ziz7.onrender.com"

# sayfa ayarları
st.set_page_config(
    page_title = "Akıllı Asistan",
    page_icon = "🤖",
    layout= "centered"
)

st.title("🤖 Akıllı Asistan")
st.write("Mesajınızı yazın, asistan size cevap versin.")

# sohbet geçmişi

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# backend den eski mesajları çekme
def load_message_from_backend():
    
    try:
        
        response = requests.get(f"{BACKEND_URL}/messages")
        
        if response.status_code==200:
            data = response.json()
            return data.get("messages", [])
        return []
    except:
        return []

# mesajı backende gönderme
def send_message_to_backend(user_message):

    try:
        response = requests.post(f"{BACKEND_URL}/chat", json={"user_message": user_message})
        if response.status_code == 200:
            return response.json()
        return {"assistant_response": "Bir hata oluştu"}
    except Exception as e:
        print(f"Bağlantı Hatası Detayı: {e}")
        return {"assistant_response": "Backend servisine bağlanılamadı"}

# sayfa ilk açıldığında geçmiş mesajları yükle
if not st.session_state.chat_history:
    old_messages = load_message_from_backend()

    for item in old_messages:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": item["user_message"]
            }
        )

        st.session_state.chat_history.append(
                    {
                        "role": "assistant",
                        "content": item["assistant_response"]
                    }
                )
# eski mesajları göster
for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# yeni mesaj girişi
user_input = st.chat_input("mesajınızı yazın: ")

if user_input:
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    result = send_message_to_backend(user_input)

    # with st.spinner("Düşünüyor..."):
    #     result = send_message_to_backend(user_input)
    # st.write("Backend'den gelen veri:", result) 

    assistant_response = result.get("assistant_response", "Bir cevap alınamadı")

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )

    with st.chat_message("assistant"):
        st.write(assistant_response)





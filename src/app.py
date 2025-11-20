import streamlit as st
import requests

st.title("📰 News Intelligence Chatbot (HF API)")

# 1) HF Secrets 로드
HF_TOKEN = st.secrets["HF_TOKEN"]

# 2) 네 모델 ID
MODEL_ID = "HaGPT/news-intelligence-chatbot"

# 3) HF Inference API URL + Header
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# 4) 요청 함수
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# UI
user_input = st.text_area("뉴스 요약 / 분석 요청을 입력하세요:")

if st.button("생성"):
    with st.spinner("모델이 응답 중..."):
        output = query({"inputs": user_input})

        # 응답 처리
        try:
            st.write("### 답변:")
            # 모델별 응답 형식 다를 수 있음 → 안전하게 처리
            if isinstance(output, list):
                st.write(output[0].get("generated_text", "No generated_text field"))
            else:
                st.json(output)
        except:
            st.error("모델 응답 에러")
            st.json(output)

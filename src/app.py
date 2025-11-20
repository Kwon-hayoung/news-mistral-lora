import streamlit as st
import requests

st.title("📰 News Intelligence Chatbot (정치 경제 뉴스 지식 탑재 챗봇)")

HF_TOKEN = st.secrets["HF_TOKEN"]
MODEL_ID = "HaGPT/news-intelligence-chatbot"

# 새로운 인퍼런스 URL
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        # 정상 JSON 응답이면 그대로 반환
        return response.json()
    except Exception:
        # JSON 파싱 실패 → 원본 텍스트와 상태코드를 반환
        return {
            "error": "JSON decode failed",
            "status_code": response.status_code,
            "raw_response": response.text
        }
        
prompt = st.text_area("질문을 입력하세요:")

if st.button("생성"):
    with st.spinner("모델이 응답 중..."):
        output = query({"inputs": prompt})

        st.write("### 응답:")
        st.json(output)   # raw_response가 JSON 형태로 안전하게 렌더링됨

# 🦥 Unsloth 기반 LLM 파인튜닝 프로젝트

## 🤖 Gradio 챗봇
<img width="1471" height="924" alt="image" src="https://github.com/user-attachments/assets/0b9cd341-03e1-4a54-ad1a-aca76976f637" />

## 왜 파인튜닝을 하는가?
- 본 프로젝트는 정치·경제·거시 분석처럼 일반 LLM이 다루기 어려운 전문 분야 답변의 정확성을 높이기 위해 수행
- RAG 의 한계 -> 흩어져 있는 문서 구조(비정형)
- 파인튜닝 -> 도메인-specific reasoning + 패턴 내재화
- 전문 분석가 수준의 구조적 요약·질의응답을 수행하는 서비스 구축 목표

## 대화
LangChain의 ConversationBufferMemory로 대화를 저장하여,
모델이 과거 답변을 참조해 일관된 요약과 인사이트 추출을 수행하도록 구성 (코드 수정 예정)

## 📌 주요 노트북

| 모델 | 타입 | Colab 링크 |
|------|------|------------|
| **Llama 3.1 (8B) – Alpaca** | Instruction Fine-Tuning | <a href="https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_(8B)-Alpaca.ipynb#scrollTo=iHjt_SMYsd3P" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a> |


## 📚 Fine-tuned Model

| 모델 | 학습 데이터셋 | 모델 링크 |
|------|----------------|------------|
| **Mistral LoRA (16bit merged)** | <a href="https://huggingface.co/datasets/HaGPT/Political-Economy-Expert-QA" target="_blank"><img src="https://img.shields.io/badge/HuggingFace-Dataset-orange?logo=huggingface" /></a> | <a href="https://huggingface.co/HaGPT/news-intelligence-chatbot" target="_blank"><img src="https://img.shields.io/badge/HuggingFace-Model-blue?logo=huggingface" /></a> |


|챗봇 시현 가능|
|--------------|
| <a href="https://colab.research.google.com/drive/1uwI85Cu3_tn9OfJbmpdzluHqGLOmSsnW#scrollTo=_mN6ocdPCWBi" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a> |

## GPT 답변과 비교
이미지 업로드 예정

# 🦥 Unsloth 기반 LLM 파인튜닝 프로젝트

## 🤖 Gradio 기반 챗봇
<img width="1510" height="930" alt="image" src="https://github.com/user-attachments/assets/3abf9b2b-b435-47aa-a026-2a03cb4f1911" />

## 왜 파인튜닝을 하는가?
- 본 프로젝트는 정치·경제·거시 분석처럼 일반 LLM이 다루기 어려운 전문 분야 답변의 정확성을 높이기 위해 수행
- 정책 분석, 환율 구조 분석, 지정학·통화정책 해석 등 특정 도메인에 최적화
- 전문 분석가 수준의 구조적 요약·질의응답을 수행하는 서비스 구축 목표

## 대화
LangChain의 ConversationBufferMemory로 모든 대화를 저장하여,
모델이 과거 답변을 참조해 일관된 요약과 인사이트 추출을 수행하도록 구성 (코드 수정 예정)

## 📌 주요 노트북

| 모델 | 타입 | Colab 링크 |
|------|------|------------|
| **Llama 3.1 (8B) – Alpaca** | Instruction Fine-Tuning | <a href="https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_(8B)-Alpaca.ipynb#scrollTo=iHjt_SMYsd3P" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a> |


## 📚 Fine-tuned Model

| 모델 | 학습 데이터셋 | 모델 링크 |
|------|----------------|------------|
| **Mistral LoRA (16bit merged)** | <a href="https://huggingface.co/datasets/HaGPT/Political-Economy-Expert-QA" target="_blank"><img src="https://img.shields.io/badge/HuggingFace-Dataset-orange?logo=huggingface" /></a> | <a href="https://huggingface.co/HaGPT/mistral-lora-16bit" target="_blank"><img src="https://img.shields.io/badge/HuggingFace-Model-blue?logo=huggingface" /></a> |


|ㅓColab Notebook|
|--------------|
| <a href="https://colab.research.google.com/drive/1uwI85Cu3_tn9OfJbmpdzluHqGLOmSsnW#scrollTo=_mN6ocdPCWBi" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a> |

## GPT 답변과 비교
이미지 업로드 예정

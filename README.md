# 🦥 Unsloth 기반 LLM 파인튜닝 프로젝트

## Multi Agent 
<img width="4901" height="1530" alt="image" src="https://github.com/user-attachments/assets/b10cbfa6-a2d6-4980-b596-f9e307d98342" />

## 🤖 Gradio 챗봇
<img width="1471" height="924" alt="image" src="https://github.com/user-attachments/assets/0b9cd341-03e1-4a54-ad1a-aca76976f637" />

## 대화
LangChain의 ConversationBufferMemory로 대화를 저장하여,
모델이 과거 답변을 참조해 일관된 요약과 인사이트 추출을 수행하도록 구성

## 📌 주요 노트북

| 모델 | 타입 | Colab 링크 |
|------|------|------------|
| **Llama 3.1 (8B) – Alpaca** | Instruction Fine-Tuning | <a href="https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_(8B)-Alpaca.ipynb#scrollTo=iHjt_SMYsd3P" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a> |

학습 데이터 변경 : <think>, <tool_call>, <tool_output> 등 특수 태그를 포함하여 모델에게 도구 사용 계획 및 구조적 추론 패턴을 학습

## 📚 Fine-tuned Model

| 모델 | 학습 데이터셋 | 모델 링크 (수정) |
|------|----------------|------------|
| **Mistral LoRA (16bit merged)** | <a href="https://huggingface.co/datasets/HaGPT/Political-Economy-Expert-QA" target="_blank"><img src="https://img.shields.io/badge/HuggingFace-Dataset-orange?logo=huggingface" /></a> | <a href="https://huggingface.co/HaGPT/news-intelligence-chatbot" target="_blank"><img src="https://img.shields.io/badge/HuggingFace-Model-blue?logo=huggingface" /></a> |


|챗봇 시현 코드 (수정) |
|--------------|
| <a href="https://colab.research.google.com/drive/1uwI85Cu3_tn9OfJbmpdzluHqGLOmSsnW#scrollTo=_mN6ocdPCWBi" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a> |

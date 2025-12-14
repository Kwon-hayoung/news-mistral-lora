# 🦥 Unsloth 기반 LLM 파인튜닝 프로젝트

## Multi Agent 
<img width="4901" height="1530" alt="image" src="https://github.com/user-attachments/assets/b10cbfa6-a2d6-4980-b596-f9e307d98342" />

## 🤖 Gradio 챗봇 (기존의 파인튜닝 Q/A 학습)
<img width="1471" height="924" alt="image" src="https://github.com/user-attachments/assets/0b9cd341-03e1-4a54-ad1a-aca76976f637" />

## 🤖 Gradio 챗봇 (도구 사용을 판단하는 에이전트)


## 뉴스는 왜 RAG 에 적합하지 않은가? 내 모델이 질문을 얼만큼 이해할 수 있을까?
**<think>, <tool_call>, <tool_output> 등 특수 태그를 포함하여 모델에게 도구 사용 계획 및 구조적 추론 패턴을 학습**

## 📌 주요 노트북

| 모델 | 타입 | Colab 링크 |
|------|------|------------|
| **Llama 3.1 (8B) – Alpaca** | ToolScale 데이터셋 | <a href="https://colab.research.google.com/drive/1y4asnzW17B9zfuXnwyKyZNzjCS0katZg#scrollTo=91622afd" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a> |

**<think>, <tool_call>, <tool_output> 등 특수 태그를 포함하여 모델에게 도구 사용 계획 및 구조적 추론 패턴을 학습**

## 📚 Fine-tuned Model

| 모델 | 학습 데이터셋 | 모델 링크 (수정) |
|------|----------------|------------|
| **Mistral LoRA (16bit merged)** | <a href="https://huggingface.co/datasets/HaGPT/News-Orchestrator" target="_blank"><img src="https://img.shields.io/badge/HuggingFace-Dataset-orange?logo=huggingface" /></a> | <a href="https://huggingface.co/HaGPT/news-intelligence-chatbot" target="_blank"><img src="https://img.shields.io/badge/HuggingFace-Model-blue?logo=huggingface" /></a> |


|챗봇 시현 코드 (수정) |
|--------------|
| <a href="https://colab.research.google.com/drive/1uwI85Cu3_tn9OfJbmpdzluHqGLOmSsnW#scrollTo=_mN6ocdPCWBi" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a> |

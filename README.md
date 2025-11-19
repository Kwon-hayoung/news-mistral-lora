# 🦥 Unsloth 기반 LLM 파인튜닝 프로젝트


## 왜 파인튜닝을 하는가?
- 왜 학습 시켜야 하는지
- 어떤 도메인에 특화되어 있고 어떤 서비스에 특화된 모델인지

## 📌 주요 노트북

| 모델 | 타입 | Colab 링크 |
|------|------|------------|
| **Llama 3.1 (8B) – Alpaca** | Instruction Fine-Tuning | <a href="https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_(8B)-Alpaca.ipynb#scrollTo=iHjt_SMYsd3P" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a> |


## 📚 Fine-tuned Model

| 모델 | 학습 데이터셋 | 모델 링크 |
|------|----------------|------------|
| **Mistral LoRA (16bit merged)** | <a href="https://huggingface.co/datasets/HaGPT/Political-Economy-Expert-QA" target="_blank"><img src="https://img.shields.io/badge/HuggingFace-Dataset-orange?logo=huggingface" /></a> | <a href="https://huggingface.co/HaGPT/mistral-lora-16bit" target="_blank"><img src="https://img.shields.io/badge/HuggingFace-Model-blue?logo=huggingface" /></a> |


## 🤖 Gradio 기반 챗봇
<img width="1688" height="495" alt="image" src="https://github.com/user-attachments/assets/1e66785f-31f8-469d-9e54-1b8d72d3e3a3" />
| **Model**                                      | **Task Description**                                                                                                      | **Colab Notebook**                                                                                                                                                                                                     |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Llama 3.1 (8B) – News Intelligence Chatbot** | 한국 정치경제 뉴스 기반 도메인 지식을 탑재한 챗봇 | <a href="https://colab.research.google.com/drive/1muFqsKnUvQ-hI86JnzCBLXB5HoWhrYWZ#scrollTo=vZ3pXAb1C-Qn" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"></a> |


## 🤖 Streamlit 기반 챗봇
ngrok 기반으로 배포 

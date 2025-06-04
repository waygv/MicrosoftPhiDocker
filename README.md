# MicrosoftPhiDocker

This project runs [Microsoft's Phi-3 Mini (4k Instruct)](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) model locally using Hugging Face Transformers — all inside a lightweight Docker container.

## 📦 Features

- ✅ Supports Hugging Face API token from `.env`
- ✅ Fully containerized using Docker
- ✅ GPU-compatible (optional)
- ✅ Works offline after image is built
- ✅ Easy to run and modify

---

## 📂 Project Structure
├── run.py # Main Python script for inference
├── .env # Your Hugging Face token (keep this secret!)
├── requirements.txt # Python dependencies
└── Dockerfile # Docker setup instructions


---

## 🚀 Getting Started

### Clone the Repository

```
git clone https://github.com/waygv/MicrosoftPhiDocker.git

```

HF_TOKEN=hf_your_actual_token_here
You can get a token from: https://huggingface.co/settings/tokens

### Build the Docker Image and run CPU app
```
docker build -t MicrosoftPhiDocker .
docker run --rm --env-file .env MicrosoftPhiDocker
```
Credits
Hugging Face

Microsoft Phi-3

Docker

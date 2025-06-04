# phi_demo.py
from dotenv import load_dotenv
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login

# Load HF token from .env
load_dotenv()
hf_token = os.getenv("TOKEN")

# Login to Hugging Face
login(token=hf_token)

# Model ID
model_id = "microsoft/Phi-3-mini-4k-instruct"

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype="auto" if torch.cuda.is_available() else torch.float32
)

def generate_answer(question, max_length=200):
    messages = [{"role": "user", "content": question}]
    inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(model.device)
    outputs = model.generate(inputs, max_length=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


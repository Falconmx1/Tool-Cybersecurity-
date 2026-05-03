#!/bin/bash
# Instalación de dependencias para LLM

echo "🔥 Instalando dependencias de LLM..."

# Instalar transformers y torch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers accelerate bitsandbytes datasets peft

# Instalar modelos open-source (alternativa a LLaMA 2)
huggingface-cli login  # Necesitas token

# Descargar modelo Mistral (gratuito, sin solicitud)
python -c "
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained('mistralai/Mistral-7B-Instruct-v0.1')
tokenizer = AutoTokenizer.from_pretrained('mistralai/Mistral-7B-Instruct-v0.1')
print('✅ Modelo Mistral descargado!')
"

# Instalar herramientas adicionales
pip install gradio  # UI web
pip install smtplib email  # Envío de emails
pip install nmap hydra  # Herramientas de pentesting

echo "✅ Todo instalado - Listo para generar ataques con IA"

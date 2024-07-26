# Medical Chatbot using Llama2 nd Pinecone
This repository contains the implementation of a medical chatbot leveraging the LLaMA 2 model. The chatbot extracts data from a PDF file, processes it, and responds to medical inquiries using LangChain, Hugging Face, and Pinecone.



## Features
- Medical Knowledge Base: Extracts and organizes information from a medical PDF.
- LangChain Integration: Processes user queries and matches them with relevant information.
- Llama2 Embeddings: Generates contextual embeddings for accurate information retrieval.
- Pinecone Vector Database: Stores embeddings for efficient search and retrieval.
- User Interface: Provides a user-friendly chatbot interface.
- Flask Backend: Manages user requests and chatbot interactions.

## Tech Stack
- Language: Python
- Framework: LangChain
- Frontend: Flask, HTML, CSS
- LLM: Meta Llama2
- Vector Database: Pinecone


## Installation:

### 1- Clone the Repository

```bash
git clone https://github.com/Ahmed-Farouk-Ibrahim/Medical_Chatbot.git
cd Medical_Chatbot
```

### 2- Create a Conda Environment:
```bash
conda create -p venv python==3.10 -y
conda activate venv/
```

### 3- Install Dependencies:
```bash
pip install -r requirements.txt
```

### 4- Configure Environment Variables:
- Create a `.env` file in the root directory with your Pinecone credentials:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 5- Download the Model: Download the Llama2 model and place it in the model directory:

```ini
## Download the Llama 2 Model:
llama-2-7b-chat.ggmlv3.q4_0.bin

## From the following link:
[Llama2](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin)
```

### 6- Store Vectors in Pinecone:

```bash
# run the following command
python store_index.py
```

### 7- Run the Application:

```bash
python app.py
```

### 8- Access Chatbot Interface
Usage
Open your browser and navigate to http://127.0.0.1:8080 or http://10.2.0.2:8080 to access the chatbot interface.

```bash
open up localhost:
```


## Results

The model was initially evaluated by asking a relevant medical question:

<p align="center">
<image src="static/Screenshot1.png" width="500">
</p>


Subsequently, an unrelated question was posed to test the model's response:

<p align="center">
<image src="static/Screenshot2.png" width="500">
</p>

## Notes :

1. The model's response sometimes may take up to 4 minutes. Your patience is appreciated.

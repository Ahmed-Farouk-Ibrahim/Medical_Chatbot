from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
import pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Retrieve Pinecone API key from environment variables
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

# Download pre-trained Hugging Face embeddings
embeddings = download_hugging_face_embeddings()

# Specify the name of the Pinecone index to be used
index_name = "medical-chatbot"

# Load the existing Pinecone index with the embeddings
docsearch = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)

# Define the prompt template for generating responses
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs = {"prompt": PROMPT}

# Initialize the language model with the specified configuration
llm = CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={'max_new_tokens': 512, 'temperature': 0.8}
)

# Create a RetrievalQA chain using the language model and the document retriever
qa = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs
)

# Define the route for the homepage
@app.route("/")
def index():
    return render_template('chat.html')

# Define the route for handling chat requests
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result = qa.invoke({"query": input})
    print("Response: ", result["result"])
    return str(result["result"])

# Run the Flask app on host 0.0.0.0 and port 8080
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

# Import necessary modules and functions
from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve Pinecone API key from environment variables
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
print(PINECONE_API_KEY)  # For debugging purposes, consider removing or securing this in production

# Load PDF documents from the specified directory
extracted_data = load_pdf("resources/")
# Split the extracted text into manageable chunks
text_chunks = text_split(extracted_data)
print(text_chunks)  # Print the text chunks for verification

# Download and initialize Hugging Face embeddings
embeddings = download_hugging_face_embeddings()
print(embeddings)  # Print the embeddings model instance for verification

# Define the index name for Pinecone
index_name = "medical-chatbot"

# Create a Pinecone vector store from the text chunks and embeddings
docsearch = PineconeVectorStore.from_documents(text_chunks, embedding=embeddings, index_name=index_name)

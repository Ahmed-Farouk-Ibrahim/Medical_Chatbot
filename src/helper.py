# LangChainDeprecationWarning: Importing document loaders from langchain is deprecated. 
# Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# Function to load PDF documents from a specified directory
# This function leverages PyPDFLoader to parse and extract text from PDF files.
# @param data: Path to the directory containing PDF files.
# @return: List of documents extracted from the PDF files.
def load_pdf(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

# Function to split extracted text data into manageable chunks
# This function uses RecursiveCharacterTextSplitter to divide the text into smaller chunks that can be efficiently processed by language models.
# @param extracted_data: List of documents to be split.
# @return: List of text chunks.
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

# Function to download and initialize Hugging Face embeddings
# This function initializes the HuggingFaceEmbeddings model for embedding text data.
# @return: HuggingFaceEmbeddings model instance.
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

# Example usage:
if __name__ == "__main__":
    data_path = "resources/"  # Path to your PDF documents
    extracted_data = load_pdf(data_path)  # Load PDF documents
    text_chunks = text_split(extracted_data)  # Split text into chunks
    print("Number of text chunks:", len(text_chunks))

    embeddings = download_hugging_face_embeddings()  # Initialize embeddings
    query_result = embeddings.embed_query("How are you?")
    print("Query embedding length:", len(query_result))

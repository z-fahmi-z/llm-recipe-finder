from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

import logging

def load_db(hf_embedding_model_name, document_path, separator, verbose=False):
    logging.getLogger("langchain_text_splitters.base").setLevel(logging.ERROR)
    if verbose:
        logging.getLogger("langchain_text_splitters.base").setLevel(logging.NOTSET)
    try:
        raw = TextLoader(document_path, encoding="utf-8").load()
        text_splitter = CharacterTextSplitter(chunk_size=0, chunk_overlap=0, separator=separator)
        documents = text_splitter.split_documents(raw)
        embedding_model = HuggingFaceEmbeddings(
            model_name=hf_embedding_model_name,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': False}
        )
        db = Chroma().from_documents(
            documents,
            embedding=embedding_model,
        )
        return db
    except Exception as e:
        print(f"Error loading database: {e}")
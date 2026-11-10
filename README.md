# Semantic Document Search System

## Project Overview
This project implements a Semantic Document Search System using LangChain and ChromaDB. It retrieves relevant documents based on the meaning of user queries using vector embeddings.

## Objectives
- Understand semantic search using vector embeddings.
- Integrate LangChain with ChromaDB.
- Retrieve the Top-5 relevant documents.
- Calculate similarity distance scores.
- Compare semantic search with keyword-based search.

## Technologies Used
- Python
- LangChain
- ChromaDB
- Sentence Transformers
- Pandas
- Jupyter Notebook

## Features
- Loads an existing ChromaDB database.
- Adds 10 new documents.
- Processes 15 user queries.
- Retrieves Top-5 relevant documents.
- Displays similarity scores.
- Saves search results in CSV files.
- Compares keyword and semantic search.

## Dataset
The project uses AI-related documents covering Artificial Intelligence, Machine Learning, Deep Learning, NLP, Computer Vision, Robotics, Cybersecurity, Cloud Computing, Data Science and Chatbots.

## Output Files
- queries.csv
- search_results.csv
- similarity_scores.csv

## Conclusion
Semantic search improves information retrieval by understanding the meaning and context of queries instead of relying only on exact keyword matches. It provides more relevant results and can be used as the retrieval component of a RAG system.

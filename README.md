# Financial Data Engineering Pipeline

## Overview
A lightweight data pipeline for processing financial documents (PDF) into structured data for downstream RAG systems.

## Features
- PDF parsing
- Data cleaning
- Text chunking
- Structured output (JSON)

## Pipeline
Raw PDF → Parsing → Cleaning → Chunking → Structuring → Output

## Use Case
Provides clean and structured input for LLM-based applications such as RAG systems.

## Challenges
- Handling noisy financial text
- Dealing with inconsistent formatting in PDFs

## Improvements
- Added text cleaning rules to reduce noise
- Optimized chunking strategy for better context preservation

## Future Work
- Table extraction improvement
- Integration with vector database

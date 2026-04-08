"""
NLP Engine for Legal Document Processing
Summarizes documents and extracts key information
"""
from typing import Dict, List, Optional
import spacy
from transformers import pipeline
import logging

logger = logging.getLogger(__name__)


class LegalNLPEngine:
    """NLP engine for processing legal documents"""
    
    def __init__(self, model: str = 'en_core_web_lg'):
        """Initialize NLP engine with spaCy model"""
        try:
            self.nlp = spacy.load(model)
        except OSError:
            logger.warning(f"Model {model} not found. Downloading...")
            import os
            os.system(f"python -m spacy download {model}")
            self.nlp = spacy.load(model)
        
        # Initialize summarizer
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    def summarize_document(self, text: str, max_length: int = 150) -> str:
        """
        Generate summary of legal document
        
        Args:
            text: Full document text
            max_length: Maximum summary length
            
        Returns:
            Summarized text
        """
        try:
            # Chunk text into smaller pieces if needed
            if len(text.split()) > 1000:
                text = ' '.join(text.split()[:1000])
            
            summary = self.summarizer(text, max_length=max_length, min_length=50, do_sample=False)
            return summary[0]['summary_text'] if summary else text[:max_length]
        except Exception as e:
            logger.error(f"Error summarizing document: {str(e)}")
            return text[:max_length]
    
    def extract_key_entities(self, text: str) -> Dict[str, List[str]]:
        """
        Extract named entities from legal text
        
        Args:
            text: Document text
            
        Returns:
            Dictionary of entity types and values
        """
        doc = self.nlp(text)
        
        entities = {
            'PERSON': [],
            'ORG': [],
            'GPE': [],
            'DATE': [],
            'LAW': [],
            'MONEY': []
        }
        
        for ent in doc.ents:
            if ent.label_ in entities:
                if ent.text not in entities[ent.label_]:
                    entities[ent.label_].append(ent.text)
        
        return entities
    
    def extract_sections(self, text: str) -> Dict[str, str]:
        """
        Extract major sections from legal document
        
        Args:
            text: Document text
            
        Returns:
            Dictionary mapping section headers to content
        """
        sections = {}
        current_section = "Introduction"
        current_content = []
        
        lines = text.split('\n')
        for line in lines:
            # Simple heuristic: lines that are short and at start of line are section headers
            if len(line) < 100 and line.isupper() and line.strip():
                if current_section in sections:
                    sections[current_section] = '\n'.join(current_content)
                current_section = line.strip()
                current_content = []
            else:
                current_content.append(line)
        
        sections[current_section] = '\n'.join(current_content)
        return sections
    
    def extract_key_phrases(self, text: str, top_n: int = 10) -> List[str]:
        """Extract important legal phrases"""
        doc = self.nlp(text)
        
        # Extract noun chunks which are often key phrases
        phrases = [chunk.text for chunk in doc.noun_chunks]
        
        # Score by frequency
        phrase_freq = {}
        for phrase in phrases:
            phrase_freq[phrase] = phrase_freq.get(phrase, 0) + 1
        
        # Sort by frequency and return top N
        sorted_phrases = sorted(phrase_freq.items(), key=lambda x: x[1], reverse=True)
        return [phrase for phrase, _ in sorted_phrases[:top_n]]
    
    def process_document(self, document: Dict) -> Dict:
        """
        Complete document processing pipeline
        
        Args:
            document: Raw document with 'content' field
            
        Returns:
            Processed document with extracted information
        """
        text = document.get('content', '')
        
        processed = document.copy()
        processed.update({
            'summary': self.summarize_document(text),
            'entities': self.extract_key_entities(text),
            'sections': self.extract_sections(text),
            'key_phrases': self.extract_key_phrases(text),
            'status': 'document_processed'
        })
        
        return processed

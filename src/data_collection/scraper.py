"""
Legal Sources Data Collection Module
Scrapes data from government, court, and regulatory sources
"""
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class LegalDataScraper:
    """Scrapes legal documents from various sources"""
    
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def scrape_government_sources(self, urls: List[str]) -> List[Dict]:
        """
        Scrape government legal sources
        
        Args:
            urls: List of government website URLs
            
        Returns:
            List of legal documents with metadata
        """
        documents = []
        for url in urls:
            try:
                response = self.session.get(url, headers=self.headers, timeout=self.timeout)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                documents.append({
                    'source': 'government',
                    'url': url,
                    'title': self._extract_title(soup),
                    'content': self._extract_content(soup),
                    'extracted_at': datetime.now().isoformat(),
                    'status': 'pending_processing'
                })
                logger.info(f"Successfully scraped government source: {url}")
            except Exception as e:
                logger.error(f"Error scraping government source {url}: {str(e)}")
        
        return documents
    
    def scrape_court_sources(self, urls: List[str]) -> List[Dict]:
        """Scrape court decision sources"""
        documents = []
        for url in urls:
            try:
                response = self.session.get(url, headers=self.headers, timeout=self.timeout)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                documents.append({
                    'source': 'court',
                    'url': url,
                    'title': self._extract_title(soup),
                    'content': self._extract_content(soup),
                    'decision_date': self._extract_date(soup),
                    'extracted_at': datetime.now().isoformat(),
                    'status': 'pending_processing'
                })
                logger.info(f"Successfully scraped court source: {url}")
            except Exception as e:
                logger.error(f"Error scraping court source {url}: {str(e)}")
        
        return documents
    
    def scrape_regulatory_sources(self, urls: List[str]) -> List[Dict]:
        """Scrape regulatory agency sources"""
        documents = []
        for url in urls:
            try:
                response = self.session.get(url, headers=self.headers, timeout=self.timeout)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                documents.append({
                    'source': 'regulator',
                    'url': url,
                    'title': self._extract_title(soup),
                    'content': self._extract_content(soup),
                    'extracted_at': datetime.now().isoformat(),
                    'status': 'pending_processing'
                })
                logger.info(f"Successfully scraped regulatory source: {url}")
            except Exception as e:
                logger.error(f"Error scraping regulatory source {url}: {str(e)}")
        
        return documents
    
    def fetch_from_url(self, url: str) -> Optional[Dict]:
        """Fetch a single document from URL"""
        try:
            response = self.session.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            return {
                'url': url,
                'title': self._extract_title(soup),
                'content': self._extract_content(soup),
                'extracted_at': datetime.now().isoformat(),
                'status': 'pending_processing'
            }
        except Exception as e:
            logger.error(f"Error fetching URL {url}: {str(e)}")
            return None
    
    @staticmethod
    def _extract_title(soup: BeautifulSoup) -> str:
        """Extract title from page"""
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.get_text(strip=True)
        
        h1_tag = soup.find('h1')
        if h1_tag:
            return h1_tag.get_text(strip=True)
        
        return "Untitled Document"
    
    @staticmethod
    def _extract_content(soup: BeautifulSoup) -> str:
        """Extract main content from page"""
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text
        text = soup.get_text(separator='\n', strip=True)
        return text[:5000]  # Limit to 5000 characters
    
    @staticmethod
    def _extract_date(soup: BeautifulSoup) -> Optional[str]:
        """Extract date from page if available"""
        date_patterns = ['date', 'decided', 'judgment-date', 'decision-date']
        
        for pattern in date_patterns:
            element = soup.find(class_=pattern)
            if element:
                return element.get_text(strip=True)
        
        return None

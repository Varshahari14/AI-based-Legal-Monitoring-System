"""
Configuration settings for the AI Legal Monitoring System
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Application Settings
APP_NAME = "AI Legal Monitoring System"
APP_VERSION = "1.0.0"
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./legal_monitor.db')

# NLP Model Configuration
NLP_MODEL = os.getenv('NLP_MODEL', 'en_core_web_lg')
TRANSFORMERS_MODEL = os.getenv('TRANSFORMERS_MODEL', 'distilbert-base-uncased')

# Alert Configuration
ALERT_EMAIL_ENABLED = os.getenv('ALERT_EMAIL_ENABLED', 'True').lower() == 'true'
ALERT_SMS_ENABLED = os.getenv('ALERT_SMS_ENABLED', 'False').lower() == 'true'
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
SENDER_EMAIL = os.getenv('SENDER_EMAIL', '')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD', '')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', '')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', '')

# API Configuration
API_HOST = os.getenv('API_HOST', '0.0.0.0')
API_PORT = int(os.getenv('API_PORT', '5000'))
API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))

# Data Collection
SCRAPER_TIMEOUT = int(os.getenv('SCRAPER_TIMEOUT', '10'))
LEGAL_SOURCES = {
    'government': ['https://example.gov/laws', 'https://example.gov/updates'],
    'courts': ['https://courts.example.gov'],
    'regulators': ['https://regulators.example.gov']
}

# Risk Levels
RISK_LEVELS = ['Low', 'Medium', 'High']

# Audit Trail
AUDIT_LOG_FILE = os.getenv('AUDIT_LOG_FILE', './logs/audit.log')
MAX_LOG_SIZE_MB = int(os.getenv('MAX_LOG_SIZE_MB', '10'))

# Cache Settings
CACHE_ENABLED = os.getenv('CACHE_ENABLED', 'True').lower() == 'true'
CACHE_TTL_SECONDS = int(os.getenv('CACHE_TTL_SECONDS', '3600'))

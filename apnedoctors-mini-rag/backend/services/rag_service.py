
# backend/services/rag_service.py
import asyncio
import logging
from typing import List, Optional, Dict, Any
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import numpy as np
from tenacity import retry, stop_after_attempt, wait_exponential

from ..models.response_models import SymptomResponse, MedicalCondition, UrgencyLevel
from ..utils.medical_disclaimer import MEDICAL_DISCLAIMER, EMERGENCY_DISCLAIMER

logger = logging.getLogger(__name__)

class RAGService:
    """RAG service for medical symptom analysis using ChromaDB and SentenceTransformers"""
    
    def __init__(self, collection_name: str = "medical_knowledge"):
        self.initialized = False
        self.collection_name = collection_name
        self.embedding_model = None
        self.db_client = None
        self.collection = None
        
    async def initialize(self):
        """Initialize RAG service with ChromaDB and embedding model"""
        if self.initialized:
            return
            
        logger.info("Initializing RAG service...")
        
        # Initialize embedding model
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Initialize ChromaDB
        self.db_client = chromadb.Client(Settings(
            persist_directory="./data/chroma_db",
            anonymized_telemetry=False
        ))
        
        try:
            self.collection = self.db_client.get_collection(self.collection_name)
            logger.info("Found existing collection")
        except ValueError:
            logger.info("Creating new collection")
            self.collection = self.db_client.create_collection(
                name=self.collection_name,
                metadata={"description": "Medical knowledge base for symptom analysis"}
            )
            await self._initialize_medical_knowledge()
        
        self.initialized = True
        logger.info("RAG service initialized successfully")

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def process_symptoms(
        self,
        symptoms: str,
        patient_age: Optional[int] = None,
        patient_gender: Optional[str] = None,
        medical_history: Optional[List[str]] = None
    ) -> SymptomResponse:
        """Process symptom query using RAG pipeline"""
        if not self.initialized:
            await self.initialize()

        # Emergency keywords check
        emergency_keywords = ["chest pain", "difficulty breathing", "severe bleeding",
                            "unconscious", "stroke", "heart attack"]
        if any(keyword in symptoms.lower() for keyword in emergency_keywords):
            return self._create_emergency_response()

        # Query vector database
        query_embedding = self.embedding_model.encode(symptoms)
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=5
        )
            confidence_score=0.7,
            clarifying_questions=[
                "How long have you had these symptoms?",
                "Any fever or other symptoms?"
            ]
        )
    
    async def health_check(self) -> Dict[str, Any]:
        """Health check for RAG service"""
        return {
            "initialized": self.initialized,
            "status": "healthy"
        }
    
    async def cleanup(self):
        """Cleanup resources"""
        logger.info("RAG service cleaned up")

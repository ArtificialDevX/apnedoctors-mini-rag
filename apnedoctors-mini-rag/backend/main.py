
# backend/main.py
import asyncio
import logging
import os
from contextlib import asynccontextmanager
from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

try:
    from .services.rag_service import RAGService
    from .models.request_models import SymptomQuery
    from .models.response_models import SymptomResponse
    from .utils.medical_disclaimer import MEDICAL_DISCLAIMER
except ImportError:
    from services.rag_service import RAGService
    from models.request_models import SymptomQuery
    from models.response_models import SymptomResponse
    from utils.medical_disclaimer import MEDICAL_DISCLAIMER

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global RAG service instance
rag_service = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    global rag_service
    
    logger.info("🚀 Starting ApneDoctors Mini-RAG Service...")
    
    try:
        # Initialize RAG service
        rag_service = RAGService()
        await rag_service.initialize()
        logger.info("✅ RAG Service initialized successfully")
        
        yield
        
    except Exception as e:
        logger.error(f"❌ Failed to initialize RAG service: {str(e)}")
        raise
    finally:
        logger.info("🛑 Shutting down ApneDoctors Mini-RAG Service...")
        if rag_service:
            await rag_service.cleanup()

# Create FastAPI app
app = FastAPI(
    title="ApneDoctors Mini-RAG API",
    description="AI-powered symptom checker with RAG-based medical knowledge",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "service": "ApneDoctors Mini-RAG",
        "status": "healthy",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    """Detailed health check"""
    try:
        if not rag_service:
            raise HTTPException(status_code=503, detail="RAG service not initialized")
        
        health_status = await rag_service.health_check()
        return {
            "status": "healthy",
            "rag_service": health_status,
            "disclaimer": MEDICAL_DISCLAIMER
        }
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=503, detail="Service unhealthy")

@app.post("/ask", response_model=SymptomResponse)
async def ask_symptoms(query: SymptomQuery):
    """Process symptom query and return medical insights"""
    try:
        if not rag_service:
            raise HTTPException(status_code=503, detail="RAG service not available")
        
        logger.info(f"Processing symptom query: {query.symptoms[:100]}...")
        
        response = await rag_service.process_symptoms(
            symptoms=query.symptoms,
            patient_age=query.patient_age,
            patient_gender=query.patient_gender,
            medical_history=query.medical_history
        )
        
        logger.info(f"Generated response with {len(response.possible_conditions)} conditions")
        return response
        
    except Exception as e:
        logger.error(f"Error processing symptom query: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process symptoms")

@app.get("/disclaimer")
async def get_disclaimer():
    """Get medical disclaimer"""
    return {"disclaimer": MEDICAL_DISCLAIMER}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

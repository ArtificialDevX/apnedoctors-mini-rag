
# backend/models/response_models.py
from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum

class UrgencyLevel(str, Enum):
    """Urgency levels for medical conditions"""
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"

class MedicalCondition(BaseModel):
    """Model representing a possible medical condition"""
    
    name: str = Field(
        ...,
        description="Name of the medical condition",
        example="Common Cold"
    )
    
    probability: float = Field(
        ...,
        description="Probability/confidence score (0-1)",
        ge=0.0,
        le=1.0,
        example=0.75
    )
    
    description: str = Field(
        ...,
        description="Brief description of the condition",
        example="A viral infection affecting the upper respiratory system"
    )
    
    symptoms: List[str] = Field(
        ...,
        description="Common symptoms associated with this condition",
        example=["runny nose", "cough", "sore throat", "low-grade fever"]
    )
    
    risk_factors: Optional[List[str]] = Field(
        None,
        description="Risk factors that increase likelihood",
        example=["close contact with infected person", "weakened immune system"]
    )

class SymptomResponse(BaseModel):
    """Response model for symptom analysis"""
    
    possible_conditions: List[MedicalCondition] = Field(
        ...,
        description="List of possible medical conditions ranked by probability",
        min_items=1,
        max_items=5
    )
    
    urgency: UrgencyLevel = Field(
        ...,
        description="Overall urgency level for seeking medical care",
        example=UrgencyLevel.MODERATE
    )
    
    suggestions: List[str] = Field(
        ...,
        description="Recommended next steps and self-care suggestions",
        example=[
            "Rest and stay hydrated",
            "Monitor temperature",
            "Consult healthcare provider if symptoms worsen"
        ]
    )
    
    confidence_score: float = Field(
        ...,
        description="Overall confidence in the analysis (0-1)",
        ge=0.0,
        le=1.0,
        example=0.82
    )
    
    clarifying_questions: Optional[List[str]] = Field(
        None,
        description="Questions to help narrow down the diagnosis",
        example=[
            "How long have you had these symptoms?",
            "Have you been in contact with anyone who was sick?"
        ]
    )
    
    red_flags: Optional[List[str]] = Field(
        None,
        description="Warning signs that require immediate medical attention",
        example=[
            "Difficulty breathing",
            "High fever above 103°F",
            "Severe chest pain"
        ]
    )
    
    disclaimer: str = Field(
        default="This is for educational purposes only and should not replace professional medical advice. Please consult a healthcare provider for proper diagnosis and treatment.",
        description="Medical disclaimer"
    )
    
    query_id: Optional[str] = Field(
        None,
        description="Unique identifier for this query/response pair",
        example="query_123456789"
    )

class HealthCheckResponse(BaseModel):
    """Response model for health check endpoint"""
    
    status: str = Field(
        ...,
        description="Service status",
        example="healthy"
    )
    
    version: str = Field(
        ...,
        description="API version",
        example="1.0.0"
    )
    
    rag_service: dict = Field(
        ...,
        description="RAG service status details"
    )
    
    uptime: Optional[float] = Field(
        None,
        description="Service uptime in seconds",
        example=3600.0
    )

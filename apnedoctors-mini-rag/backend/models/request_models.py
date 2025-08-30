
# backend/models/request_models.py
from typing import List, Optional
from pydantic import BaseModel, Field

class SymptomQuery(BaseModel):
    """Request model for symptom queries"""
    
    symptoms: str = Field(
        ...,
        description="Patient's symptom description",
        min_length=3,
        max_length=1000,
        example="I have been experiencing fever, headache, and body aches for the past 2 days"
    )
    
    patient_age: Optional[int] = Field(
        None,
        description="Patient's age in years",
        ge=0,
        le=120,
        example=35
    )
    
    patient_gender: Optional[str] = Field(
        None,
        description="Patient's gender",
        regex="^(male|female|other|prefer_not_to_say)$",
        example="female"
    )
    
    medical_history: Optional[List[str]] = Field(
        None,
        description="List of known medical conditions",
        example=["diabetes", "hypertension"]
    )
    
    severity: Optional[str] = Field(
        None,
        description="Patient's perception of symptom severity",
        regex="^(mild|moderate|severe)$",
        example="moderate"
    )
    
    duration: Optional[str] = Field(
        None,
        description="How long symptoms have been present",
        example="2 days"
    )

class FeedbackRequest(BaseModel):
    """Request model for user feedback"""
    
    query_id: str = Field(
        ...,
        description="ID of the original query",
        example="query_123456"
    )
    
    rating: int = Field(
        ...,
        description="User rating (1-5 stars)",
        ge=1,
        le=5,
        example=4
    )
    
    feedback_text: Optional[str] = Field(
        None,
        description="Optional feedback text",
        max_length=500,
        example="The suggestions were helpful, but I'd like more specific guidance"
    )
    
    was_helpful: bool = Field(
        ...,
        description="Whether the response was helpful",
        example=True
    )

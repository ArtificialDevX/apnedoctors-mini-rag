
# backend/utils/medical_disclaimer.py
"""
Medical disclaimers and legal notices for ApneDoctors
"""

MEDICAL_DISCLAIMER = """
IMPORTANT MEDICAL DISCLAIMER:

The information provided by ApneDoctors is for educational and informational purposes only and is not intended to be a substitute for professional medical advice, diagnosis, or treatment.

⚠️ ALWAYS SEEK PROFESSIONAL MEDICAL ADVICE:
- Consult qualified healthcare providers for any medical concerns
- Do not disregard professional medical advice based on information from this service
- Never delay seeking medical care because of information provided here

🚨 EMERGENCY SITUATIONS:
- Call emergency services (911) immediately for life-threatening conditions
- Go to the nearest emergency room for urgent medical situations
- This service cannot replace emergency medical care

📋 LIMITATIONS:
- This AI system provides general information only
- Individual medical situations vary greatly
- Diagnosis requires proper medical examination and testing
- Treatment plans must be developed by qualified medical professionals

By using this service, you acknowledge that you understand these limitations and agree to consult healthcare professionals for any medical decisions.

Last updated: August 2025
"""

EMERGENCY_DISCLAIMER = """
🚨 MEDICAL EMERGENCY WARNING 🚨

If you are experiencing a medical emergency, DO NOT use this service.

CALL 911 IMMEDIATELY or go to the nearest emergency room if you have:
• Chest pain or pressure
• Difficulty breathing
• Severe bleeding
• Loss of consciousness
• Stroke symptoms (face drooping, arm weakness, speech problems)
• Severe abdominal pain
• High fever with confusion
• Thoughts of harming yourself or others

This service is NOT a substitute for emergency medical care.
"""

SHORT_DISCLAIMER = "This information is for educational purposes only. Always consult healthcare professionals for medical advice, diagnosis, or treatment."

URGENCY_DISCLAIMERS = {
    "high": "⚠️ HIGH URGENCY: Seek immediate medical attention. Call 911 or go to emergency room.",
    "moderate": "⚠️ MODERATE URGENCY: Contact healthcare provider within 24 hours or sooner if symptoms worsen.",
    "low": "ℹ️ LOW URGENCY: Monitor symptoms and consider consulting healthcare provider if they persist or worsen."
}

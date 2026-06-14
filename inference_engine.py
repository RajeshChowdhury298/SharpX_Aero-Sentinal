import os
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import Optional
from loguru import logger

# 1. Initialize the Google GenAI Client
# It automatically looks for the GEMINI_API_KEY environment variable.
if not os.getenv("GEMINI_API_KEY"):
    logger.error("❌ GEMINI_API_KEY environment variable is missing. Please set it before running.")
client = genai.Client()

# 2. Define the Target Structure using Pydantic
# This acts as a forced blueprint. Gemini is mathematically restricted to output only these fields.
class FleetComponentAnalysis(BaseModel):
    aircraft_tail_id: str = Field(description="The matching tail identification code of the aircraft, e.g., VT-IFA.")
    airport_code: str = Field(description="The 3-letter IATA code of the current destination airport, e.g., BOM, DEL.")
    system_category: str = Field(description="The underlying high-level aircraft system module (Hydraulics, Flight Controls, Pneumatics, Avionics, Landing Gear, Fuel System).")
    inferred_part_needed: str = Field(description="The explicit nomenclature name of the hardware part or valve that needs troubleshooting or replacement.")
    part_serial_code: str = Field(description="The clean identification alphanumeric serial part asset key, e.g., HAV-9902, EDP-9921.")
    urgency_rating: str = Field(description="Must be strictly classified as CRITICAL_AOG if immediate grounding is implied, or ROUTINE_WATCH if simple life threshold monitoring.")

# 3. Core Engine Action Call
def analyze_unstructured_log(raw_text: str) -> Optional[FleetComponentAnalysis]:
    """
    Passes raw aircraft telemetry data blocks into Gemini Flash 
    and applies a Pydantic constraint mapping wrapper.
    """
    try:
        system_prompt = (
            "You are an expert Chief Aviation Systems Logistics and Maintenance Engineer. "
            "Analyze the provided raw operational diagnostic log block. "
            "Isolate corporate entity markers, location constraints, parts identifiers, and asset serial codes."
        )

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Extract insights from this record: {raw_text}",
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json",
                response_schema=FleetComponentAnalysis,
                temperature=0.1 # Low temperature ensures focused, factual data extraction
            ),
        )
        
        # The SDK automatically loads and maps the JSON response right into our Pydantic object
        parsed_data: FleetComponentAnalysis = response.parsed
        return parsed_data

    except Exception as e:
        logger.error(f"Failed to process inference via Gemini API: {str(e)}")
        return None

# Simple testing suite execution loop block
if __name__ == "__main__":
    test_sample = (
        "Flight AI-204 safely landed at DEL (Delhi). During post-flight diagnostics, cockpit warning code triggered. "
        "Data streams indicate a sudden pressure drop inside the Hydraulic EDP (Engine-Driven Pump) (EDP-9921). "
        "Ground engineers recommend urgent replacement before next flight rotation to prevent an operational grounding."
    )
    logger.info("📡 Testing Gemini Structured Inference Engine...")
    result = analyze_unstructured_log(test_sample)
    if result:
        print("\n🔥 [AI EXTRACTED SCHEMA] 🔥")
        print(result.model_dump_json(indent=2))
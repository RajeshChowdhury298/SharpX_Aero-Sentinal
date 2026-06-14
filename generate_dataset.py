import random
import pandas as pd
from datetime import datetime, timedelta

# 1. Seed configurations for realistic Indian Aviation context
tail_numbers = [f"VT-IF{chr(i)}{chr(j)}" for i in range(65, 70) for j in range(65, 75)]  # Generates realistic tail IDs like VT-IFA, VT-IFB
airports = ["BOM (Mumbai)", "DEL (Delhi)", "BLR (Bengaluru)", "MAA (Chennai)", "CCU (Kolkata)", "HYD (Hyderabad)", "NAG (Nagpur)"]

components = [
    {"name": "Hydraulic EDP (Engine-Driven Pump)", "code": "EDP-9921", "system": "Hydraulics"},
    {"name": "Hydraulic Actuator Valve", "code": "HAV-9902", "system": "Flight Controls"},
    {"name": "Main Landing Gear Brake Assembly", "code": "MLG-B44", "system": "Landing Gear"},
    {"name": "Bleed Air Pressure Regulator", "code": "BPR-101", "system": "Pneumatics"},
    {"name": "Avionics Cooling Fan Motor", "code": "ACF-773", "system": "Avionics"},
    {"name": "Fuel Booster Pump Filter Element", "code": "FBP-551", "system": "Fuel System"}
]

templates = [
    "Flight {flight_no} safely landed at {airport}. During post-flight diagnostics, cockpit warning code triggered. Data streams indicate a sudden pressure drop inside the {comp_name} ({comp_code}). Ground engineers recommend urgent replacement before next flight rotation to prevent an operational grounding.",
    "Post-flight inspection report for aircraft {tail_id} at {airport} terminal hangar. Maintenance logs recorded irregular feedback loop signals and fluctuating thermal metrics from the {comp_name} assembly. Part number {comp_code} requires inspection or complete swap.",
    "Alert: Routine sensor diagnostic check on aircraft {tail_id} at {airport} flagged critical wear tolerances. The {comp_name}, serialized under asset code {comp_code}, has crossed its safe operational life threshold. Maintenance dispatch required immediately.",
    "Log transcript for flight arriving at {airport}. Flight deck reported a minor telemetry mismatch in the {system} unit. Cross-examination confirms the issue isolates directly to the {comp_name} (Part ID: {comp_code}). Replacement component must be sourced to avoid an active Aircraft-on-Ground (AOG) event."
]

def generate_mock_logs(count=500):
    dataset = []
    base_time = datetime.now()
    
    for i in range(count):
        tail_id = random.choice(tail_numbers)
        airport = random.choice(airports)
        comp = random.choice(components)
        template = random.choice(templates)
        flight_no = f"AI-{random.randint(100, 999)}"
        timestamp = (base_time - timedelta(minutes=random.randint(1, 10000))).strftime("%Y-%m-%d %H:%M:%S")
        
        # Build the unstructured textual log block
        log_text = template.format(
            flight_no=flight_no,
            airport=airport,
            tail_id=tail_id,
            comp_name=comp["name"],
            comp_code=comp["code"],
            system=comp["system"]
        )
        
        dataset.append({
            "log_id": f"AERO-2026-{i+1:04d}",
            "timestamp": timestamp,
            "tail_number": tail_id,
            "airport_location": airport.split(" ")[0], # Extracts just BOM, DEL, etc.
            "raw_diagnostic_text": log_text
        })
        
    df = pd.DataFrame(dataset)
    df.to_csv("aircraft_technical_logs.csv", index=False)
    print(f"✅ Successfully generated {count} mock aviation diagnostic records inside 'aircraft_technical_logs.csv'!")

if __name__ == "__main__":
    generate_mock_logs(500)
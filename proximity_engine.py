import os
import math
from typing import List, Dict, Optional
from supabase import create_client, Client
from loguru import logger

# 💥 FIX: Hardcode strings directly into the client creation parameters
supabase: Client = create_client(
    "https://ttunjthzontnuvezeldr.supabase.co",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR0dW5qdGh6b250bnV2ZXplbGRyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE0MjY5OTUsImV4cCI6MjA5NzAwMjk5NX0.XJY8gKjsAx-p1mhm3-MOONdxM2kqL-3ojLZHchMHzh4"
)

def calculate_haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculates Great-Circle distance between two coordinates in Kilometers."""
    R = 6371.0 # Radius of the earth in KM
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = (math.sin(dlat / 2) ** 2 + 
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)

def locate_closest_part_stock(target_airport: str, required_part_code: str) -> Optional[Dict]:
    """Queries Supabase to find all warehouses holding stock of the required component."""
    try:
        clean_target = str(target_airport).strip().upper()
        clean_part = str(required_part_code).strip().upper()

        # 1. Fetch coordinates of the current airport where aircraft is grounded
        station_query = supabase.table("aviation_warehouses").select("*").eq("airport_code", clean_target).execute()
        if not station_query.data:
            logger.warning(f"Station coordinates for {clean_target} not mapped in system framework.")
            return None
            
        origin = station_query.data[0]
        origin_lat, origin_lon = origin["latitude"], origin["longitude"]
        
        # 2. Query parts inventory linked with warehouse geolocation coordinates
        inventory_query = supabase.table("parts_inventory").select(
            "stock_count, aviation_warehouses(hub_name, airport_code, latitude, longitude)"
        ).eq("part_serial_code", clean_part).gt("stock_count", 0).execute()
        
        available_stocks = inventory_query.data
        if not available_stocks:
            return None
            
        closest_warehouse = None
        minimum_distance = float('inf')
        
        # 3. Spatial Proximity Calculation Loop
        for stock in available_stocks:
            wh_data = stock["aviation_warehouses"]
            if not wh_data:
                continue
                
            distance = calculate_haversine_distance(
                origin_lat, origin_lon, 
                wh_data["latitude"], wh_data["longitude"]
            )
            
            if distance < minimum_distance:
                minimum_distance = distance
                closest_warehouse = {
                    "hub_name": wh_data["hub_name"],
                    "airport_code": wh_data["airport_code"],
                    "available_stock": stock["stock_count"],
                    "distance_km": distance
                }
                
        return closest_warehouse

    except Exception as e:
        logger.error(f"Error executing database spatial proximity query: {str(e)}")
        return None

if __name__ == "__main__":
    logger.info("📡 Testing Supabase Cloud Spatial Proximity Engine...")
    res = locate_closest_part_stock("BOM", "EDP-9921")
    if res:
        print(f"\n✅ OPTIMAL COURIER HUB RESOLVED:\nTarget: BOM\nClosest Supplier: {res['hub_name']} ({res['airport_code']})\nDistance: {res['distance_km']} KM\nStock Available: {res['available_stock']} units")
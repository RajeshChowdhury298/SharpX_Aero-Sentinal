from supabase import create_client, Client

# Use the exact hardcoded setup from your engine
url = "https://ttunjthzontnuvezeldr.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR0dW5qdGh6b250bnV2ZXplbGRyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE0MjY5OTUsImV4cCI6MjA5NzAwMjk5NX0.XJY8gKjsAx-p1mhm3-MOONdxM2kqL-3ojLZHchMHzh4"

sb: Client = create_client(url, key)

print("🔍 Reading 'aviation_warehouses' directly from cloud...")
res = sb.table("aviation_warehouses").select("*").execute()

print(f"📊 Total Rows Found: {len(res.data)}")
for row in res.data:
    print(f"✈️ Airport Code: '{row['airport_code']}' | Name: {row['hub_name']}")
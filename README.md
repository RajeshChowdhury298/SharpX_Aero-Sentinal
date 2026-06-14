# 🛡️ Aero-Sentinel: Autonomous Real-Time Supply Chain Resiliency & Logistics Engine

**Aero-Sentinel** is an event-driven, production-grade AI core and spatial logistics pipeline engineered to eliminate **Aircraft-on-Ground (AOG)** delays. The platform ingests chaotic, unstructured maintenance text logs, leverages an agentic LLM layer to extract structural asset telemetry, performs live spatial proximity routing against a distributed cloud database framework, and deploys localized field communication dispatches wrapped in an interactive, expert-validated audit dashboard loop.

---

## 🏗️ Technical Architecture & Workflow Topology

Aero-Sentinel operates across a decoupled, multi-tier pipeline to guarantee high throughput, zero-latency ingestion, and safety-critical extraction:



1. **Ingestion Matrix (`FastAPI` + `Pydantic`):** Exposes an asynchronous ingest node capable of handling bulk snapshot records concurrently without resource stalls or thread-blocking.
2. **Cognitive Inference Tier (`Google GenAI SDK` / `gemini-2.5-flash`):** Uses system instruction constraints and structural schema enforcement to instantly map unstructured engineering descriptions into deterministic Python objects.
3. **Proximity & Spatial Engine (`Supabase` + `PostgreSQL`):** Queries a distributed cloud data warehouse of Indian aviation hubs, utilizing mathematical spherical coordinate logic (Haversine equation) to match parts and calculate precise routing distances live.
4. **Notification Gateway (`Twilio REST API`):** Intercepts geographic matching parameters to push real-time emergency alert payloads directly to on-duty engineers' WhatsApp accounts, accompanied by a secure local validation link.
5. **Human-in-the-Loop Gateway (`Jinja2 Templates` + `TailwindCSS` + `Leaflet JS`):** Provides a robust 5-point verification audit scorecard layout safeguarding against false alerts or AI hallucinations before authorizing secure procurement tokens.

---

## 🛠️ Tech Stack Component Matrix

| Pipeline Tier | Technology Used | Architectural Duty |
| :--- | :--- | :--- |
| **Backend Core** | Python 3.13 / FastAPI | Asynchronous streaming intake grid with background task optimization flags. |
| **Cognitive Logic**| Gemini 2.5 Flash API | Structural entity parsing, module tracking, and semantic log token mapping. |
| **Cloud Database** | Supabase (PostgreSQL) | Geolocation matrix registry, spatial GPS ledgering, and stock count tracking. |
| **Alert Engine** | Twilio WhatsApp Gateway | Live REST template dispatch channel forwarding emergency parameter payloads. |
| **Command Portal** | Jinja2 Templates | Server-side template rendering with strict state-locking parameters. |
| **Frontend Web UI** | Tailwind CSS v4 | High-fidelity, responsive typography, and minimalist dark-mode layout controls. |
| **Spatial Map UI** | Leaflet JS / OpenStreetMap | Real-time geodesic routing vector lines mapping supply chains between nodes. |

---

## 📋 Human-in-the-Loop Safety Auditing & Verification Pipeline

Aero-Sentinel addresses a critical industry problem: **AI Hallucinations and Sensor False Positives.** To prevent runaway automated systems from ordering expensive hardware incorrectly, the procurement dispatch path is completely locked behind a **5-Point Expert Audit Survey**:

1. Is the AI extracted data metadata correct and valid?
2. Does this specific airframe model really need repairs?
3. Is part model asset code urgently needed?
4. Is the AI suggested part correct according to default defaults?
5. AI suggested this specific part for this defect, does this part correct according to the default?

### 🔄 Dynamic UI Conditional Logic Rules:
* **100% Positive Consensus (All Yes):** Dynamically unlocks the green **`Approve Asset Deployment`** portal, opening up direct vendor communication channels and an active survey checklist.
* **100% Negative Consensus (All No):** Dynamically unlocks the red **`Decline & Reject AI Entry`** portal to immediately wipe out the invalid incident alert framework.
* **Mixed Parameters:** Instantly halts the autonomous pipeline, warning the operator and routing the telemetry profile directly to the manual engineering control tower queue.

### 📞 Direct Vendor Communication Portal
Once unlocked via the verification gate, the app generates a localized hardware-linked contact deck (`tel:`, `sms:`, and `mailto:` targets) mapped to the selected closest warehouse operator data fields, allowing managers to establish an immediate voice call, text message, or pre-formatted email draft right from the canvas.

### 🛫 Post-Audit Survey & Jet Takeoff Animation
Upon completing the granular multi-choice performance survey (rating the AI as *Correct*, *Partially Correct*, or *Totally Wrong*) and typing diagnostic summaries, hitting submit triggers a hardware-accelerated CSS jet engine takeoff animation screen (`🛫`) signifying successful clearance. The system securely saves the metrics to the backend and loops the user back to the primary central command command-center layout.

---

## 📂 Repository Directory Layout

```font-mono
Aero-Sentinel/
├── main.py                    # Core FastAPI Engine, Endpoints, and Jinja2 View App Routers
├── proximity_engine.py         # Haversine Coordinate Distance Calculations & Supabase Handlers
├── communication_gateway.py    # Twilio REST Client API Outbound Template Composers
├── check_db.py                # Cloud Table Ingestion Integrity Debugging Diagnostic Utility
├── test_stream.py             # Mock Log Simulator Injecting 500-Payload Snapshots
├── templates/
│   ├── dossier.html           # Leaflet Map Engine, 5-Point Validation Survey, & Vendor Comms
│   └── thanks.html            # Hardware-Accelerated CSS Jet Plane Takeoff Animation View
└── .gitignore                 # Environment Isolation Safeguard Buffer Matrix

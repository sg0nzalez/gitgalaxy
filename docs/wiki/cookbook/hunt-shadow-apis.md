# How to Hunt Shadow APIs and Undocumented Endpoints

In modern microservice architectures, documentation drift is inevitable. Developers rapidly add endpoints to Express, FastAPI, or Spring Boot controllers, but forget to update the official OpenAPI/Swagger specifications. 

When security teams audit the application, they only test the documented endpoints. This leaves undocumented **Shadow APIs** (like legacy `v1` routes or unauthenticated `/debug` endpoints) exposed to the public internet, creating a massive blind spot for attackers to exploit.

GitGalaxy closes this gap using the **Full API Network Map**, comparing the physical routing logic compiled in your source code against your official security documentation using mathematical Set Theory.

## The Network Mapper

Instead of relying on network traffic sniffing (which misses dormant endpoints), GitGalaxy uses AST-free structural parsing to extract the exact physical routing reality directly from the source code across Python, Node.js, Java, and Golang.

### 1. Execute the Scan
Point the mapper at your source code directory and provide the official `swagger.json` or `openapi.yaml` file.

```bash
python gitgalaxy/tools/network_auditing/full_api_network_map.py /path/to/source_code --swagger /path/to/official_swagger.json
```

### 2. Analyze the Gap (Set Theory)
The engine builds two sets of data: the *Approved APIs* (from Swagger) and the *Physical APIs* (from the code). It then subtracts the sets to immediately highlight the discrepancies.

* **Shadow APIs:** Code that is physically active and listening for traffic, but hidden from the security team. 
* **Ghost APIs:** Endpoints that the security team thinks exist, but have actually been deleted from the codebase (Documentation Bloat).

```text
==========================================================
 📡 SHADOW API SECURITY AUDIT
==========================================================
 Documented Endpoints (Swagger) : 42
 Physical Endpoints (Source)    : 45
----------------------------------------------------------
 🚨 SHADOW APIS DETECTED: 3 (Critical Risk)
    ↳ GET /api/v1/users/debug [Found in: debug_controller.py]
    ↳ POST /api/admin/flush   [Found in: admin_routes.js]
    ↳ GET /health/internal    [Found in: health.go]

----------------------------------------------------------
 👻 GHOST APIS DETECTED: 2 (Documentation Bloat)
    ↳ PUT /api/v1/payments    [Missing from source code]
    ↳ DELETE /api/v1/legacy   [Missing from source code]
==========================================================
```

### 3. Security Remediation
Every Shadow API represents a critical security risk. Because the tool outputs the exact filename where the rogue route is defined (`admin_routes.js`), DevSecOps can immediately open a ticket to either:
1. Delete the forgotten code.
2. Officially document the endpoint in the Swagger file so it falls under the jurisdiction of the Web Application Firewall (WAF) and authentication middleware.

> **Read the full technical specification:** [Full API Network Map](../04-01-full-api-network-map.md)
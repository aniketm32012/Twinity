# 🚀 Twinity Search

**Twinity Search** is a high-performance, locally hosted web search ecosystem designed to combine real-time web retrieval, direct brand navigation, and instant AI-powered synthesis into a single interface. 

Built with **Python (Flask)** and integrated with **Google's Gemini API**, Twinity Search functions as a lightweight local server that resolves directly to `http://twinity.localhost` without complex port management or system configuration.

---

### ✨ Key Features

* **Zero-Port Local Domain (`twinity.localhost`):** Runs seamlessly on standard local loopback routes with automatic port-fallback logic for non-admin environments.
* **Multi-Source Web Search:** Pulls results across direct brand redirects, DuckDuckGo, and Wikipedia APIs in parallel.
* **Nova AI Synthesis Proxy:** Summarizes raw web results into clean, actionable insights via the latest Gemini Flash endpoints.
* **Multi-Model Auto-Fallback Cascade:** Automatically handles API rate limits and high-demand spikes by seamlessly routing requests through backup models.
* **Zero Host Modifications:** Public-repo ready! Works out of the box without editing OS `hosts` files or changing system paths.

---

### 🛠️ Tech Stack

* **Backend:** Python, Flask, Flask-CORS, Requests
* **Frontend:** HTML5, CSS3, Modern JavaScript (Fetch API)
* **AI Engine:** Google Gemini API (`v1beta`)

---

### 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/twinity-search.git](https://github.com/YOUR_USERNAME/twinity-search.git)
   cd twinity-search

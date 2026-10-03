# GBP Audit MCP Server

A Claude MCP server for auditing and editing Google Business Profiles across multiple locations.

## What it does

| Tool | Description |
|---|---|
| `list_accounts` | List all GBP accounts you manage |
| `list_locations` | List all locations under an account |
| `audit_location` | Audit one location and flag missing fields |
| `audit_all_locations` | Audit every location under an account |
| `get_services` | View services on a location |
| `update_services` | Replace services on a location |
| `bulk_push_services` | Push same services to all locations |
| `update_profile` | Edit name, phone, website, or description |

---

## Setup (each team member)

### 1. Prerequisites

- Python 3.10+
- Node.js 18+
- Claude Code CLI: `npm install -g @anthropic-ai/claude-code`

### 2. Clone the repo

```bash
git clone <repo-url>
cd gbp-mcp-server
```

### 3. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add your credentials.json

- Go to [console.cloud.google.com](https://console.cloud.google.com)
- Open the shared project → APIs & Services → Credentials
- Download the OAuth 2.0 Client ID JSON
- Save it as `credentials.json` in the project root

> **Never commit credentials.json or token.json** — they are in .gitignore

### 6. Add the MCP server to Claude Code

Edit `~/.claude/settings.json` and add:

```json
{
  "mcpServers": {
    "gbp-audit": {
      "command": "python",
      "args": ["/absolute/path/to/gbp-mcp-server/server.py"]
    }
  }
}
```

Replace `/absolute/path/to/` with your actual path.

### 7. First-time authentication

Run the server once directly to trigger the browser login:

```bash
python server.py
```

A browser window will open — log in with the Google account that has access to your GBPs and grant permissions. A `token.json` file will be saved locally. You won't need to log in again unless the token expires.

---

## Example usage in Claude

```
> list all my GBP accounts

> list locations for accounts/123456789

> audit all locations for accounts/123456789

> get services for accounts/123/locations/456

> update services on accounts/123/locations/456 with:
  [{"freeFormServiceItem": {"category": {"displayName": "Plumbing"}, "label": {"displayName": "Drain Cleaning"}}}]

> push these services to all locations under accounts/123456789
```

---

## Project structure

```
gbp-mcp-server/
├── credentials.json    ← your OAuth file (not committed)
├── token.json          ← auto-generated after login (not committed)
├── gbp_client.py       ← Google API wrapper
├── server.py           ← MCP server
├── requirements.txt    ← Python dependencies
└── README.md
```

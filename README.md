# mcp

- Client: https://www.pulsemcp.com/clients
- Server: https://www.pulsemcp.com/servers


## Setup up project

### Create a new directory for our project
- curl -LsSf https://astral.sh/uv/install.sh | sh
- uv init mcp-server
- cd mcp-server

### Create virtual environment and activate it
- uv venv
- source .venv/bin/activate

### Install dependencies
- uv add "mcp[cli]" httpx
- uv add beautifulsoup4

### Running the Server
- uv run main.py
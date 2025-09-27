from fastmcp import FastMCP
import os

# ================================
# 👇 Create an instance of FastMCP
# ================================

mcp = FastMCP("SERVER MCP 🤖")

# Import tools and resources modules to register decorators
from .tools import tools
from .resources import resources
from .prompts import prompts

def run_server():
    """
    Function to run the FastMCP server.
    
    Environment variables:
    - MCP_TRANSPORT: 'stdio' (default) or 'sse'
    - MCP_PORT: Port for SSE (default: 8000)
    - MCP_HOST: Host for SSE (default: localhost)
    """
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    
    if transport == "sse":
        host = os.getenv("MCP_HOST", "localhost")
        port = int(os.getenv("MCP_PORT", "8000"))
        
        print(f"🚀 Starting MCP Server (SSE) on http://{host}:{port}/mcp")
        mcp.run(transport="sse", host=host, port=port)
    else:
        print("🚀 Starting MCP Server (STDIO)")
        mcp.run(transport="stdio")

if __name__ == "__main__":
    run_server()

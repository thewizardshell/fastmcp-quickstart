"""
Entry point for running the MCP server.
"""
from src.server import run_server
from dotenv import load_dotenv  # ← Agregar
load_dotenv()  

if __name__ == "__main__":
    run_server()

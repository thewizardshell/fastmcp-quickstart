"""
Resources module for FastMCP server.
Here you can define various resources that provide data to the LLM.
"""
from ..server import mcp

@mcp.resource("example://resource")
def example_resource() -> str:
    """
    Example resource - Replace this with your actual resources.
    
    Returns:
        Data from the resource
    """
    return "Example resource data"

# Add more resources here as needed

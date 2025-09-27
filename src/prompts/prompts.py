"""
Prompts module for FastMCP server.

Prompts are reusable instruction templates that tell the AI:
- WHAT to do
- HOW to do it  
- WHAT format to use

Add your @mcp.prompt() functions here.
"""
from ..server import mcp


@mcp.prompt()
def analyze_data(data_description: str) -> str:
    """
    Analyze data and provide insights.
    
    Args:
        data_description: Description of the data to analyze
    
    Returns:
        Formatted analysis prompt
    """
    return f"""
    Analyze this data: {data_description}
    
    Provide:
    1. Key insights
    2. Patterns or trends
    3. Recommendations
    
    Use markdown format.
    """


@mcp.prompt()
def review_code(code: str, language: str = "python") -> str:
    """
    Review code for bugs and improvements.
    
    Args:
        code: Code to review
        language: Programming language
    
    Returns:
        Code review prompt
    """
    return f"""
    Review this {language} code:
    
    ```{language}
    {code}
    ```
    
    Check:
    - Bugs
    - Performance
    - Best practices
    - Security issues
    """


@mcp.prompt()
def generate_docs(function_signature: str) -> str:
    """
    Generate documentation for code.
    
    Args:
        function_signature: Function to document
    
    Returns:
        Documentation generation prompt
    """
    return f"""
    Generate complete documentation for:
    
    {function_signature}
    
    Include:
    - Description
    - Parameters
    - Return value
    - Examples
    """


# ============================================
# ADD MORE PROMPTS HERE
# ============================================

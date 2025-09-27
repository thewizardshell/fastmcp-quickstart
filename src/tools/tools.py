"""
🛠️ TOOLS MODULE
Define your FastMCP tools here and use services for business logic.
"""
from ..server import mcp
from ..services  import example_service, calculator_service

# ============================================
# 📌 TOOLS USING SERVICES
# ============================================

@mcp.tool(name="process_text", description="Process text using example service")
def process_text(text: str) -> str:
    """
    Process text using the example service.
    
    Args:
        text: Text to process
        
    Returns:
        Processed text
    """
    # Call service method - business logic is separated
    result = example_service.process_data(text)
    return result


@mcp.tool(name="calculate", description="Perform calculations using calculator service")
def calculate(operation: str, a: float, b: float) -> float:
    """
    Perform calculations using calculator service.
    
    Args:
        operation: 'add' or 'multiply'
        a: First number
        b: Second number
        
    Returns:
        Calculation result
    """
    if operation == 'add':
        return calculator_service.add(a, b)
    elif operation == 'multiply':
        return calculator_service.multiply(a, b)
    else:
        raise ValueError(f"Unknown operation: {operation}")


# ============================================
# 📌 ADD MORE TOOLS HERE
# ============================================

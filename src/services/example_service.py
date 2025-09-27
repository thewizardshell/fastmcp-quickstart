"""
📦 SERVICES MODULE - TEMPLATE
=====================================================
Here you define your business logic separated from tools.

Benefits:
- Cleaner code organization
- Reusable logic across multiple tools
- Easier to test
- Better separation of concerns

HOW TO USE:
1. Create a service class with your logic
2. Import it in tools.py
3. Call the service methods from your @mcp.tool()
"""

from typing import Optional, Dict, Any


# ============================================
# 📌 EXAMPLE SERVICE CLASS
# ============================================

class ExampleService:
    """
    Template for a service class.
    
    Replace this with your actual business logic.
    """
    
    def __init__(self):
        """Initialize your service with any needed configuration"""
        self.config = {
            "api_key": "your-api-key",
            "base_url": "https://api.example.com"
        }
    
    def process_data(self, input_data: str) -> str:
        """
        Example method - Replace with your logic
        
        Args:
            input_data: Data to process
            
        Returns:
            Processed result
        """
        # Your business logic here
        result = f"Processed: {input_data}"
        return result
    
    def fetch_from_api(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Example API call method
        
        Args:
            endpoint: API endpoint to call
            params: Optional query parameters
            
        Returns:
            API response data
        """
        # In a real implementation:
        # import httpx
        # response = httpx.get(f"{self.config['base_url']}/{endpoint}", params=params)
        # return response.json()
        
        # Template placeholder:
        return {
            "status": "success",
            "endpoint": endpoint,
            "params": params
        }


# ============================================
# 📌 ADD MORE SERVICE CLASSES HERE
# ============================================

class CalculatorService:
    """Example: Calculator service"""
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers"""
        return a + b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers"""
        return a * b


class DatabaseService:
    """Example: Database service"""
    
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
    
    def query(self, sql: str) -> list:
        """
        Execute SQL query
        
        Args:
            sql: SQL query string
            
        Returns:
            Query results
        """
        # Your database logic here
        # import sqlite3
        # conn = sqlite3.connect(self.db_path)
        # cursor = conn.execute(sql)
        # results = cursor.fetchall()
        # conn.close()
        # return results
        
        return [{"example": "data"}]


# ============================================
# 📌 SINGLETON INSTANCES (Optional)
# ============================================

# Create global instances that can be imported
example_service = ExampleService()
calculator_service = CalculatorService()
database_service = DatabaseService()

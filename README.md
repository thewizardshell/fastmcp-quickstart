# QuickStart MCP

<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/d9f17209-7b24-4619-a2ce-a6f10d69450e" />


**Template para crear servidores MCP usando FastMCP de forma rápida y estructurada.**

## 📖 ¿Qué es MCP y FastMCP?

### Model Context Protocol (MCP)
MCP es un **protocolo estandarizado** que permite a las IAs (LLMs) conectarse con herramientas y datos externos. Se le conoce como **"el puerto USB-C para la IA"** porque proporciona una forma uniforme de conectar LLMs con recursos que pueden usar.

### FastMCP
FastMCP es un **framework de alto nivel en Python** que hace que construir servidores MCP sea simple e intuitivo. Maneja todos los detalles complejos del protocolo para que te concentres en construir funcionalidades.

---

## 🧩 Los 3 Componentes Principales de MCP

### 1. 🛠️ **TOOLS (Herramientas)**
**¿Qué son?** Funciones que la IA puede ejecutar para realizar acciones.

**Analogía:** Como endpoints **POST/PUT** en una API REST.

**Casos de uso:**
- Buscar en Google
- Consultar una base de datos
- Enviar un email
- Calcular algo
- Modificar archivos

**Ejemplo:**
```python
@mcp.tool()
def search_database(query: str) -> str:
    """Search for records in the database"""
    return f"Results for: {query}"
```

**¿Cómo lo usa la IA?**
```
Usuario: "Busca usuarios con email gmail.com"
IA: *Ejecuta tool search_database("gmail.com")*
IA: "Encontré 42 usuarios con email gmail.com"
```

---

### 2. 📚 **RESOURCES (Recursos)**
**¿Qué son?** Datos de solo lectura que la IA puede consultar.

**Analogía:** Como endpoints **GET** en una API REST.

**Casos de uso:**
- Archivos de configuración
- Documentación
- Datos estáticos
- Información de usuario
- Schemas de base de datos

**Ejemplo:**
```python
@mcp.resource("config://database")
def database_config() -> str:
    """Database configuration information"""
    return "host: localhost, port: 5432, db: myapp"
```

**¿Cómo lo usa la IA?**
```
Usuario: "¿Cuál es la configuración de la BD?"
IA: *Lee resource config://database*
IA: "La base de datos está en localhost:5432, nombre: myapp"
```

---

### 3. 💬 **PROMPTS (Plantillas de Instrucciones)**
**¿Qué son?** Plantillas reutilizables que le dicen a la IA **cómo hacer algo**.

**Analogía:** Como **recetas de cocina** que indican paso a paso qué hacer.

**Casos de uso:**
- Análisis de datos estructurados
- Revisión de código
- Generación de documentación
- Debugging asistido
- Workflows complejos

**Ejemplo:**
```python
@mcp.prompt()
def analyze_data(dataset: str) -> str:
    """Analyze dataset and provide insights"""
    return f"""
    Analyze this dataset: {dataset}
    
    Steps:
    1. Use tool 'query_database' to get data
    2. Calculate statistics
    3. Identify patterns
    4. Generate recommendations
    
    Format: Markdown with charts
    """
```

**¿Cómo lo usa la IA?**
```
Usuario: "Analiza las ventas de enero"
IA: *Carga prompt analyze_data("ventas_enero")*
IA: *Sigue las instrucciones del prompt automáticamente*
IA: *Usa los tools necesarios*
IA: "Análisis completo de ventas de enero: [reporte estructurado]"
```

---

## 🔄 Comparación Visual

| Componente | Analogía | Función | Ejemplo |
|------------|----------|---------|---------|
| **TOOL** 🛠️ | Acción/Verbo | Ejecuta algo | `calculate()`, `send_email()` |
| **RESOURCE** 📚 | Sustantivo/Dato | Provee info | `user_profile`, `config` |
| **PROMPT** 💬 | Receta/Plan | Orquesta | "Analiza X usando Y y Z" |

---

## ❓ Preguntas Frecuentes

### ¿Puedo conectar un Prompt con un Tool?
**¡SÍ!** De hecho, esa es la forma más poderosa de usar MCP.

**Ejemplo:**
```python
# Tool que hace algo
@mcp.tool()
def fetch_sales_data(month: str) -> dict:
    """Get sales data for a specific month"""
    return {"total": 50000, "items": 120}

# Prompt que usa el tool
@mcp.prompt()
def sales_report(month: str) -> str:
    """Generate complete sales report"""
    return f"""
    Generate sales report for {month}:
    
    1. Use tool 'fetch_sales_data' with month='{month}'
    2. Calculate growth vs previous month
    3. Identify top products
    4. Create executive summary
    
    Format: Professional report in markdown
    """
```

**Flujo:**
```
Usuario: "Genera reporte de ventas de marzo"
↓
IA carga prompt 'sales_report'
↓
Prompt le dice a la IA: "Usa tool fetch_sales_data"
↓
IA ejecuta fetch_sales_data('marzo')
↓
IA procesa los datos según instrucciones del prompt
↓
IA genera el reporte final
```

### ¿Puedo usar Resources dentro de Prompts?
**¡SÍ!** Los prompts pueden indicar qué resources leer.

**Ejemplo:**
```python
@mcp.resource("data://schema")
def database_schema():
    return "users(id, name, email), orders(id, user_id, total)"

@mcp.prompt()
def query_assistant(question: str) -> str:
    return f"""
    Question: {question}
    
    1. Read resource 'data://schema' to understand DB structure
    2. Generate SQL query based on schema
    3. Use tool 'execute_query' to run it
    4. Format results as table
    """
```

### ¿Cuándo usar cada componente?

**Usa TOOLS cuando:**
- ✅ Necesitas ejecutar una acción
- ✅ Vas a modificar algo
- ✅ Llamarás APIs externas
- ✅ Harás cálculos o transformaciones

**Usa RESOURCES cuando:**
- ✅ Tienes datos estáticos
- ✅ Configs o documentación
- ✅ Información de solo lectura
- ✅ Contexto que la IA necesita conocer

**Usa PROMPTS cuando:**
- ✅ Necesitas workflows complejos
- ✅ Quieres combinar tools y resources
- ✅ Requieres respuestas estructuradas
- ✅ Tienes patrones repetitivos

---

## 📁 Estructura del Proyecto

```
template-mcp-py/
├── .env                    # Configuración (transport, port, etc.)
├── run.py                  # Punto de entrada
│
└── src/
    ├── server.py          # Servidor MCP principal
    │
    ├── tools/             # Herramientas (@mcp.tool)
    │   ├── __init__.py
    │   └── tools.py
    │
    ├── resources/         # Recursos (@mcp.resource)
    │   ├── __init__.py
    │   └── resources.py
    │
    ├── services/          # Lógica de negocio
    │   ├── __init__.py
    │   └── example_service.py
    │
    └── prompts/           # Plantillas (@mcp.prompt)
        ├── __init__.py
        └── prompts.py
```

---

## 🚀 Instalación

### Opción 1: Con pip
```bash
# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install fastmcp pydantic python-dotenv
```

### Opción 2: Con uv (Recomendado - Más rápido)
```bash
# Instalar uv
curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux/Mac
# O en Windows: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Instalar dependencias
uv add fastmcp pydantic python-dotenv
```

---

## 💻 Uso

### 1. Modo STDIO (Para Claude Desktop, Cursor)
```bash
python run.py
```

### 2. Modo SSE (Servidor HTTP)
```bash
# Opción A: Variable de entorno
MCP_TRANSPORT=sse python run.py

# Opción B: Editar .env
# .env
MCP_TRANSPORT=sse
MCP_PORT=8000

python run.py
```

El servidor estará en: `http://localhost:8000/mcp`

---

## 🛠️ Crear Nuevas Funcionalidades

### Agregar un Tool
```python
# En src/tools/tools.py

@mcp.tool()
def calculate_tax(amount: float, rate: float = 0.16) -> float:
    """Calculate tax for a given amount"""
    return amount * rate
```

### Agregar un Resource
```python
# En src/resources/resources.py

@mcp.resource("pricing://plans")
def pricing_plans() -> str:
    """Available pricing plans"""
    return "Basic: $10, Pro: $50, Enterprise: Custom"
```

### Agregar un Prompt
```python
# En src/prompts/prompts.py

@mcp.prompt()
def tax_calculator(amount: float) -> str:
    """Calculate and explain tax"""
    return f"""
    Calculate tax for amount: ${amount}
    
    1. Use tool 'calculate_tax' with amount={amount}
    2. Explain the calculation
    3. Show breakdown
    
    Format: Clear explanation with numbers
    """
```

---

## 🔗 Conectar con Claude Desktop

Editar: `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac)

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["/ruta/completa/al/proyecto/run.py"]
    }
  }
}
```

Para SSE:
```json
{
  "mcpServers": {
    "my-server": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

---

## 💡 Ejemplo Completo: Workflow Integrado

```python
# RESOURCE: Datos disponibles
@mcp.resource("data://users")
def user_data():
    return "100 users in database"

# TOOL: Acción específica
@mcp.tool()
def query_users(filter: str) -> list:
    """Query users from database"""
    return [{"id": 1, "name": "John"}]

# PROMPT: Orquesta todo
@mcp.prompt()
def user_analysis() -> str:
    """Analyze user database"""
    return """
    Analyze users:
    
    1. Read resource 'data://users' for context
    2. Use tool 'query_users' to get data
    3. Calculate statistics
    4. Generate insights
    5. Create summary report
    
    Format: Executive summary with metrics
    """
```

**Usuario:** "Analiza la base de usuarios"
**IA:** *Ejecuta el workflow completo automáticamente*

---

## 📚 Recursos Adicionales

- **Documentación FastMCP:** https://gofastmcp.com
- **Model Context Protocol:** https://modelcontextprotocol.io
- **Ejemplos en GitHub:** https://github.com/jlowin/fastmcp

---

## 🎯 Próximos Pasos

1. **Explora** los archivos de ejemplo en `src/`
2. **Modifica** tools, resources y prompts según tus necesidades
3. **Conecta** con Claude Desktop o tu cliente MCP favorito
4. **Construye** workflows poderosos combinando los 3 componentes

---

## ❓ Soporte

¿Dudas? Revisa:
- Archivos de ejemplo en cada carpeta
- Documentación oficial de FastMCP
- Issues en el repositorio de FastMCP

---

**¡Happy coding!** 🚀

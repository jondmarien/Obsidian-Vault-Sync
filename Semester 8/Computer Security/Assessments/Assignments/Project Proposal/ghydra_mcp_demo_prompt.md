# GhydraMCP Demo: Advanced Binary Analysis with AI

## Overview

This demo showcases GhydraMCP, a Multi-headed MCP Server for Ghidra that enables AI models to interact with Ghidra for advanced binary analysis. This demonstration will walk through setting up multiple Ghidra instances, analyzing different components of a malware sample, and leveraging AI to assist in reverse engineering tasks.

## Setup Instructions

### Prerequisites

- Ghidra (version 10.3 or newer) installed
- Python 3.8+ with pip
- GhydraMCP plugin installed in Ghidra
- Sample binaries for analysis (provided in the `samples/` folder)

### Environment Configuration

1. Start by installing the required Python packages:

```bash
pip install mcp-sdk ghydra-client
```

2. Configure the MCP server in Claude Desktop (or your AI assistant environment):

```json
{
  "mcpServers": {
    "ghydra": {
      "command": "uv",
      "args": [
        "run",
        "/path/to/bridge_mcp_hydra.py"
      ],
      "env": {
        "GHIDRA_HYDRA_HOST": "localhost"
      }
    }
  }
}
```

3. Launch two Ghidra instances with the sample binaries:
   - Instance 1 (port 8192): Main malware executable
   - Instance 2 (port 8193): Associated DLL file

## Demo Scenario: Analyzing a Multi-Component Malware

In this scenario, we're analyzing a sophisticated malware that consists of a main executable and a supporting DLL. Our goal is to understand its functionality, identify potential vulnerabilities, and document our findings.

## Demo Steps

### 1. Discovering and Registering Ghidra Instances

Start by discovering active Ghidra instances and registering them with GhydraMCP:

```python
# Ask AI to discover and register Ghidra instances
```

Expected AI Response:
```python
# Discovering active Ghidra instances
client.use_tool("ghydra", "discover_instances")

# Alternatively, manually register known instances
client.use_tool("ghydra", "register_instance", {"port": 8192, "url": "http://localhost:8192/"})
client.use_tool("ghydra", "register_instance", {"port": 8193, "url": "http://localhost:8193/"})

# Listing registered instances
client.use_tool("ghydra", "list_instances")
```

### 2. Analyzing the Main Executable (Instance 1)

Now, let's analyze the main executable in the first Ghidra instance:

```python
# Ask AI to identify the main function and decompile it
```

Expected AI Response:
```python
# Specify which instance to use
instance_params = {"port": 8192}

# Get program information
client.use_tool("ghydra", "get_program_info", instance_params)

# Find and decompile the main function
client.use_tool("ghydra", "decompile_function", {**instance_params, "name": "main"})

# Get function call graph
client.use_tool("ghydra", "get_callgraph", {**instance_params, "address": "0x00401000"})
```

### 3. Searching for Suspicious Strings

Let's search for potentially malicious strings in the binary:

```python
# Ask AI to find suspicious strings related to network activity, encryption, or system manipulation
```

Expected AI Response:
```python
# List all strings with pagination
client.use_tool("ghydra", "list_strings", {**instance_params, "limit": 100, "offset": 0})

# Search for specific suspicious patterns
client.use_tool("ghydra", "list_strings", {**instance_params, "filter": "http"})
client.use_tool("ghydra", "list_strings", {**instance_params, "filter": "encrypt"})
client.use_tool("ghydra", "list_strings", {**instance_params, "filter": "registry"})
```

### 4. Examining the Supporting DLL (Instance 2)

Now, let's switch to the second Ghidra instance to analyze the DLL:

```python
# Ask AI to analyze the exports in the DLL and identify potential malicious functions
```

Expected AI Response:
```python
# Switch to the second instance
instance_params = {"port": 8193}

# Get DLL information
client.use_tool("ghydra", "get_program_info", instance_params)

# List exported functions
client.use_tool("ghydra", "list_functions", {**instance_params, "type": "exported"})

# Analyze a suspicious exported function
client.use_tool("ghydra", "decompile_function", {**instance_params, "name": "InitializeConnection"})
```

### 5. Cross-Reference Analysis Between Components

Let's identify how the main executable and DLL interact:

```python
# Ask AI to find references between the main executable and the DLL
```

Expected AI Response:
```python
# In the main executable (first instance)
instance_params = {"port": 8192}

# Find references to the DLL name
client.use_tool("ghydra", "list_strings", {**instance_params, "filter": "malware_helper.dll"})

# Analyze the function that loads the DLL
client.use_tool("ghydra", "decompile_function", {**instance_params, "name": "LoadLibraryHandler"})

# Look for cross-references to a specific address
client.use_tool("ghydra", "get_xrefs", {**instance_params, "address": "0x00402500"})
```

### 6. Data Structure Analysis

Now, identify and analyze key data structures:

```python
# Ask AI to identify and document important data structures in the malware
```

Expected AI Response:
```python
# Examine a potential configuration structure
client.use_tool("ghydra", "get_data", {**instance_params, "address": "0x00404000"})

# Set a proper data type for better analysis
client.use_tool("ghydra", "set_data_type", {**instance_params, "address": "0x00404000", "data_type": "ConfigStruct"})

# Add meaningful names to data fields
client.use_tool("ghydra", "rename_data", {**instance_params, "address": "0x00404008", "name": "encryption_key"})
```

### 7. Adding Analysis Comments and Documentation

Finally, document our findings with meaningful comments:

```python
# Ask AI to add comments to key functions and data structures
```

Expected AI Response:
```python
# Add a function comment
client.use_tool("ghydra", "set_comment", {
    **instance_params,
    "address": "0x00401000",
    "comment": "Main entry point - initializes components and starts the connection thread",
    "comment_type": "plate"
})

# Add a comment to a suspicious instruction
client.use_tool("ghydra", "set_comment", {
    **instance_params,
    "address": "0x00401234",
    "comment": "Obfuscated API call to download additional payload",
    "comment_type": "pre"
})

# Document a data structure
client.use_tool("ghydra", "set_comment", {
    **instance_params,
    "address": "0x00404000",
    "comment": "Configuration structure containing C2 server addresses and encryption parameters",
    "comment_type": "plate"
})
```

## Extending the Demo

For a more comprehensive demonstration, consider these additional scenarios:

1. **Automating Analysis**: Show how to script repetitive analysis tasks
2. **Multiple File Analysis**: Analyze related files in different Ghidra instances simultaneously
3. **Custom Data Types**: Create and apply custom data structures to improve analysis
4. **Collaborative Analysis**: Demonstrate how multiple analysts can work on different components

## Conclusion

This demo illustrates how GhydraMCP enables AI assistants to interact with Ghidra for advanced binary analysis. By connecting multiple Ghidra instances and providing a comprehensive API, GhydraMCP enhances reverse engineering workflows and enables more efficient analysis of complex software.


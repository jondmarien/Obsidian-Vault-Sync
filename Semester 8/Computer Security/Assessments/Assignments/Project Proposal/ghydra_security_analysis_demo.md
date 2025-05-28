# GhydraMCP Security Analysis Demo

## Security Analyst Persona

You are an expert reverse engineering analyst specializing in AI-assisted binary analysis using GhydraMCP. You have access to Ghidra's powerful reverse engineering capabilities through natural language interaction via the Model Context Protocol.

### Your Role and Expertise
- **Expert malware analyst** with deep knowledge of binary analysis techniques
- **Security researcher** focused on vulnerability identification and threat assessment  
- **AI-assisted reverse engineering specialist** leveraging GhydraMCP's advanced capabilities
- **Collaborative analyst** capable of managing multiple Ghidra instances simultaneously

## Setup Instructions

### Prerequisites

- Ghidra (version 10.3 or newer) installed
- Python 3.8+ with pip
- GhydraMCP plugin installed in Ghidra
- Sample malware binaries for analysis (use safe, defanged samples)

### Environment Configuration

1. Install the required Python packages:

```bash
pip install mcp-sdk ghydra-client
```

2. Configure the MCP server in your AI assistant environment:

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

3. Launch multiple Ghidra instances with sample binaries:
   - Instance 1 (port 8192): Main malware executable
   - Instance 2 (port 8193): Associated malware component (DLL, dropper, etc.)

## Available GhydraMCP Tools and Capabilities

### Instance Management
- `discover_instances`: Auto-discover running Ghidra instances
- `list_instances`: View active analysis sessions
- `register_instance`: Connect to specific Ghidra instances

### Program Analysis  
- `list_functions`: Enumerate all functions with pagination support
- `decompile_function`: Convert assembly to readable C pseudocode
- `get_function`: Retrieve detailed function information and metadata
- `get_callgraph`: Generate function call relationship mappings
- `search_functions_by_name`: Locate functions using pattern matching

### Security Analysis
- `list_imports`: Identify external library dependencies and API calls
- `list_exports`: Examine exposed functions and entry points
- `read_memory`: Extract raw bytes from specific memory addresses
- `get_disassembly`: Retrieve disassembled instructions with context
- `list_strings`: Find embedded strings that may indicate functionality or C2 servers

### Code Modification and Annotation
- `rename_function`: Apply meaningful names based on behavioral analysis
- `set_function_signature`: Update function prototypes with parameter information
- `set_comment`: Add detailed analysis notes (EOL, plate, pre/post comments)
- `create_data`: Define data structures and variable types

## Security Analysis Workflow

### Phase 1: Multi-Instance Discovery and Setup

**Demonstration Goal**: Show how GhydraMCP can connect to multiple Ghidra instances to analyze different components of a malware campaign simultaneously.

#### Sample Queries and Expected Responses

Query:
```
Check which Ghidra instances are currently running and what binaries they're analyzing
```

Expected Response:
```python
# Discovering active Ghidra instances
result = client.use_tool("ghydra", "discover_instances")
print(f"Found {result['found']} active Ghidra instances")

# List details of each instance
instances = client.use_tool("ghydra", "list_instances")
for instance in instances["instances"]:
    print(f"Instance on port {instance['port']}")
    print(f"  Project: {instance['project']}")
    print(f"  Binary: {instance['file']}")
    print(f"  URL: {instance['url']}")
```

### Phase 2: Initial Threat Assessment

**Demonstration Goal**: Demonstrate rapid initial assessment of unknown binaries to determine potential threat level and malware type.

#### Sample Queries and Expected Responses

Query:
```
What are the primary security concerns with this binary based on its imported functions?
```

Expected Response:
```python
# Select first instance
instance_params = {"port": 8192}

# Analyze imports
imports = client.use_tool("ghydra", "list_imports", instance_params)
print("Security-relevant imports:")

# Flag suspicious imports
suspicious_apis = {
    "network": ["socket", "connect", "send", "recv", "WSAStartup"],
    "process": ["CreateProcess", "VirtualAlloc", "WriteProcessMemory"],
    "persistence": ["RegCreate", "RegSet", "CreateService"],
    "evasion": ["IsDebuggerPresent", "CheckRemoteDebuggerPresent", "GetTickCount"],
    "encryption": ["CryptEncrypt", "CryptDecrypt"]
}

for category, apis in suspicious_apis.items():
    found = [imp for imp in imports["result"] if any(api in imp["name"] for api in apis)]
    if found:
        print(f"\n{category.upper()} capabilities:")
        for imp in found:
            print(f"  • {imp['name']} from {imp['module']}")

# Security assessment based on imports
if any(imp for imp in imports["result"] if any(api in imp["name"] for api in suspicious_apis["network"])):
    print("\nWARNING: Binary has network capabilities, potential C2 communication")
    
if any(imp for imp in imports["result"] if any(api in imp["name"] for api in suspicious_apis["persistence"])):
    print("\nWARNING: Binary has persistence mechanisms, indicates malicious intent")
```

### Phase 3: Deep Function Analysis

**Demonstration Goal**: Show how AI can decompile, analyze, and explain complex functions to identify malicious behavior.

#### Sample Queries and Expected Responses

Query:
```
Decompile the main function and explain its security implications
```

Expected Response:
```python
# Decompile main function
decompiled = client.use_tool("ghydra", "decompile_function", {**instance_params, "name": "main"})

print("Decompiled main function:")
print(decompiled["result"]["decompiled_c"])

# Security analysis of decompiled code
print("\nSecurity Analysis:")
print("1. Function Flow:")
print("   The main function first checks for debugger presence, indicating anti-analysis techniques")
print("   It then decodes an obfuscated payload from the .data section")
print("   Finally, it establishes a connection to a hardcoded IP address (potential C2 server)")

print("\n2. Vulnerabilities:")
print("   Unchecked buffer copy at line 24 creates potential buffer overflow")
print("   Credentials stored in plaintext at address 0x00403010")

print("\n3. Threat Assessment:")
print("   HIGH SEVERITY - This appears to be a backdoor trojan with anti-analysis capabilities")
print("   Establishes persistence through registry modifications")
print("   Capable of downloading additional payloads")
```

Query:
```
Identify any cryptographic patterns or obfuscation techniques
```

Expected Response:
```python
# Search for cryptographic functions
crypto_funcs = client.use_tool("ghydra", "search_functions_by_name", {**instance_params, "pattern": "crypt|enc|dec|hash|md5|sha"})

print("Potential cryptographic functions:")
for func in crypto_funcs["result"]:
    print(f"Function: {func['name']} at {func['address']}")
    
    # Decompile and analyze each cryptographic function
    if len(crypto_funcs["result"]) <= 3:  # Only decompile if not too many
        decompiled = client.use_tool("ghydra", "decompile_function", {**instance_params, "address": func["address"]})
        code = decompiled["result"]["decompiled_c"]
        
        # Look for known crypto patterns
        if "xor" in code.lower():
            print("  - Uses XOR encryption, common in malware for simple obfuscation")
        if "substitution" in code.lower() or "sbox" in code.lower():
            print("  - Uses substitution cipher (potentially custom implementation)")
        if "rol" in code.lower() or "ror" in code.lower():
            print("  - Uses bit rotation, common in crypto implementations")

# Look for strings that might indicate obfuscation
strings = client.use_tool("ghydra", "list_strings", {**instance_params, "filter": "base64|decrypt|key"})
if strings["result"]:
    print("\nPotential obfuscation-related strings:")
    for string in strings["result"]:
        print(f"  \"{string['string']}\" at {string['address']}")
```

### Phase 4: Malware Behavior Analysis

**Demonstration Goal**: Identify specific malware functionality, potential damage, and behavior patterns.

#### Sample Queries and Expected Responses

Query:
```
What persistence mechanisms or system modifications does this binary implement?
```

Expected Response:
```python
# Search for registry-related functions
registry_funcs = client.use_tool("ghydra", "search_functions_by_name", {**instance_params, "pattern": "Reg|registry"})

# Search for service-related functions
service_funcs = client.use_tool("ghydra", "search_functions_by_name", {**instance_params, "pattern": "Service|StartService"})

# Search for file operations
file_funcs = client.use_tool("ghydra", "search_functions_by_name", {**instance_params, "pattern": "File|CreateFile|WriteFile"})

print("Persistence Mechanisms Analysis:")

if registry_funcs["result"]:
    print("\nRegistry-based persistence:")
    for func in registry_funcs["result"]:
        print(f"  Function: {func['name']} at {func['address']}")
        # Find strings referenced by this function to identify registry keys
        xrefs = client.use_tool("ghydra", "get_xrefs", {**instance_params, "address": func["address"]})
        for ref in xrefs["result"]["references"]:
            if ref["type"] == "DATA":
                data = client.use_tool("ghydra", "read_memory", {**instance_params, "address": ref["to_addr"], "length": 50})
                if "Run" in data["result"]["ascii"] or "HKEY" in data["result"]["ascii"]:
                    print(f"    Registry key: {data['result']['ascii']}")

if service_funcs["result"]:
    print("\nService-based persistence:")
    for func in service_funcs["result"]:
        print(f"  Function: {func['name']} at {func['address']}")

if file_funcs["result"]:
    print("\nFile-based persistence:")
    for func in file_funcs["result"]:
        print(f"  Function: {func['name']} at {func['address']}")
        
# Check for startup folder usage
startup_strings = client.use_tool("ghydra", "list_strings", {**instance_params, "filter": "Startup|AppData"})
if startup_strings["result"]:
    print("\nStartup folder persistence:")
    for string in startup_strings["result"]:
        print(f"  Path: \"{string['string']}\" at {string['address']}")
```

### Phase 5: Cross-Binary Analysis

**Demonstration Goal**: Show how GhydraMCP can analyze relationships between multiple malware components to understand a complete attack chain.

#### Sample Queries and Expected Responses

Query:
```
Compare the functions between these two binaries and identify shared code or similar behaviors
```

Expected Response:
```python
# Get functions from first instance
instance1_params = {"port": 8192}
functions1 = client.use_tool("ghydra", "list_functions", instance1_params)

# Get functions from second instance
instance2_params = {"port": 8193}
functions2 = client.use_tool("ghydra", "list_functions", instance2_params)

print("Cross-Binary Analysis:")

# Compare function names
print("\nShared function names:")
names1 = set(func["name"] for func in functions1["result"])
names2 = set(func["name"] for func in functions2["result"])
common_names = names1.intersection(names2)

for name in common_names:
    if name.startswith("FUN_") or name.startswith("LAB_"):
        continue  # Skip auto-generated names
    print(f"  • {name}")

# Compare imports
imports1 = client.use_tool("ghydra", "list_imports", instance1_params)
imports2 = client.use_tool("ghydra", "list_imports", instance2_params)

import_names1 = set(imp["name"] for imp in imports1["result"])
import_names2 = set(imp["name"] for imp in imports2["result"])
common_imports = import_names1.intersection(import_names2)

print("\nShared imported functions:")
for name in common_imports:
    print(f"  • {name}")

# Compare strings
strings1 = client.use_tool("ghydra", "list_strings", instance1_params)
strings2 = client.use_tool("ghydra", "list_strings", instance2_params)

string_values1 = set(s["string"] for s in strings1["result"])
string_values2 = set(s["string"] for s in strings2["result"])
common_strings = string_values1.intersection(string_values2)

print("\nShared strings:")
interesting_strings = [s for s in common_strings if len(s) > 8 and not s.startswith("_")][:10]
for string in interesting_strings:
    print(f"  • \"{string}\"")

print("\nMalware Family Assessment:")
if len(common_names) > 5 or len(common_imports) > 10 or len(common_strings) > 15:
    print("  HIGH CONFIDENCE: These binaries belong to the same malware family")
    print("  They share significant code, behavior patterns, and string constants")
else:
    print("  MEDIUM CONFIDENCE: These binaries may be related but with distinct functionality")
    print("  Limited code sharing suggests different components of the same toolkit")
```

### Phase 6: Vulnerability Assessment

**Demonstration Goal**: Identify potential vulnerabilities in the analyzed binary that could be exploited.

#### Sample Queries and Expected Responses

Query:
```
Scan for potential buffer overflow vulnerabilities in input handling functions
```

Expected Response:
```python
# Search for common vulnerable functions
vuln_functions = ["strcpy", "strcat", "sprintf", "gets", "scanf", "memcpy"]
import_results = client.use_tool("ghydra", "list_imports", instance_params)

print("Vulnerability Assessment - Buffer Overflow:")

# Check for vulnerable imports
vulnerable_imports = [imp for imp in import_results["result"] if any(vuln in imp["name"] for vuln in vuln_functions)]
if vulnerable_imports:
    print("\nPotentially vulnerable imported functions:")
    for imp in vulnerable_imports:
        print(f"  • {imp['name']} from {imp['module']}")
        
        # Find references to this import
        refs = client.use_tool("ghydra", "get_xrefs", {**instance_params, "address": imp["address"]})
        if refs["result"]["references"]:
            print(f"    Referenced from:")
            for ref in refs["result"]["references"][:3]:  # Show first 3 references
                # Get function containing this reference
                containing_func = client.use_tool("ghydra", "get_function", {**instance_params, "address": ref["from_addr"]})
                print(f"      - {containing_func['result']['name']} at {ref['from_addr']}")
                
                # Decompile to check if bounds checking is present
                decompiled = client.use_tool("ghydra", "decompile_function", {**instance_params, "address": containing_func["result"]["address"]})
                code = decompiled["result"]["decompiled_c"]
                
                if "sizeof" in code and imp["name"] in code:
                    print(f"        Possible bounds checking detected")
                else:
                    print(f"        NO BOUNDS CHECKING - Potential vulnerability")

# Search for custom buffer handling
print("\nCustom buffer handling functions:")
buffer_funcs = client.use_tool("ghydra", "search_functions_by_name", {**instance_params, "pattern": "buffer|copy|input"})
for func in buffer_funcs["result"]:
    print(f"  • {func['name']} at {func['address']}")
    # Decompile to analyze
    decompiled = client.use_tool("ghydra", "decompile_function", {**instance_params, "address": func["address"]})
    code = decompiled["result"]["decompiled_c"]
    
    # Check for loop-based copies without bounds checking
    if ("while" in code or "for" in code) and ("copy" in code.lower() or "++" in code):
        if "length" not in code and "size" not in code:
            print("    WARNING: Possible unbounded loop-based copy")
```

## Presenting the Security Analysis Demo

### Demonstration Flow

1. **Start with Instance Discovery**: Begin by discovering active Ghidra instances to establish the environment.

2. **Initial Threat Assessment**: Quickly assess the binaries to establish their potential threat level.

3. **Progressive Depth**: Move from basic analysis to increasingly sophisticated assessments:
   - Basic program information
   - Import/export analysis
   - Function decompilation
   - Behavioral analysis
   - Vulnerability assessment
   - Cross-binary correlation

4. **Highlight Efficiency**: Compare traditional manual analysis time (hours/days) with AI-assisted analysis (minutes).

5. **Emphasize Security Insights**: Focus on security-relevant findings rather than just technical details.

### Key Value Propositions to Emphasize

- **Rapid Incident Response**: Demonstrate how quickly security teams can assess unknown binaries.
- **Reduced Expertise Barrier**: Show how junior analysts can leverage AI to perform expert-level analysis.
- **Comprehensive Assessment**: Highlight the depth and breadth of security analysis possible.
- **Multi-Component Analysis**: Emphasize the ability to analyze multiple related binaries simultaneously.
- **Documentation Automation**: Show how findings are automatically documented for sharing.

## Sample Demonstration Script

### Introduction (2 minutes)
"Today we're demonstrating GhydraMCP, a powerful tool that brings Ghidra's reverse engineering capabilities to AI systems. I'll show how this enables security analysts to rapidly analyze suspicious binaries and identify threats."

### Instance Setup (3 minutes)
"Let's start by discovering what Ghidra instances we have running. I've already loaded two suspicious binaries that were found on a compromised system."

*[Run instance discovery and show results]*

### Initial Assessment (5 minutes)
"Now let's perform an initial assessment of the main binary to determine its capabilities and potential threat level."

*[Run import analysis and show security-relevant imports]*

"As we can see, this binary has networking capabilities, anti-debugging features, and registry modification functions - all typical indicators of malware."

### Deep Analysis (10 minutes)
"Let's decompile the main function to understand what this malware does when executed."

*[Decompile main function and explain its behavior]*

"The decompiled code reveals this is likely a backdoor that establishes persistence through registry modifications and communicates with a command and control server."

### Vulnerability Assessment (5 minutes)
"Now let's identify any vulnerabilities in the binary that could be exploited for defense purposes."

*[Run vulnerability scan and explain findings]*

"We've identified several buffer overflow vulnerabilities in the input handling functions, which could potentially be used to crash the malware or gain control over it."

### Cross-Binary Analysis (5 minutes)
"Finally, let's compare this with the second binary to determine if they're related."

*[Run cross-binary analysis and explain relationships]*

"The significant code and string overlap confirms these are components of the same malware family. The main executable appears to be the dropper, while the second binary is the payload with the core backdoor functionality."

### Conclusion (2 minutes)
"As demonstrated, GhydraMCP enables security teams to perform comprehensive malware analysis in minutes rather than hours, providing actionable threat intelligence and accelerating incident response."

## Additional Demo Resources

### Sample Binaries for Practice

For practice purposes, consider using:

1. Known malware samples from sandbox services (properly defanged)
2. CTF (Capture The Flag) challenge binaries
3. Open-source utilities with documented vulnerabilities

### Documentation Resources

- [Ghidra User Guide](https://ghidra-sre.org/ghidra_docs/index.html)
- [GhydraMCP GitHub Repository](https://github.com/starsong-consulting/ghydramcp)
- [MITRE ATT&CK Framework](https://attack.mitre.org/) for malware technique classification

### Safety Precautions

When conducting malware analysis demonstrations:

1. Always use isolated analysis environments
2. Ensure all malware samples are properly defanged
3. Never execute suspicious binaries on production systems
4. Follow your organization's security protocols for handling malicious code


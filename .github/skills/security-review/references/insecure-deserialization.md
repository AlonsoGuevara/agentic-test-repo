# Insecure Deserialization

**Severity**: Critical

## Description
Insecure deserialization occurs when an application deserializes untrusted data without proper validation, allowing an attacker to manipulate serialized objects to achieve remote code execution, privilege escalation, or application logic bypass. Many serialization formats (pickle, Java serialization, YAML with unsafe loaders, PHP unserialize) can instantiate arbitrary objects and invoke methods during deserialization, making this especially dangerous.

## Detection
- Use of unsafe deserialization functions on untrusted input: `pickle.loads()`, `pickle.load()`, `yaml.load()` without `SafeLoader`, `marshal.loads()`, `shelve.open()`
- Java's `ObjectInputStream.readObject()` on untrusted data
- PHP `unserialize()` on user input
- `eval()` used to parse data formats (JSON, configuration, etc.)
- Custom deserialization that instantiates classes based on untrusted type information
- Keywords to look for: `pickle`, `unpickle`, `deserialize`, `yaml.load`, `marshal`, `shelve`, `readObject`, `unserialize`, `eval`, `exec`

## Remediation
Avoid deserializing untrusted data. Use safe serialization formats (JSON, Protocol Buffers). If deserialization is required, use safe loaders and validate data before processing.

**Before:**
```
function loadUserData(serializedData):
    data = pickle.loads(serializedData)
    return data

function loadConfig(yamlString):
    config = yaml.load(yamlString)
    return config
```

**After:**
```
function loadUserData(jsonString):
    # Use a safe format like JSON instead of pickle
    data = json.parse(jsonString)
    validate(data, expectedSchema)
    return data

function loadConfig(yamlString):
    # Use SafeLoader to prevent arbitrary object instantiation
    config = yaml.load(yamlString, Loader=SafeLoader)
    return config
```

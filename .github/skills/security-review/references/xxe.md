# XML External Entity (XXE) Injection

**Severity**: High

## Description
XML External Entity injection occurs when an XML parser processes external entity references in untrusted XML input. An attacker can craft XML documents that reference external resources — such as local files, internal network services, or remote URLs — causing the parser to fetch or include their contents. XXE can lead to local file disclosure, server-side request forgery, denial of service (via recursive entity expansion, the "billion laughs" attack), and in some cases remote code execution.

## Detection
- XML parsing of untrusted input without disabling external entity processing
- XML parsers with default configurations (many enable external entities by default)
- Use of `DOCTYPE` declarations in user-supplied XML that define `ENTITY` references
- XML parsing libraries without explicit security hardening: `xml.etree.ElementTree`, `lxml.etree.parse`, `javax.xml.parsers`, `DOMParser`, `SAXParser`
- SOAP endpoints that accept raw XML
- File upload functionality that accepts XML, SVG, or DOCX files (which are ZIP-wrapped XML)
- Keywords to look for: `xml.parse`, `etree.parse`, `SAXParser`, `DocumentBuilder`, `XMLReader`, `DOCTYPE`, `ENTITY`, `SYSTEM`

## Remediation
Disable external entity processing and DTD processing in XML parsers. Use less complex data formats (JSON) when possible. If XML is required, configure parsers securely.

**Before:**
```
function parseXml(xmlString):
    parser = createXmlParser()
    document = parser.parse(xmlString)  # Default config allows XXE
    return document

# Attacker sends:
# <?xml version="1.0"?>
# <!DOCTYPE foo [
#   <!ENTITY xxe SYSTEM "file:///etc/passwd">
# ]>
# <data>&xxe;</data>
```

**After:**
```
function parseXml(xmlString):
    parser = createXmlParser()
    parser.setFeature("disallow-doctype-decl", true)
    parser.setFeature("external-general-entities", false)
    parser.setFeature("external-parameter-entities", false)
    parser.setFeature("load-external-dtd", false)
    document = parser.parse(xmlString)
    return document

# Or prefer JSON for APIs:
function parseInput(inputString):
    return json.parse(inputString)
```

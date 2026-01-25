# Python + Cybersecurity Learning Curriculum
## Dustin Lidster - 2026

---

## CURRICULUM OVERVIEW

This curriculum combines Python programming fundamentals with practical cybersecurity applications. Each unit teaches core programming concepts through the lens of building real security tools.

**Total Duration:** 16-20 weeks (self-paced)

**Learning Philosophy:**
- Learn by doing, not just reading
- Build real tools for your GitHub portfolio
- Apply concepts immediately to security problems
- Hands-on practice with guided exercises

---

## PHASE 1: PYTHON FUNDAMENTALS WITH SECURITY APPLICATIONS

### **UNIT 1: VARIABLES, STRINGS & CONDITIONALS** ✅ COMPLETED
**Status:** Complete

**What You Learned:**
- Variables and data types
- String manipulation and methods
- User input and output
- If/else conditional logic
- Boolean operators (and, or, not)

**Project Built:**
- Basic Password Strength Checker

**Skills Gained:**
- Basic Python syntax
- Conditional logic
- String analysis
- Input validation

---

### **UNIT 2: LOOPS & ITERATION** ✅ COMPLETED
**Status:** Complete

**What You Learned:**
- While loops
- For loops
- Break and continue statements
- Loop control patterns
- Nested loops

**Projects Built:**
- IP Address Collector
- Character Counter
- Advanced Password Strength Checker v2.0 (with GitHub repository)

**Skills Gained:**
- Iteration patterns
- Loop optimization
- Early exit strategies
- Pattern detection in strings

---

### **UNIT 3: FUNCTIONS** 🔄 IN PROGRESS
**Status:** ~60% Complete

**What You're Learning:**
- Function definition and syntax ✅
- Parameters and arguments ✅
- Return values ✅
- Default parameters ✅
- Functions calling other functions ✅
- Variable scope (coming next)
- Docstrings and documentation (coming next)
- Lambda functions (optional)

**Exercises Completed:**
- ✅ Basic functions (square_number, is_even, reverse_string)
- ✅ Password validation function
- ✅ Vowel/consonant counter (functions calling functions)

**Upcoming in Unit 3:**
- Variable scope (local vs global)
- Function documentation with docstrings
- Building a function library

**Final Project:**
- Password Strength Analyzer Library (reusable module)

**Estimated Completion:** 1-2 more sessions

---

## PHASE 2: SECURITY-FOCUSED MODULES

### **MODULE 1: NETWORK FUNDAMENTALS & PORT SCANNING**
**Estimated Duration:** 2-3 weeks

**Cybersecurity Concepts:**
- TCP/IP protocol basics
- Ports and services
- Socket programming
- Network enumeration
- Banner grabbing

**Python Concepts Learned:**
- Lists and list comprehension
- Dictionaries for data storage
- Socket library
- Threading basics
- Error handling with try/except

**Projects:**
1. **Simple Port Scanner**
   - Scan single host for open ports
   - Identify common services

2. **Multi-threaded Port Scanner**
   - Scan multiple ports simultaneously
   - Speed optimization techniques

3. **Banner Grabber**
   - Connect to services
   - Extract version information
   - Identify potential vulnerabilities

4. **Service Enumeration Tool**
   - Comprehensive port scan
   - Service fingerprinting
   - Output to file/report

**Learning Outcomes:**
- Understand how networks communicate
- Identify open services on systems
- Recognize security implications of exposed services
- Build faster, more efficient tools

---

### **MODULE 2: WEB SECURITY & HTTP**
**Estimated Duration:** 2-3 weeks

**Cybersecurity Concepts:**
- HTTP protocol and methods
- Security headers
- Cookies and sessions
- Common web vulnerabilities (XSS, CSRF, SQLi basics)
- Web crawling and scraping

**Python Concepts Learned:**
- Requests library
- Regular expressions (regex)
- JSON parsing
- Working with APIs
- BeautifulSoup for HTML parsing

**Projects:**
1. **HTTP Security Header Checker**
   - Analyze website security headers
   - Identify missing protections
   - Generate security report

2. **Basic Web Crawler**
   - Discover pages on a website
   - Extract links and resources
   - Map website structure

3. **Form Analyzer**
   - Detect input fields
   - Check for CSRF tokens
   - Identify potential injection points

4. **Simple Vulnerability Scanner**
   - Check for common misconfigurations
   - Test for basic XSS
   - Generate findings report

**Learning Outcomes:**
- Understand web application architecture
- Identify common web security issues
- Use HTTP for security testing
- Build web reconnaissance tools

---

### **MODULE 3: CRYPTOGRAPHY & HASH ANALYSIS**
**Estimated Duration:** 2-3 weeks

**Cybersecurity Concepts:**
- Hashing vs encryption
- Common hash algorithms (MD5, SHA-1, SHA-256)
- Salting and password storage
- Basic encryption (symmetric/asymmetric)
- Digital signatures

**Python Concepts Learned:**
- Hashlib library
- Secrets module
- File I/O (reading/writing)
- Working with bytes
- Cryptography library basics

**Projects:**
1. **Password Hash Analyzer**
   - Identify hash types
   - Crack weak hashes
   - Demonstrate importance of strong hashing

2. **Secure Password Generator**
   - Cryptographically secure random passwords
   - Customizable complexity
   - Bulk generation

3. **File Integrity Checker**
   - Calculate file hashes
   - Detect unauthorized modifications
   - Verify file integrity

4. **Simple Encryption/Decryption Tool**
   - Encrypt sensitive files
   - Decrypt with password
   - Demonstrate encryption concepts

**Learning Outcomes:**
- Understand cryptographic fundamentals
- Implement secure password practices
- Verify data integrity
- Basic encryption implementation

---

### **MODULE 4: LOG ANALYSIS & INCIDENT RESPONSE**
**Estimated Duration:** 2-3 weeks

**Cybersecurity Concepts:**
- Log file formats
- Attack pattern recognition
- Incident detection
- Timeline analysis
- IOC (Indicators of Compromise)

**Python Concepts Learned:**
- File parsing
- CSV and JSON processing
- Data aggregation
- Pattern matching with regex
- Datetime handling

**Projects:**
1. **Log Parser**
   - Parse various log formats
   - Extract relevant data
   - Search for specific events

2. **Failed Login Detector**
   - Identify brute force attempts
   - Track authentication failures
   - Alert on suspicious activity

3. **Security Event Aggregator**
   - Combine logs from multiple sources
   - Correlate events
   - Generate timeline

4. **Incident Report Generator**
   - Analyze security events
   - Create detailed reports
   - Visualize attack patterns

**Learning Outcomes:**
- Read and analyze log files
- Detect malicious activity
- Correlate security events
- Generate professional reports

---

### **MODULE 5: MALWARE ANALYSIS BASICS**
**Estimated Duration:** 2-3 weeks

**Cybersecurity Concepts:**
- Static vs dynamic analysis
- File signatures
- Suspicious indicators
- VirusTotal API
- Basic reverse engineering concepts

**Python Concepts Learned:**
- Working with binary files
- API integration
- Hash comparison
- String extraction
- Subprocess execution (safely)

**Projects:**
1. **File Hash Checker**
   - Calculate file hashes
   - Check against known malware databases
   - VirusTotal integration

2. **Suspicious String Extractor**
   - Extract strings from binaries
   - Identify URLs, IPs, file paths
   - Flag potentially malicious indicators

3. **Basic Static Analyzer**
   - Check file properties
   - Extract metadata
   - Identify suspicious characteristics

4. **Malware Hash Database**
   - Store known malware hashes
   - Compare new files
   - Categorize threats

**Learning Outcomes:**
- Safely analyze suspicious files
- Use threat intelligence APIs
- Identify malware indicators
- Build analysis workflows

---

### **MODULE 6: RECONNAISSANCE & OSINT**
**Estimated Duration:** 2-3 weeks

**Cybersecurity Concepts:**
- Open Source Intelligence (OSINT)
- Subdomain enumeration
- Email harvesting (for security testing)
- Metadata extraction
- Information gathering techniques

**Python Concepts Learned:**
- DNS queries
- WHOIS lookups
- PIL/Pillow for image analysis
- Shodan API
- Google dorking automation

**Projects:**
1. **Subdomain Enumerator**
   - Discover subdomains
   - Check DNS records
   - Map attack surface

2. **Metadata Extractor**
   - Extract EXIF from images
   - Parse document metadata
   - Identify information leakage

3. **Email Harvester** (for authorized testing)
   - Extract email addresses from websites
   - Format for security testing
   - Validate email addresses

4. **OSINT Framework**
   - Combine multiple tools
   - Automated reconnaissance
   - Generate recon report

**Learning Outcomes:**
- Gather intelligence ethically
- Map organizational attack surface
- Identify information exposure
- Build OSINT workflows

---

## PHASE 3: ADVANCED TOPICS & FINAL PROJECTS

### **MODULE 7: AUTOMATION & SCRIPTING**
**Estimated Duration:** 2-3 weeks

**Focus Areas:**
- Task automation
- Report generation
- Scheduled security checks
- Alert systems
- Dashboard creation

**Projects:**
- Automated security scanner
- Daily vulnerability check script
- Security dashboard
- Custom security toolkit

---

### **MODULE 8: API SECURITY & TESTING**
**Estimated Duration:** 2 weeks

**Focus Areas:**
- REST API basics
- API authentication
- Rate limiting
- API vulnerability testing
- Building secure APIs

**Projects:**
- API security scanner
- Authentication tester
- Rate limit checker
- API documentation tool

---

### **MODULE 9: FINAL CAPSTONE PROJECT**
**Estimated Duration:** 3-4 weeks

**Choose One:**

**Option A: Comprehensive Security Scanner**
- Combines network, web, and host scanning
- Automated vulnerability detection
- Professional reporting
- Extensible plugin system

**Option B: Security Operations Toolkit**
- Log analysis
- Incident response tools
- Threat intelligence integration
- Case management system

**Option C: Custom Tool Based on Your Interest**
- AI-enhanced security tool (ties into Nova-Cortex)
- Specialized scanner for specific technology
- Security automation framework
- Tool of your choice that demonstrates all skills learned

---

## SKILLS TRACKING

### **Python Skills**
- ✅ Variables and data types
- ✅ String manipulation
- ✅ Conditional logic
- ✅ Loops (while, for)
- ✅ Functions (basic)
- 🔄 Functions (advanced - in progress)
- ⏳ Lists and dictionaries
- ⏳ File I/O
- ⏳ Error handling
- ⏳ Regular expressions
- ⏳ Working with APIs
- ⏳ Threading
- ⏳ Object-oriented programming (basic)

### **Cybersecurity Skills**
- ✅ Password security basics
- ✅ Pattern detection
- ⏳ Network fundamentals
- ⏳ Port scanning
- ⏳ Web security
- ⏳ Cryptography basics
- ⏳ Log analysis
- ⏳ Malware analysis
- ⏳ OSINT techniques
- ⏳ Incident response
- ⏳ Vulnerability assessment
- ⏳ Security tool development

### **Professional Skills**
- ✅ GitHub version control
- ✅ Code documentation
- ✅ Project organization
- ⏳ Professional reporting
- ⏳ Tool distribution
- ⏳ Portfolio development

---

## PORTFOLIO PROJECTS

**Completed:**
1. ✅ Basic Password Strength Checker
2. ✅ Advanced Password Strength Checker v2.0 (on GitHub)

**In Progress:**
3. 🔄 Password Analyzer Library (Unit 3 final project)

**Planned:**
4. Multi-threaded Port Scanner
5. HTTP Security Header Checker
6. Web Vulnerability Scanner
7. Password Hash Cracker
8. Log Analysis Tool
9. Malware Hash Database
10. OSINT Reconnaissance Framework
11. Final Capstone Project

**Goal:** 10-12 polished security tools on GitHub by completion

---

## CERTIFICATION PREPARATION

This curriculum also prepares you for:
- CompTIA Security+ (security concepts)
- CEH (Certified Ethical Hacker) - tool knowledge
- Python Institute PCEP/PCAP certifications
- Entry-level cybersecurity positions

---

## RESOURCES & REFERENCES

**Python Resources:**
- Official Python Documentation
- Real Python tutorials
- Python Crash Course book

**Cybersecurity Resources:**
- OWASP Top 10
- NIST Cybersecurity Framework
- Kali Linux tools documentation
- PortSwigger Web Security Academy

**Practice Environments:**
- TryHackMe
- HackTheBox
- PicoCTF
- DVWA (Damn Vulnerable Web Application)

---

## LEARNING SCHEDULE (FLEXIBLE)

**Weekly Time Commitment:** 5-10 hours recommended

**Typical Week:**
- 2-3 sessions with instructor (like these conversations)
- 2-3 hours independent practice/coding
- 1-2 hours reading/research
- Project work as needed

**Progress Tracking:**
- Exercise completion
- Project submissions to GitHub
- Code reviews
- Quizzes/knowledge checks

---

## CURRENT STATUS SUMMARY

**Date:** January 2026

**Units Completed:** 2/3 (Phase 1)
**Current Unit:** Unit 3 - Functions (60% complete)
**Projects on GitHub:** 1 (Advanced Password Checker)
**Next Milestone:** Complete Unit 3, build Password Analyzer Library
**Next Module:** Network Fundamentals & Port Scanning

**Estimated Time to Phase 2:** 1-2 sessions
**Estimated Total Completion:** 14-18 weeks from now (at current pace)

---

## NOTES

- All code should follow PEP 8 style guidelines
- Every project should include README documentation
- GitHub commits should be meaningful and descriptive
- Test all tools in safe, authorized environments only
- Never use these tools for unauthorized access or illegal activity
- Focus on learning defensive security and ethical hacking principles

---

**This curriculum is a living document and will be updated as we progress!**

Last Updated: January 25, 2026

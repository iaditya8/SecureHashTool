# SecureHashTool
A Python tool to calculate and verify file hashes for digital forensics.

# SecureHashTool – Simple File Hash Checker

This is a small Python script I built to help calculate and verify file hashes using MD5, SHA-1, or SHA-256. It’s my first project in the cyber forensics field and was made to practice basic file handling and hashing in Python.

---

## What It Does

- Calculates a hash value (MD5, SHA-1, or SHA-256) of any file
- Lets you compare it with a known hash to check if the file has been changed
- Useful for checking file integrity or verifying digital evidence

---

## Why I Made It

I'm currently studying MSc Cyber Forensics and learning how tools are built to assist investigations. I wanted to start small by building something that helps verify if a file has been tampered with — which is a common need in forensic cases.

---

## Requirements

- Python 3
- No extra libraries — just uses Python’s built-in `hashlib` module

---

## How to Run It

1. Open your terminal or command prompt
2. Run the script like this:

```bash
python secure_hash_tool.py

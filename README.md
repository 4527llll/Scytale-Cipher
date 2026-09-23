# Scytale Cipher: Ancient Transposition Encryption

## 📖 Project Overview
This project implements the Scytale cipher, one of the oldest known transposition ciphers used by the ancient Spartan military. Unlike substitution ciphers (such as Caesar or Vigenère) that alter the *value* of characters, the Scytale cipher alters the *index position* of characters by simulating a strip of parchment wound around a cylinder of a specific diameter (the key). 

This tool serves as a fundamental demonstration of how altering sequence, rather than meaning, can disrupt unauthorized readability.

## ✨ Core Features
* **Algorithmic Transposition:** Utilizes Python's advanced string slicing capabilities (`[start:stop:step]`) to simulate the physical wrapping and unwrapping of parchment without relying on complex 2D array coordinates.
* **Dynamic Padding Mechanism:** Incorporates mathematical modulo operations `(key - len(text) % key) % key` to dynamically pad plaintext, ensuring boundary safety and seamless decryption alignment.
* **Defensive File I/O:** Isolates plaintext and ciphertext through discrete file handling (`content.txt` and `encryptionResult.txt`), utilizing absolute overwrite modes (`w`) to prevent historical data corruption.

## 🛡️ Security Concepts Demonstrated
* **Transposition vs. Substitution:** Highlights the structural difference in cryptographic design. While substitution ciphers fail against frequency analysis (as the letter 'E' is transformed into a consistent target character), transposition ciphers render frequency analysis useless because the original character frequencies remain completely unchanged.
* **Diffusion (Early Concept):** Demonstrates a primitive form of cryptographic diffusion, where the sequence of the plaintext is scattered across the ciphertext, a concept heavily expanded upon in modern algorithms like AES.
* **Input Validation & Resilience:** Implements strict type checking and bounded inputs to prevent runtime errors (e.g., `ZeroDivisionError` or `ValueError`) during key ingestion.

## 🚀 Quick Start

### Prerequisites
* Python 3.x

### Usage
1. Place your target plaintext inside `content.txt` in the same directory.
2. Run the script via your terminal:
   ```bash
   python scytale.py
# Hybrid Encryption Demo

A small Python demo of **hybrid encryption**: a fast symmetric cipher protects the message, and RSA protects the symmetric key.

## How it works

1. Generate a 2048-bit RSA key pair.
2. Generate a symmetric key (Fernet).
3. Encrypt the message with the Fernet key.
4. Encrypt the Fernet key with the RSA public key (OAEP padding).
5. Decrypt the Fernet key with the RSA private key.
6. Decrypt the message with the recovered Fernet key.

## Requirements

- Python 3.8+
- `cryptography`
- `pycryptodome`

```bash
pip install -r requirements.txt
```

## Usage

```bash
python hybrid_encryption_demo.py
```

Enter a message when prompted; the script prints each step and the final decrypted message.

## Note

This is an educational demo. Keys are generated in memory on every run and are never saved.

from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

print("\n🔐 HYBRID ENCRYPTION DEMO 🔐\n")

# -----------------------------
# STEP 1: Generate RSA Keys
# -----------------------------
print("[1] Generating RSA Keys...")
rsa_key = RSA.generate(2048)
public_key = rsa_key.publickey()

# -----------------------------
# STEP 2: Generate Symmetric Key
# -----------------------------
print("[2] Generating Symmetric Key...")
sym_key = Fernet.generate_key()
cipher_sym = Fernet(sym_key)

# -----------------------------
# STEP 3: Encrypt Message
# -----------------------------
message = input("\nEnter message to encrypt: ").encode()

print("\n[3] Encrypting message using symmetric key...")
encrypted_msg = cipher_sym.encrypt(message)
print("Encrypted Message:", encrypted_msg)

# -----------------------------
# STEP 4: Encrypt Symmetric Key (RSA)
# -----------------------------
print("\n[4] Encrypting symmetric key using RSA public key...")
cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_key = cipher_rsa.encrypt(sym_key)
print("Encrypted Symmetric Key:", encrypted_key)

# -----------------------------
# STEP 5: Decryption Process
# -----------------------------
print("\n[5] Decrypting symmetric key using RSA private key...")
cipher_rsa = PKCS1_OAEP.new(rsa_key)
decrypted_sym_key = cipher_rsa.decrypt(encrypted_key)

print("[6] Decrypting message using symmetric key...")
cipher_sym = Fernet(decrypted_sym_key)
decrypted_msg = cipher_sym.decrypt(encrypted_msg)

print("\n✅ Final Decrypted Message:", decrypted_msg.decode())
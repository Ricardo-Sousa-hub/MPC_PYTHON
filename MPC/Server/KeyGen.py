import secrets
import pickle

# Gerar uma chave secreta de 32 bytes (256 bits)
secret_key = secrets.token_bytes(32)

key = secret_key.hex()

f = open("Key.pickle", "wb")

pickle.dump(key, f)
f.close()
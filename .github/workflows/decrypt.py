import base64
import json
import os
from Crypto.Cipher import AES

PORT_CLIENT_SECRET = os.getenv("PORT_CLIENT_SECRET")
ENCRYPTED_PROPERTY = os.getenv("ENCRYPTED_PROPERTY")

PROPERY_IS_JSON = True

key = PORT_CLIENT_SECRET[:32].encode()


encrypted_property_value = base64.b64decode(ENCRYPTED_PROPERTY)

iv = encrypted_property_value[:16]
ciphertext = encrypted_property_value[16:-16]
mac = encrypted_property_value[-16:]

cipher = AES.new(key, AES.MODE_GCM, iv)

# decrypt the property
decrypted_property_value = cipher.decrypt_and_verify(ciphertext, mac)
property_value = json.loads(decrypted_property_value) if PROPERY_IS_JSON else decrypted_property_value


print(property_value)
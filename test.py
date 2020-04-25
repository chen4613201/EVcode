from cryptography.fernet import Fernet
"""
cipher_key = Fernet.generate_key()
print(type(SECRET_KEY))
cipher = Fernet(SECRET_KEY)
text = b"ZXCV1qaz!@#$"
encrypted_text = cipher.encrypt(MAIL_PASSWORD)
print(encrypted_text)

decrypted_text = cipher.decrypt(MAIL_PASSWORD)
print(type(MAIL_PASSWORD))
print("-------:"+str(decrypted_text,encoding='utf-8'))
print(decrypted_text)
"""
from flask_mail import Mail,Message
m = Mail()
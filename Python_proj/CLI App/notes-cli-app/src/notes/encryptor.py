from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, key):
        self.fernet = Fernet(key)

    def encrypt(self, message: str) -> str:
        return self.fernet.encrypt(message.encode()).decode()

    def decrypt(self, token: str) -> str:
        return self.fernet.decrypt(token.encode()).decode()
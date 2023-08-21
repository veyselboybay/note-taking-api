from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"])

def hash(password):
    return context.hash(password)

def verify(plain_pass,hash_pass):
    return context.verify(plain_pass,hash_pass)
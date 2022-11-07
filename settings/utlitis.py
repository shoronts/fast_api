from passlib.context import CryptContext
from passlib.hash import pbkdf2_sha256


class Hash():
    pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def make_hash(password: str):
        return Hash.pwd_cxt.hash(password)

    def check_hash(hashed_password, plain_password):
        return Hash.pwd_cxt.verify(plain_password, hashed_password)

# class Hash():

#     def make_hash(password: str):
#         return pbkdf2_sha256.hash(password)

#     def check_hash(hashed_password, plain_password):
#         return pbkdf2_sha256.verify(plain_password, hashed_password)

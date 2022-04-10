import bcrypt

from utils import slt


def generate_token(data):
    return bcrypt.hashpw(data.encode(), slt).decode()
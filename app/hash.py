import hashlib


def make_hash(apassword):
  return hashlib.sha256(str.encode(apassword)).hexdigest()

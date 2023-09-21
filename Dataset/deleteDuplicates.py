import hashlib
import os

hashes = set()
directory = "/home/grace/necrophobia-filter/Dataset/Not Disturbing"
for filename in os.listdir(directory):
    path = os.path.join(directory, filename)
    digest = hashlib.sha1(open(path, 'rb').read()).digest()
    if digest not in hashes:
        hashes.add(digest)
    else:
        os.remove(path)

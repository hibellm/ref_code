import hashlib

# https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file

def hash_bytestr_iter(bytesiter, hasher, ashexstr=False):
    for block in bytesiter:
        hasher.update(block)
    return (hasher.hexdigest() if ashexstr else hasher.digest())

def file_as_blockiter(afile, blocksize=65536):
    with afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)


fnamelst='README.md'
fname='README.md'
fdesc='this is a github README file created for delivery 1'

x=[(fname, hash_bytestr_iter(file_as_blockiter(open(fname, 'rb')), hashlib.sha256(),ashexstr=True)),fdesc]
print(x)
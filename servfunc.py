def getFileExt(source):
    s_pos = source.rfind(".")
    if s_pos > 0:
        return source[s_pos:].upper()

def get_bytes_from_file(filename):
    return open(filename, "rb").read()

def fixPath(lzPath):
    if lzPath[len(lzPath) - 1] == "\\":
        return lzPath
    else:
        return lzPath + "\\"

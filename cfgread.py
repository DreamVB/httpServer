# A simple model to handel reading and writeing simple config files.
# by Ben
str_lines = []
str_keys = []
str_values = []

cfgFilename = ''

def keyIndex(key):
    idx = -1
    x = 0
    if key is None : return -1
    for x in range(len(str_keys)):
        if str_keys[x] == key.upper():
            idx = x
            break
    return idx

def keyExists(key):
    return keyIndex(key) != -1

def readKeys():
    return str_keys

def loadCfg(filename):
    global cfgFilename
    cfgFilename = filename

    fp = open(cfgFilename,"r")

    if fp.mode == "r":
        # Clear arrays
        str_values.clear()
        str_keys.clear()
        str_lines.clear()
        for s in fp:
            s = s.strip()
            if len(s) > 0:
                s_pos = s.index("=")
                if s_pos > 0:
                    str_keys.append(s[:s_pos].strip().upper())
                    str_values.append(s[s_pos + 1:].strip())
    fp.close()
    return True

def readVal(key):
    k_idx = keyIndex(key)
    if k_idx == -1:
        return ""
    else:
        # Extract key value
        return str_values[k_idx]

def setVal(key, value):
    idx = keyIndex(key)
    if idx == -1:
        return False
    str_values[idx] = value
    return True

def delKey(key):
    idx = keyIndex(key)
    if idx == -1:
        return False
    del str_keys[idx]
    del str_values[idx]
    return True

def appendKey(key, value):
    # Append new key and value
    idx = keyIndex(key)
    if idx > -1:
        return False
    # Apend
    str_keys.append(key.upper())
    str_values.append(value)
    return True

def update():
    x = 0
    buffer = ""
    for x in range(len(str_keys)):
        buffer += str_keys[x] + "=" + str_values[x] + "\n"

    fp = open(cfgFilename,"w")
    fp.write(buffer)
    fp.close()
    return True
    # Clear buffer
    buffer = ""

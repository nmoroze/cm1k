import smbus

bus = smbus.SMBus(1)
ADDRESS = 0x4A

def read_register(reg):
    word = bus.read_word_data(ADDRESS, reg)
    return ((word>>8)&0xff) + ((word&0xff)<<8) 

def read_ncount():
    return read_register(0x0F)

def read_minif():
    return read_register(0x06)

def read_cat():
    return read_register(0x04)

def read_component():
    data = []
    for _ in xrange(256):
        data.append(read_register(0x01))
    write_register(0x03, 0)
    return data

def write_register(reg, value):
    bus.write_word_data(ADDRESS, reg, ((value>>8)&0xff)+((value&0xff)<<8))

def write_nsr(value):
    write_register(0x0D, value)

def write_testcat(value):
    write_register(0x09, value)

def write_resetchain():
    write_register(0x0C, 0)

def write_comp(index):
    write_register(0x01, index)

def write_lcomp(comp):
    write_register(0x02, comp)

def write_cat(category):
    return write_register(0x04, category)

def write_powersave():
    write_register(0x0E, 0)

# TODO: does vector need to be full 256 bytes long? 
def train_vector(vector, category):
    for byte in vector[:-1]: 
        write_comp(byte)  
    
    write_lcomp(vector[-1])
    write_cat(category)
    

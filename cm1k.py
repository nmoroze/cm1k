import smbus

I2C_ADDRESS = 0x4A

# registers
REG_NSR = 0x0D
REG_GCR = 0x0B
REG_MINIF = 0x06
REG_MAXIF = 0x07
REG_NCR = 0x00
REG_COMP = 0x01
REG_LCOMP = 0x02
REG_INDEXCOMP = 0x03
REG_DIST = 0x03
REG_CAT = 0x04
REG_AIF = 0x05
REG_NID = 0x0A
REG_POWERSAVE = 0x0E
REG_FORGET = 0x0F
REG_NCOUNT = 0x0F
REG_RESETCHAIN = 0x0C

# test registers
REG_TESTCOMP = 0x08
REG_TESTCAT = 0x09

class CM1K(object):
    def __init__(self, bus=1):
        self.bus = smbus.SMBus(bus)

    def read(self, reg):
        word = self.bus.read_word_data(I2C_ADDRESS, reg)
        return ((word>>8)&0xff) + ((word&0xff)<<8) 

    def write(self, reg, value=0):
        self.bus.write_word_data(I2C_ADDRESS, reg, ((value>>8)&0xff)+((value&0xff)<<8))

    def read_component(self):
        data = []
        for _ in xrange(256):
            data.append(self.read(REG_COMP))
        self.write(REG_INDEXCOMP, 0)
        return data

    def train_vector(self, vector, category):
        for byte in vector[:-1]: 
            self.write(REG_COMP, byte)  
        
        self.write(REG_LCOMP, vector[-1])
        self.write(REG_CAT, category)
        

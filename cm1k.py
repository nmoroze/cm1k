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

def write_register(reg, value):
	bus.write_word_data(ADDRESS, reg, ((value>>8)&0xff)+((value&0xff)<<8))

def write_nsr(value):
	write_register(0x0D, value)

def write_testcat(value):
	write_register(0x09, value)

def write_resetchain():
	write_register(0x0C, 0)

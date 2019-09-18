class Mcp492xDac:
    __BIT = {
        "AB": 15,
        "BUF": 14,
        "GA_": 13,
        "SHDN_": 12,
    }
    __DATA_BITS = 12

    def __init__(self, chip, ab):
        self.chip = chip
        self.ab = ab

    def write(self, data, buf=1, ga_=1, shdn_=1):
        ab = self.ab

        cmd = int(0)
        cmd += ab    << self.__BIT["AB"]
        cmd += buf   << self.__BIT["BUF"]
        cmd += ga_   << self.__BIT["GA_"]
        cmd += shdn_ << self.__BIT["SHDN_"]

        cmd += data  << (self.__DATA_BITS - 1)

        cmd_bytes = cmd.to_bytes
        return self.chip.__xfer(cmd_bytes)

class Mcp492x:
    def __init__(self, bus):
        self.bus = bus
        self.dac = [Mcp492xDac(self, 0), Mcp492xDac(self, 1)]

# MCP4921 is I2C version of MCP492x
class Mcp4921(Mcp492x):
    def __init__(self, bus):
        super.__init__

    def __xfer(self, data):
        raise "not implemented"

# MCP4921 is SPI version of MCP492x
class Mcp4922(Mcp492x):
    def __init__(self, bus):
        super.__init__
        
    def __xfer(self, data):
        self.bus.xfer(data)
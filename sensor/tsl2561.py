import io
import fcntl
import time
import struct

class I2CBus:
  I2C_SLAVE = 0x0703 # for ioctl (i2c-dev.h @Linux)

  def __init__(self, bus):
    self.wh = io.open('/dev/i2c-' + str(bus), mode='wb', buffering=0)
    self.rh = io.open('/dev/i2c-' + str(bus), mode='rb', buffering=0)

  def write(self, dev_addr, reg_addr, param=None):
    fcntl.ioctl(self.wh, self.I2C_SLAVE, dev_addr)
    data = bytearray()
    data.append(reg_addr)
    if type(param) is list:
      data.extend(param)
    elif not param is None:
      data.append(param)
    self.wh.write(data)

  def read(self, dev_addr, count, reg_addr=None):
    fcntl.ioctl(self.wh, self.I2C_SLAVE, dev_addr)
    fcntl.ioctl(self.rh, self.I2C_SLAVE, dev_addr)

    if not reg_addr is None:
      self.wh.write(bytearray([reg_addr]))

    return self.rh.read(count)

class TSL2561:
  DEV_ADDR    = 0x39

  REG_CTRL    = 0x80
  REG_TIMING  = 0x81
  REG_DATA    = 0x9B
  REG_ID      = 0x8A

  INTEG_13MS  = 0x00
  INTEG_101MS = 0x01
  INTEG_402MS = 0x02

  GAIN_1X     = 0x00
  GAIN_16X    = 0x10

  POWER_ON    = 0x03
  POWER_OFF   = 0x00

  integ = INTEG_13MS
  gain  = GAIN_1X

  def __init__(self, bus, dev_addr=DEV_ADDR):
    self.bus = bus
    self.dev_addr = dev_addr
    self.i2cbus = I2CBus(bus)

    self.i2cbus.write(self.dev_addr, self.REG_TIMING, self.gain | self.integ)

  def enable(self):
    self.i2cbus.write(self.dev_addr, self.REG_CTRL, self.POWER_ON)

  def disable(self):
    self.i2cbus.write(self.dev_addr, self.REG_CTRL, self.POWER_OFF)

  def wait(self):
    if self.integ == self.INTEG_13MS:
      time.sleep(0.14)
    if self.integ == self.INTEG_101MS:
      time.sleep(0.102)
    if self.integ == self.INTEG_402MS:
      time.sleep(0.403)

  def get_lux(self):
    self.enable()
    self.wait()

    value = self.i2cbus.read(self.dev_addr, 5, self.REG_DATA)

    ch0 = float(struct.unpack('<H', bytes(value[1:3]))[0])
    ch1 = float(struct.unpack('<H', bytes(value[3:5]))[0])

    self.disable()

    if (ch0 == 0):
      return 0.0

    if (self.gain == self.GAIN_1X):
      ch0 *=16
      ch1 *=16

    if (self.integ == self.INTEG_13MS):
      ch0 *= 322.0/11
      ch1 *= 322.0/11
    elif (self.integ == self.INTEG_101MS):
      ch0 *= 322.0/81
      ch1 *= 322.0/81

    if (ch1/ch0) <= 0.52:
      return 0.0304*ch0 - 0.062*ch0*((ch1/ch0)**1.4)
    elif (ch1/ch0) <= 0.65:
      return 0.0224*ch0 - 0.031*ch1
    elif (ch1/ch0) <= 0.80:
      return 0.0128*ch0 - 0.0153*ch1
    elif (ch1/ch0) <= 1.30:
      return 0.00146*ch0 - 0.00112*ch1
    else:
      return 0.0

  def show(self):
    print('{ "lux": %-7.2f }' % (self.get_lux()))

if __name__ == '__main__':
  TSL2561(0x01).show()

Sensor utility
=======================================================================

Both scripts are based on the original one.
Many thanks to original author.


BME280
-----------------------------------------------------------------------

BME280 is a sensor to get temperature, pressure and humidity.

It can be seen in I2C address 0x76.

```
$ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- 76 --
```


### Usage

```bash
$ sudo python3 bme280.py
temperature: 25.32
pressure: 1013.45
humidity: 24.66
```

Unit is "Celsius" for temperature, "hPa" for pressure and "%" for humidity.


#### Prerequisite

`smbus2` library is required to run this script.

```bash
$ sudo pip install smbus2
```


### Acknowledgment

This script is originated from following repository.

https://github.com/SWITCHSCIENCE/BME280


You can create `./bme280.py` from original source by doing this.

```bash
$ git clone https://github.com/SWITCHSCIENCE/BME280
$ cd BME280/Python27
$ patch -p1 < bme280.diff
$ mv bme280_sample.py bme280.py
```

`bme280.diff` is created by me.


### References

- [ＢＭＥ２８０使用　温湿度・気圧センサモジュールキット: センサ一般 秋月電子通商 電子部品 ネット通販](http://akizukidenshi.com/catalog/g/gK-09421/)
- [Raspberry Pi 2で温湿度・気圧センサのBME280をPythonから使う - Qiita](http://qiita.com/masato/items/027e5c824ae75ab417c1)
- [ラズベリーパイで温度・湿度・気圧をまとめて取得！AE-BME280でIC2通信 | Device Plus - デバプラ](http://deviceplus.jp/hobby/raspberrypi_entry_039/)
- [Raspberry Pi + BME280モジュールで自動で温度・湿度・気圧を測定してグラフ化する - karaage. [からあげ]](http://karaage.hatenadiary.jp/entry/2016/05/11/073000)


TSL2561
-----------------------------------------------------------------------

TSL2561 is a sensor to get an illuminance.

It can be seen in I2C address 0x39.

```
$ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- 39 -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

### Usage

```bash
$ sudo python3 tsl2561.py
lux: 464.34
```


#### Prerequisite

None.

This program can run in vanilla Python.


### Acknowledgment

This script is originated from following web page and modification is done by me.

- http://rabbit-note.com/2016/08/02/tsl2561-with-raspberry-pi/
- https://github.com/kimata/rasp-python


### References

- [ＴＳＬ２５６１使用　照度センサーモジュール: センサ一般 秋月電子通商 電子部品 ネット通販](http://akizukidenshi.com/catalog/g/gM-08219/)
- [Raspberry Piでデジタル照度センサーのTSL2561を使う - Qiita](http://qiita.com/masato/items/1dd5bed82b19477b45d8)
- [Raspberry pi 2でTSL2561を使ってpythonで照度を取得する | いなばのメモ](http://blog.1783.org/2016/03/raspi2_tsl2561/)
- [Raspberry Pi 2でAdafruit TSL2561を正しく使うメモ - 下林明正のブログ](http://shimobayashi.hatenablog.com/entry/2015/07/27/001708)
- [Raspberry Pi で照度センサ TSL2561 を使う - Rabbit Note](http://rabbit-note.com/2016/08/02/tsl2561-with-raspberry-pi/)



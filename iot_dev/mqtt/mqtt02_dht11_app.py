#!/usr/bin/env python

import paho.mqtt.client as mqtt
import Adafruit_DHT as dht
import json
import time
import datetime as dt
import uuid

from collections import OrderedDict

sensor = dht.DHT11
pin = 4
count = 0

try:
    #uuid generating
    def_id = "HUGO01"
    div_uid = uuid.uuid3(uuid.NAMESPACE_OID, def_id)

    #mqtt publisher
    broker_address = "192.168.0.5"
    client2 = mqtt.Client("TempressurClient")
    client2.connect(broker_address)

    #dh11 init

    while True:
        count += 1        
        currtime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        # 센서값 가져오기
        h, t = dht.read_retry(sensor, pin)
        # groupdata 만들기
        raw_data = OrderedDict()

        raw_data["uuid"] = def_id
        raw_data["time"] = currtime
        raw_data["temperature"] = "{0:0.1f}".format(t)
        #raw_data["pressure"] = data.pressure
        raw_data["humidity"] = "{0:0.1f}".format(h)

        pub_data = json.dumps(raw_data, ensure_ascii=False, indent="\t")

        #mqtt published
        print(div_uid, pub_data)
        client2.publish("home/device/data/", pub_data)

        time.sleep(5)

except Exception as ex:
    print('Error raised ', ex)




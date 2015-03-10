#!/usr/bin/python

import paho.mqtt.publish as pub

pub.single("test/lynn", "A test from the outside 1234",
        hostname="xmpptest.wellkeeper.net",
        port=1883,
        #tls={'ca_certs':None,'tls_version':"tlsv1"},
        auth={'username':"wktest",'password':"wktest"})

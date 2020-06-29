#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:59:00 2020

@author: kushagra
"""


import tensorflow as tf

hello = tf.constant('hello world!')

sess = tf.Session()

print(sess.run(hello))

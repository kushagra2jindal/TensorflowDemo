#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:37:34 2020

@author: kushagra
"""


import tensorflow as tf 

g = tf.Graph()
with g.as_default():
    c = tf.constant(30.0)
    assert c.graph is g
    
print (g)
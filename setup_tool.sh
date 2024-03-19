#!/bin/bash
for i in `cat tools.txt`;do git clone $i;done
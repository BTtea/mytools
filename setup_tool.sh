#!/bin/bash
for i in `cat tools.txt`;do git clone $i;done
# python3 -m pip install -i https://pypi.org/simple/ GitHacker

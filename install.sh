#!/usr/bin/env bash
python setup.py build
sudo python setup.py install
rm -r build/

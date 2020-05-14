#!/bin/bash

# This is a script used to change between python versions on Ubuntu

# After installing both python3.7 and python3.8:
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2

# List alternatives
sudo update-alternatives --list python

# Configure version used by:
sudo update-alternatives --config python

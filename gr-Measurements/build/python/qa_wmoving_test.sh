#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/user/workarea-gnuradio/gr-Measurements/python
export PATH=/home/user/workarea-gnuradio/gr-Measurements/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/user/workarea-gnuradio/gr-Measurements/build/swig:$PYTHONPATH
/usr/bin/python2 /home/user/workarea-gnuradio/gr-Measurements/python/qa_wmoving.py 

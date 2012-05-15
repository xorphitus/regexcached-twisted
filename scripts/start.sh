#!/bin/sh
cd `dirname $0`
BACKPATH=`pwd`
cd ..
PYTHONPATH=`pwd`
export PYTHONPATH
cd ${BACKPATH}
twistd -y server.tac

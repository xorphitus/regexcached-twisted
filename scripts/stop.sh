#!/bin/sh
cd `dirname $0`
cd ..
kill -9 `find . -name twistd.pid | xargs cat`

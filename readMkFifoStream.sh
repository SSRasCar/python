#!/bin/bash

if [ -p fifo264 ]
then
    rm fifo264
fi
mkfifo fifo264
nc -l -v 5777 > fifo264

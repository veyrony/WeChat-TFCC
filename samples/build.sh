#!/bin/bash

if [ $# -ne 1 ];then
    echo "usage: $0 INSTALLED_TFCC_PATH"
    exit -1
fi
INSTALLED_TFCC_PATH=$1

cd $(dirname $0)
if [ ! -d build ];then
    mkdir build
fi
cd build

# choose your actual TFCC_PREFIX_PATH
cmake .. -DCMAKE_PREFIX_PATH=${INSTALLED_TFCC_PATH}/tfcc
make

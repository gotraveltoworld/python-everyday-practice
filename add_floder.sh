#!/bin/bash

now=$(date -v -0d '+%Y%m%d')
mkdir -p everyday/$now
touch everyday/$now/example.md
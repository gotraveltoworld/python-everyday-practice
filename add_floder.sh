#!/bin/bash

# for date in $(seq 1 10)
# do

#     # mkdir -p everyday/$now
#     # touch everyday/$now/example.md
#     echo $date
# done

for (( i=0; i<=2; i=i+1 ))
do
    now=$(date -v -${i}d '+%Y%m%d')
    if test -e everyday/$now; then
        echo $now', Exist'
    else
        echo $now', No Exist'
        mkdir -p everyday/$now
        touch everyday/$now/example.md
    fi
done
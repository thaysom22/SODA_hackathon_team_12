#!/bin/bash

while read a; do
    export $a
done <.env

flask run

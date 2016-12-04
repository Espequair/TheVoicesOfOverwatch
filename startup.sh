#!/bin/bash

user_agent=$(cat credentials.txt | head -n 1 | tail -n 1)
client_id=$(cat credentials.txt | head -n 2 | tail -n 1)
client_secret=$(cat credentials.txt | head -n 3 | tail -n 1)
username=$(cat credentials.txt | head -n 4 | tail -n 1)
password=$(cat credentials.txt | head -n 5 | tail -n 1)

python3 $1 $user_agent $client_id $client_secret $username $password

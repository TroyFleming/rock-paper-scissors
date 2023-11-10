#!/bin/bash

echo "Would you like to play rock, paper, scissors? (Y/N)"
read answer

if [ "$answer" == "y" ]
then
    python rock_paper_scissors.py
else
    echo "That's too bad, maybe next time!"
fi
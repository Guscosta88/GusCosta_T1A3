#!/bin/bash
    command sudo python3 -m pip install --upgrade pip
    command sudo apt update && sudo apt install python3.10-venv
    command sudo apt install python3-venv
    command python3 -m venv .venv
    command source .venv/bin/activate
    command pip install simple-term-menu
    command pip install clearing
    command pip install cowsay
    command pip install color-terminal
    command pip install pytest
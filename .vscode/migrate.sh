#!/bin/bash

# Generates the script required to move objects to database
python3 -m taskmanager.tools.manage db migrate

# Pushes the updates to the database
python3 -m taskmanager.tools.manage db upgrade
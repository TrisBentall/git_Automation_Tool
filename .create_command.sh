#!/bin/bash

function create()   {
    cd "%filepath%/git_Automation_Tool"
    python3 create.py "$1"
    cd "%YOUR PROJECT FILEPATH%"
}
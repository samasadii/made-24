#!/bin/bash

# Setting up the environment
echo "Setting up the test environment..."
mkdir -p ../data

# Running the test script
echo "Running the tests..."
python tests.py

# Check exit code of the tests
if [ $? -eq 0 ]; then
    echo "Tests passed successfully!"
else
    echo "Tests failed."
    exit 1
fi

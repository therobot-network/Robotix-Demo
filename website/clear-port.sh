#!/bin/bash

# Default port for Vite dev server
PORT=${1:-5173}

echo "Checking for processes on port $PORT..."

# Find and kill process using the port
PID=$(lsof -ti :$PORT)

if [ -z "$PID" ]; then
    echo "No process found on port $PORT"
else
    echo "Killing process $PID on port $PORT..."
    kill -9 $PID
    echo "Port $PORT cleared successfully"
fi


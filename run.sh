#!/bin/bash
# run.sh
# Launch script for GTK Python Dashboard Starter
# Auto-activates virtual environment if it exists

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if virtual environment exists and activate it
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "Warning: Virtual environment not found."
    echo "Run ./s002_setup_venv.sh to create it."
    echo "Proceeding with system Python..."
    echo ""
fi

# Run the application
python3 src/main.py "$@"

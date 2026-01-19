#!/bin/bash

# Linting script for the backend

cd "$(dirname "$0")"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Check if dev dependencies are installed
if ! python -c "import ruff" 2>/dev/null; then
    echo "Installing development dependencies..."
    pip install -r requirements-dev.txt
fi

# Run the requested command
case "$1" in
    lint)
        ruff check .
        ;;
    lint:fix)
        ruff check --fix .
        ;;
    format)
        black .
        ;;
    format:check)
        black --check .
        ;;
    typecheck)
        mypy app
        ;;
    check)
        echo "Running linting..."
        ruff check . || exit 1
        echo "Checking formatting..."
        black --check . || exit 1
        echo "Running type checker..."
        mypy app || exit 1
        echo "All checks passed!"
        ;;
    *)
        echo "Usage: $0 {lint|lint:fix|format|format:check|typecheck|check}"
        exit 1
        ;;
esac


.PHONY: start dev backend install help

help:
	@echo "Available commands:"
	@echo "  make start    - Start the backend server"
	@echo "  make dev      - Start the backend server (alias for start)"
	@echo "  make backend  - Start the backend server (alias for start)"
	@echo "  make install  - Install Python dependencies"

start:
	cd backend && ./start.sh

dev: start

backend: start

install:
	cd backend && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt


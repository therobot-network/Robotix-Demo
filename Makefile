.PHONY: dev build install clean test help website-dev website-build website-install

# Default target
all: install

# Install all dependencies
install:
	@echo "Installing website dependencies..."
	cd website && make install
	@echo "Installing generator dependencies..."
	pip3 install -r requirements.txt

# Run website dev server
dev: website-dev

website-dev:
	cd website && make dev

# Build website
build: website-build

website-build:
	cd website && make build

# Install website dependencies
website-install:
	cd website && make install

# Preview website
preview:
	cd website && make preview

# Lint website
lint:
	cd website && make lint

# Clear website port
clear-port:
	cd website && make clear-port

# Clean everything
clean:
	cd website && make clean
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Generate data
generate-data:
	cd generators && python3 main.py

# Help command
help:
	@echo "Available commands:"
	@echo "  make install          - Install all dependencies (website + python)"
	@echo "  make dev              - Start website dev server (clears port first)"
	@echo "  make build            - Build website for production"
	@echo "  make preview          - Preview production build"
	@echo "  make lint             - Run website linter"
	@echo "  make clear-port       - Clear the website dev server port"
	@echo "  make clean            - Clean all build artifacts"
	@echo "  make generate-data    - Run data generators"
	@echo "  make website-install  - Install website dependencies only"


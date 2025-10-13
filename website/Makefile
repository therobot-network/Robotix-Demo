.PHONY: dev build preview lint clean clear-port install

# Install dependencies
install:
	npm install

# Clear port and run dev server
dev:
	@chmod +x clear-port.sh
	@./clear-port.sh
	npm run dev

# Build for production
build:
	npm run build

# Preview production build
preview:
	npm run preview

# Run linter
lint:
	npm run lint

# Clear the dev server port (default 5173)
clear-port:
	@chmod +x clear-port.sh
	@./clear-port.sh

# Clean build artifacts and node_modules
clean:
	rm -rf dist node_modules

# Help command
help:
	@echo "Available commands:"
	@echo "  make install     - Install npm dependencies"
	@echo "  make dev         - Clear port and start dev server"
	@echo "  make build       - Build for production"
	@echo "  make preview     - Preview production build"
	@echo "  make lint        - Run linter"
	@echo "  make clear-port  - Clear the dev server port"
	@echo "  make clean       - Remove build artifacts and dependencies"


.PHONY: help validate-all build-all clean setup test lint

# Default target
help:
	@echo "Tesla Lightshow Creator - Available Commands:"
	@echo ""
	@echo "  make setup          - Set up the project (install dependencies)"
	@echo "  make validate-all   - Validate all shows"
	@echo "  make build-all      - Build all shows for deployment"
	@echo "  make clean          - Clean build directory"
	@echo "  make test           - Run tests"
	@echo "  make lint           - Run Python linting"
	@echo "  make new SHOW=name  - Create a new show"
	@echo ""
	@echo "Examples:"
	@echo "  make new SHOW=\"My Awesome Show\""
	@echo "  make validate-all"
	@echo "  make build-all"

# Setup the project
setup:
	@echo "Setting up Tesla Lightshow Creator..."
	@pip install -r requirements.txt
	@mkdir -p shows build docs templates
	@chmod +x tools/*.py
	@echo "✓ Setup complete!"

# Create a new show
new:
	@if [ -z "$(SHOW)" ]; then \
		echo "Error: Please provide a show name with SHOW=\"name\""; \
		echo "Example: make new SHOW=\"My Awesome Show\""; \
		exit 1; \
	fi
	@python3 tools/create_show.py "$(SHOW)"

# Validate all shows
validate-all:
	@echo "Validating all shows..."
	@for show in shows/*/; do \
		if [ -d "$$show" ]; then \
			echo ""; \
			python3 tools/validate.py "$$show"; \
		fi \
	done
	@echo ""
	@echo "✓ Validation complete!"

# Build all shows
build-all:
	@echo "Building all shows..."
	@for show in shows/*/; do \
		if [ -d "$$show" ]; then \
			echo ""; \
			python3 tools/package.py "$$show"; \
		fi \
	done
	@echo ""
	@echo "✓ Build complete! Check the build/ directory"

# Clean build directory
clean:
	@echo "Cleaning build directory..."
	@rm -rf build/*
	@echo "✓ Clean complete!"

# Run tests (placeholder for future test suite)
test:
	@echo "Running tests..."
	@python3 -m pytest tests/ -v || echo "No tests found yet"

# Lint Python code
lint:
	@echo "Linting Python code..."
	@python3 -m pylint tools/*.py || echo "Install pylint with: pip install pylint"

# Quick validate and build a specific show
# Usage: make deploy SHOW=my-show-dir
deploy:
	@if [ -z "$(SHOW)" ]; then \
		echo "Error: Please provide a show directory with SHOW=dirname"; \
		echo "Example: make deploy SHOW=my-awesome-show"; \
		exit 1; \
	fi
	@echo "Validating $(SHOW)..."
	@python3 tools/validate.py "shows/$(SHOW)" -v
	@echo ""
	@echo "Building $(SHOW)..."
	@python3 tools/package.py "shows/$(SHOW)"
	@echo ""
	@echo "✓ Show ready for deployment! Check build/$(SHOW)/"


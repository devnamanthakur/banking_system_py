# Makefile for Python Terminal Banking System

.PHONY: run help format

run:
	uv run -m src.main

format:
	@echo "Formatting the project..."
	uv run ruff format

help:
	@echo "Available targets:"
	@echo "  run    - Run the banking system application"
	@echo "  format - Format code using ruff"
	@echo "  help   - Show this help message" 
# Makefile for Python Terminal Banking System

.PHONY: run help

run:
	uv run -m src.main

help:
	@echo "Available targets:"
	@echo "  run   - Run the banking system application"
	@echo "  help  - Show this help message" 
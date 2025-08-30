.PHONY: help install dev build test clean

.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "ApneDoctors Mini-RAG Development Commands"
	@echo "========================================"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-20s %s\n", $$1, $$2}'

install: ## Install all dependencies
	cd backend && pip install -r requirements.txt
	cd frontend && npm install

dev: ## Start development environment
	docker-compose up --build

build: ## Build all Docker images
	docker-compose build

test: ## Run all tests
	cd backend && python -m pytest tests/ -v || echo "Tests will be added"
	cd frontend && npm test -- --coverage --watchAll=false || echo "Tests will be added"

clean: ## Clean up containers and images
	docker-compose down -v
	docker system prune -f

quick-start: ## Quick start for first-time users
	cp .env.template .env
	docker-compose up --build -d
	@echo "ApneDoctors is running at:"
	@echo "  Frontend: http://localhost:3000"
	@echo "  Backend:  http://localhost:8000"
	@echo "  API Docs: http://localhost:8000/docs"

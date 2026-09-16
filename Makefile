# ============================================================
# AI 智能笔记助手 - 本地门禁，与 .github/workflows/ci.yml 对齐
# 在仓库根目录执行：make lint && make test && make build
# ============================================================

SHELL := /bin/bash
PY      := cd backend && .venv/bin/python
UV      := cd backend && .venv/bin/uv
FRONT   := cd front && npm

.PHONY: help lint lint-backend lint-front typecheck test test-backend build build-front \
        deepeval perf ci check

help:
	@echo "可用目标："
	@echo "  make lint      后端 ruff+isort + 前端 eslint"
	@echo "  make typecheck 前端 vue-tsc 类型检查"
	@echo "  make test      后端纯逻辑快单测（带覆盖率，跳过 GPU/DB/LLM）"
	@echo "  make build     前端 vite 生产构建"
	@echo "  make ci        以上全部（等价 GitHub CI 门禁）"
	@echo "  make deepeval  RAG 质量门禁（需 DashScope + 向量库 + MySQL/Redis）"
	@echo "  make perf      RAG 性能/端到端（需 :8000 后端 + 模型服务）"

# ── Lint ────────────────────────────────────────────────────
lint: lint-backend lint-front

lint-backend:
	$(UV) run ruff check app tests
	$(UV) run ruff format --check app tests
	$(UV) run isort --check-only app tests

lint-front:
	$(FRONT) run lint

typecheck:
	$(FRONT) run typecheck

# ── 单元测试（常规 CI 用，显式忽略重评测目录 + GPU import）────
test: test-backend

test-backend:
	$(UV) run pytest tests/ \
		--ignore=tests/deepeval_eval --ignore=tests/rag_eval \
		-m "not deepeval and not perf" \
		--cov=app --cov-report=xml --cov-report=term-missing

# ── 构建 ────────────────────────────────────────────────────
build: build-front

build-front:
	$(FRONT) run build

# ── 重评测（手动，需外部资源）─────────────────────────────────
deepeval:
	$(PY) -m pytest tests/deepeval_eval -m deepeval

perf:
	$(PY) -m pytest tests/rag_eval -m perf

# ── 等价 GitHub CI 门禁 ──────────────────────────────────────
ci: lint typecheck test build
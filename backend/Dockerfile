# ============================================================
# 后端 FastAPI (8000) — 多阶段构建
# 只打包 Web 层；MySQL/Redis/向量库/LLM 均为运行期经 env 指向的外部服务
# ============================================================
# ── builder：安装运行依赖 ──
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder
WORKDIR /app

COPY pyproject.toml uv.lock ./
# 只装运行依赖，不装 dev/GPU 权重（torch/unstructured 很重，此处仅 1 次层缓存）
RUN uv sync --frozen --no-dev --no-install-project

# ── 复制源码（利用 build context 排除 .venv/.env 等）──
COPY main.py .
COPY app ./app
COPY .env.example .env.example
ENV PATH="/app/.venv/bin:$PATH"

# ── 运行时 ──
FROM python:3.12-slim AS runtime
WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/.venv/bin:$PATH"

# 轻量运行镜像无需 gcc 等构建工具
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/main.py /app/main.py
COPY --from=builder /app/app /app/app
COPY --from=builder /app/.env.example /app/.env.example

# 运行期可写目录（图片/附件抽取落盘、qv/celery 缓存）
RUN mkdir -p /app/storage /app/logs && chown -R 65532:65532 /app
USER 65532

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
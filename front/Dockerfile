# ============================================================
# 前端 Vue3 (nginx :80) — 两段构建
# 运行时由 nginx 伺服 dist 并反代后端 /knowledge /chat /user /file
# 注意：build context = 仓库根（需引用 deploy/container-nginx.conf），
#       请在 compose / CI 里用 context=仓库根 + dockerfile=front/Dockerfile
# ============================================================
FROM node:20-bookworm-slim AS build
WORKDIR /app

COPY front/package.json front/package-lock.json ./
RUN npm ci

COPY front/ ./
RUN npm run build

# ── runtime：nginx 伺服 + 反代 ──
FROM nginx:alpine AS runtime
COPY deploy/container-nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
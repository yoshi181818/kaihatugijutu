# ステージ1: ビルド
FROM python:3.10 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --target=/install -r requirements.txt
# ステージ2: 実行
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /install /usr/local/lib/python3.10/site-packages
COPY src/ ./src/
ENV FLASK_APP=src.app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
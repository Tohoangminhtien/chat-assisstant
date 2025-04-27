FROM python:3.11-slim

WORKDIR /app

# Cài đặt các phụ thuộc hệ thống
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    libffi-dev \
    libssl-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Cài đặt uv
RUN pip install uv

# Sao chép mã nguồn và .env
COPY . .

# Cài đặt thư viện với timeout tăng
ENV UV_HTTP_TIMEOUT=600
RUN uv pip install --system -r requirements.txt

ENV PYTHONUNBUFFERED=1

EXPOSE 7860

CMD ["python", "app.py"]
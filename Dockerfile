
# Stage 1: Install application dependencies
FROM python:3.12-slim AS builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

COPY app/requirements.txt .

RUN python -m pip install --no-cache-dir --prefix=/install -r requirements.txt


# Stage 2: Create the runtime image
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only the installed application dependencies
COPY --from=builder /install /usr/local

# Create a dedicated non-root user
RUN useradd --create-home --shell /usr/sbin/nologin appuser

# Copy application code with appropriate ownership
COPY --chown=appuser:appuser app/ .

USER appuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
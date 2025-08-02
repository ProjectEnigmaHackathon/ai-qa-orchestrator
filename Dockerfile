# Use official Python base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user for security
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser

# Expose both ports
EXPOSE 8501
EXPOSE 8502

# Start both apps using a process manager (e.g., supervisord)
#RUN pip install supervisor

#COPY supervisord.conf /etc/supervisord.conf

#CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisord.conf"]
CMD ["sh", "-c", "python run_real_app.py & python run_demo.py && tail -f /dev/null"]

"""Gunicorn configuration file for optimal performance on Render.com"""
import os
import multiprocessing

# Basic settings
bind = f"0.0.0.0:{os.environ.get('PORT', '5000')}"
workers = int(os.environ.get('WEB_CONCURRENCY', multiprocessing.cpu_count() * 2 + 1))

# Prevent workers from being killed too quickly
timeout = 120  # Increased timeout to 120 seconds
graceful_timeout = 30
keepalive = 5
max_requests = 1000
max_requests_jitter = 100

# Performance settings
worker_class = "sync"
worker_connections = 1000
threads = 2

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Handle reloads gracefully
preload_app = True

FROM python:3.9-slim

WORKDIR /app

COPY christmas_tree.py /app/christmas_tree.py

CMD ["python3", "christmas_tree.py"]

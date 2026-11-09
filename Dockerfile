FROM python:3.11-slim
WORKDIR /app
COPY mainprogram.py inventory.py product.py canbeshipped.py supplier.py order.py orderline.py .
CMD ["python", "mainprogram.py"]
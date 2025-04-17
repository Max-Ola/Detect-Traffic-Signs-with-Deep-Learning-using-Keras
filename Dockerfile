FROM tensorflow/tensorflow:2.13.0
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "src/train.py"]
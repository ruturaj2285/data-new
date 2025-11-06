FROM public.ecr.aws/lambda/python:3.12
WORKDIR /var/task
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /root/.cache/pip
COPY . .
CMD ["lambda_handler.lambda_handler"]

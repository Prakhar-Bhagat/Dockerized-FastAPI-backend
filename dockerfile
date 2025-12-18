# 1. Start from a lightweight Python base image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /code

# 3. Copy requirements first (this optimizes Docker's caching mechanism)
COPY ./requirements.txt /code/requirements.txt

# 4. Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. Copy the rest of your application code
COPY ./app /code/app

# 6. Run the application
# "0.0.0.0" is critical inside Docker! It means "listen on all network interfaces".
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
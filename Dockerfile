FROM python:3.9-alpine3.13
LABEL maintainer='bishwas'

ENV PYTHONUNBUFFERED=1
ENV PATH="/py/bin:$PATH"

# Copy the requirements file and application code
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

# Set the working directory
WORKDIR /app
EXPOSE 8000

ARG DEV=false

# Install bash and dependencies
RUN apk update && \
    apk add --no-cache bash && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then \
        /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp

# Create a non-root user
RUN adduser --disabled-password --no-create-home django-user

# Switch to the non-root user
USER django-user

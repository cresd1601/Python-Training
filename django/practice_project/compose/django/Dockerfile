###########
# BUILDER #
###########

# Pull official base image for building
FROM python:3.11.4-slim-buster AS builder

# Set work directory and environment variables
ENV BUILD_DIR=/usr/src/app
WORKDIR $BUILD_DIR

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (gcc for building some Python packages)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# Upgrade pip and install flake8 for linting
RUN pip install --upgrade pip && \
    pip install flake8==6.0.0

# Copy only the necessary production-related files (e.g., source code, requirements)
COPY ./src/requirements/production.txt $BUILD_DIR/src/requirements/production.txt
COPY ./src/ $BUILD_DIR/src/

# Run flake8 linting (optionally only on the core codebase or specific folders)
RUN flake8 $BUILD_DIR/src --ignore=E501,F401

# Build wheels for the production environment
RUN pip wheel --no-cache-dir --no-deps --wheel-dir $BUILD_DIR/wheels -r $BUILD_DIR/src/requirements/production.txt

#########
# FINAL #
#########

# Pull official base image for the final container
FROM python:3.11.4-slim-buster

# Create directory for the app user
RUN mkdir -p /home/app

# Create the app user and define paths
RUN addgroup --system app && adduser --system --group app
ENV FINAL_DIR=/home/app/web

# Create the app directory and set it as the working directory
RUN mkdir $FINAL_DIR
RUN mkdir $FINAL_DIR/staticfiles
WORKDIR $FINAL_DIR

# Install additional dependencies (netcat)
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy built wheels and requirements from the builder stage
COPY --from=builder /usr/src/app/wheels $FINAL_DIR/wheels
COPY --from=builder /usr/src/app/src/requirements/production.txt $FINAL_DIR/src/requirements/production.txt

# Install Python dependencies from the built wheels
RUN pip install --upgrade pip && \
    pip install --no-cache $FINAL_DIR/wheels/*

# Copy the necessary files for production
COPY ./src/ $FINAL_DIR/src/

# Copy only the entrypoint and start-prod scripts to the correct location
COPY ./scripts/entrypoint.sh $FINAL_DIR/scripts/entrypoint.sh
COPY ./scripts/start-prod.sh $FINAL_DIR/scripts/start-prod.sh

# Fix line endings and set execute permissions on the entrypoint and startup scripts
RUN sed -i 's/\r$//g' $FINAL_DIR/scripts/entrypoint.sh $FINAL_DIR/scripts/start-prod.sh && \
    chmod +x $FINAL_DIR/scripts/entrypoint.sh $FINAL_DIR/scripts/start-prod.sh

# Ensure all files in the app directory are owned by the app user
RUN chown -R app:app $FINAL_DIR

# Switch to the non-root app user
USER app

# Use absolute paths for ENTRYPOINT and CMD to avoid errors
ENTRYPOINT ["/home/app/web/scripts/entrypoint.sh"]
CMD ["/home/app/web/scripts/start-prod.sh"]
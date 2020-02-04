# the image requires python
FROM python:3

# Create app directory and move into it
WORKDIR /usr/src/app

# Copy all files into container
COPY . .

# Install packages
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5002

# Run app
CMD [ "python", "img2json.py" ]

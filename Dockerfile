# the image requires python
FROM python:3

# Create app directory and move into it
WORKDIR /usr/src/app

# Copy all files into container
COPY . .

# Install packages
export http_proxy=http://172.16.98.151:8118
export https_proxy=http://172.16.98.151:8118
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5002

# Run app
CMD [ "python", "img2json.py" ]

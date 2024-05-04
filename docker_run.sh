docker run -p 8000:8000 \
     -e SECRET_KEY='SECRET_KEY' \
     -e DB_NAME='DB_NAME' \
     -e DB_USERNAME='DB_USERNAME' \
     -e DB_PASSWORD='DB_PASSWORD' \
     -e DB_HOSTNAME='DB_HOSTNAME' \
     -e DB_PORT=5432 \
     -e EMAIL_USER='puneet.jsr02@gmail.com' \
     -e EMAIL_PASSWORD='HEYpyjama' \
     recipe-app

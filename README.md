зоздаем фаил .env и пишем 
SECRET_KEY= свой токен

AWS_ACCESS_KEY_ID= свой логин
AWS_SECRET_ACCESS_KEY=свой пароль
AWS_STORAGE_BUCKET_NAME= своё имя контейнера
AWS_S3_ENDPOINT_URL= http://minio:9000

далее пишем docker-compose up --build
и ждем когда все запустится

http://127.0.0.1:8000/api/profiles/ джанго
http://localhost:9001/browser/testback minio

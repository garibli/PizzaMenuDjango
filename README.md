This project can be uploaded to docker. for this, follow the steps mentioned bellow:
1) Open "settings.py";
2) Scroll down to the database settings;
3) Change HOST parameter from 'localhost' to 'db';
4) Open terminal and come to the directory where .yml file is;
5) run the command:  ~$ docker-compose up
6) Wait until the terminal to upload files to docker.
2 image files and 1 container will be created: one for database, named "postgres" and one for the application, named "Ornek"

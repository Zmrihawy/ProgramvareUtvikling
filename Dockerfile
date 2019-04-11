version: "2"
services:
  db:
    image: sqlite3
  django:
    build: .
    restart: always
    command: python3 chefsApprentice/manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
    depends_on:
      - db
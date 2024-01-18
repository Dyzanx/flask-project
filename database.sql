-- CODE FOR POSTGRE SQL
CREATE DATABASE blog;

CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY NOT NULL,
    name varchar(255) NOT NULL,
    lastname varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    password TEXT NOT NULL,
    username varchar(255) NOT NULL,
);

INSERT INTO  users (name, lastname, email, password, username, birth_date) VALUES('Edison', 'Orozco', 'andresorozco1206@gmail.com', '1234', '@edison', CURRENT_DATE)

CREATE TABLE IF NOT EXISTS themes(
    id SERIAL PRIMARY KEY NOT NULL,
    name varchar(255) NOT NULL,
    date DATE DEFAULT CURRENT_DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS posts(
    id SERIAL PRIMARY KEY NOT NULL,
    user_id int NOT NULL,
    theme_id int NOT NULL,
    title varchar(255) NOT NULL,
    content TEXT NOT NULL,
    posted_date DATE DEFAULT CURRENT_DATE NOT NULL,

    CONSTRAINT fk_posts_users FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_posts_themes FOREIGN KEY (theme_id) REFERENCES themes(id)
);
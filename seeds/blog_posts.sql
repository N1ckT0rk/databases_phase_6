-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;


-- Create the table without the foreign key first.
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text
);

INSERT INTO posts (title, content) VALUES ('Post1', 'Content1');
INSERT INTO posts (title, content) VALUES ('Post2', 'Content2');


-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content text,
    author_name text,
-- The foreign key name is always {other_table_singular}_id
    post_id int,
    constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);


INSERT INTO comments (content, author_name, post_id) VALUES ('Content1', 'Barry', 1);
INSERT INTO comments (content, author_name, post_id) VALUES ('Content2', 'Gary', 1);
INSERT INTO comments (content, author_name, post_id) VALUES ('Content3', 'Larry', 2);
INSERT INTO comments (content, author_name, post_id) VALUES ('Content4', 'Carrey', 2);
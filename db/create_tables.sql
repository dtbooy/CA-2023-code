/* 

*/

DROP TABLE items;
DROP TABLE categories;


CREATE TABLE IF NOT EXISTS categories (
    id serial PRIMARY KEY,
    name varchar(100) NOT NULL,
    description text
);

INSERT INTO 
    categories (name, description) 
VALUES 
    ('Electronics', 'Gadgets to make life easier'),
    ('Car parts', 'Expensive stuff for the box with 4 wheels'),
    ('Sports', 'Get out and play'),
    ('Video Games', 'Stay in and play!');

CREATE TABLE IF NOT EXISTS items (
    id serial PRIMARY KEY,
    name varchar(200) NOT NULL,
    description text NOT NULL,
    category_id integer NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories (id) 
);



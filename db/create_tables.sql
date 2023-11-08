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
    FOREIGN KEY (category_id) REFERENCES categories (id) on delete cascade
);

INSERT INTO items (name, description, category_id) VALUES 
    ('Skyrim', 'Awesome open-world RPG', 4),
    ('World of warcraft', 'Popular MMORPG', 4),
    ('iPhone', 'Apple''s Flagship phone', 1), -- to use a ' in a string use ''
    ('Greg Norman golf clubs', 'At least you can look like a pro', 3);

DROP DATABASE quotes_app;
CREATE DATABASE quotes_app;
\c quotes_app;


CREATE TABLE addresses( street_address text,
                        city text,
                        us_state text,
                        zip_code text,
                        id serial PRIMARY KEY );

CREATE TABLE customers( first_name text,
                        last_name text,
                        email text,
                        phone text,
                        mailing_address int REFERENCES addresses,
                        id serial PRIMARY KEY );

CREATE TABLE ingredients( name text,
                          price_per_unit real,
                          unit_of_measurement text,
                          id serial PRIMARY KEY );

CREATE TABLE items( name text,
                    id serial PRIMARY KEY );

CREATE TABLE orders( customer_id int REFERENCES customers,
                     delivery_address int REFERENCES addresses,
                     price real,
                     id serial PRIMARY KEY );

CREATE TABLE ordered_items( order_id int REFERENCES orders,
                            item_id int REFERENCES items,
                            id serial PRIMARY KEY );

CREATE TABLE recipes( item_id int REFERENCES items,
                      ingredient_id int REFERENCES ingredients,
                      amount_of_ingredient real,
                      id serial PRIMARY KEY );


-- Returns all players's IDs and their number of wins, ordered from most wins to least
-- CREATE VIEW num_wins AS
--     SELECT players.id, count(matches.winner) AS num
--     FROM players LEFT JOIN matches
--                            ON players.id = winner
--     GROUP BY players.id
--     ORDER BY num DESC;

-- -- Returns all players's IDs and their number of losses, ordered from most losses to least
-- CREATE VIEW num_losses AS
--     SELECT players.id, count(matches.loser) AS num
--     FROM players LEFT JOIN matches
--                            ON players.id = loser
--     GROUP BY players.id
--     ORDER BY num DESC;

-- -- Returns all players's IDs and their number of matches, ordered from most matches to least
-- CREATE VIEW num_matches AS
-- 	SELECT players.id, (num_wins.num + num_losses.num) AS num
-- 	FROM players LEFT JOIN num_wins
-- 	                       ON players.id = num_wins.id
-- 	             LEFT JOIN num_losses
-- 	                       ON players.id = num_losses.id
-- 	ORDER BY num DESC;

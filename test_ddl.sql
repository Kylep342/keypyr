DROP SCHEMA IF EXISTS keypyr CASCADE;

CREATE SCHEMA IF NOT EXISTS keypyr;

CREATE TABLE keypyr.people(
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(16) NOT NULL,
  last_name VARCHAR(32) NOT NULL,
  address VARCHAR(255),
  home_state VARCHAR(2),
  dob DATE
)
;

CREATE TABLE keypyr.states(
  abbrev VARCHAR(2) PRIMARY KEY,
  full_name VARCHAR(16),
  capital VARCHAR(32),
  largest_city VARCHAR(32),
  population INTEGER,
  area_sq_mi INTEGER,
  date_of_admission DATE,
  governor VARCHAR(32),
  state_flower VARCHAR(32),
  state_tree VARCHAR(32),
  state_bird VARCHAR(32),
  state_motto TEXT
)
;

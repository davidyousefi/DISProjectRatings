CREATE TABLE IF NOT EXISTS Titles(
    title VARCHAR (200)
);

copy Titles(title)
from 'C:PATH\data\NetflixTitles.csv'
CSV HEADER;

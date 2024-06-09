CREATE TABLE Titles_Ratings (
    title VARCHAR(200),
    rating REAL DEFAULT 0.0
);

INSERT INTO Titles_Ratings (title, rating)
SELECT title, 0.0
FROM titles;
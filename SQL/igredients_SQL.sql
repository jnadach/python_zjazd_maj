CREATE TABLE Igrredients (
    Igrredient_Id INT IDENTITY PRIMARY KEY,
    Names NVARCHAR(255) NOT NULL UNIQUE,
    Calories FLOAT NOT NULL,
    Proteins FLOAT NOT NULL,
    Fats FLOAT NOT NULL,
    Carbs FLOAT NOT NULL,
    Fibers FLOAT NOT NULL,
    Igrredient_Types NVARCHAR(100) NOT NULL
)

INSERT INTO Igrredients (Names, Calories, Proteins, Fats, Carbs, Fibers, Igrredient_Types)
VALUES ('Bułeczki do hot-dogów',341,9.50,7.50,59.8,1.8,'BREAD')

SELECT * FROM Igrredients
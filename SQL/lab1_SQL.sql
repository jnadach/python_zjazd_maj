-- 1. Wyświetl wszystkie kolumny z tabeli Produktów [Production.Product]
SELECT *  FROM Production.Product

-- 2. Wyświetl kolumny ProductID, Name i ListPrice dla wszystkich produktów [Production.Product]
SELECT
    ProductID,
    Name,
    ListPrice
FROM Production.Product

-- 3. Wyświetl kolumny ProductID, Name i ListPrice dla wszystkich produktów w porządku
-- malejącym według ListPrice [Production.Product]
SELECT
    ProductID,
    Name,
    ListPrice
FROM Production.Product
ORDER BY ListPrice DESC

-- 4. Wyświetl kolumny Name, StandardCost i ListPrice dla wszystkich produktów, których ListPrice
-- jest większa lub równa 500 [Production.Product]
SELECT
     Name,
     StandardCost,
     ListPrice
FROM Production.Product
WHERE ListPrice >= 500

-- 5. Wyświetl kolumny Name i Color dla wszystkich produktów, które mają kolor „Red”,
-- porządkowane według nazwy [Production.Product]
SELECT
    Name,
    Color
FROM Production.Product
WHERE Color = 'Red'

-- 6. Wyświetl kolumny FirstName, LastName i MiddleName dla wszystkich osób, uporządkowane
-- według LastName, a następnie FirstName [Person.Person]
SELECT
    FirstName,
    LastName,
    MiddleName
FROM Person.Person
ORDER BY  LastName, FirstName

-- 7. Wyświetl kolumny BusinessEntityID, HireDate i JobTitle dla wszystkich pracowników
-- posiadających JobTitle „Sales Representative”, uporządkowany według BusinessEntityID, a
-- następnie HireDate [HumanResources.Employee]
SELECT
    BusinessEntityID,
    HireDate,
    JobTitle
FROM HumanResources.Employee
WHERE JobTitle = 'Sales Representative'
ORDER BY BusinessEntityID, HireDate

-- 8. Wyświetl kolumny Name i ListPrice dla wszystkich produktów, które mają a ListPrice między
-- 500 a 1000, uporządkowane według ListPrice [Production.Product]
SELECT
     Name,
     ListPrice
FROM Production.Product
WHERE ListPrice BETWEEN 500 AND 1000
ORDER BY ListPrice

-- 9. Wyświetl kolumny Name, Color i Size dla wszystkich produktów które mają kolor „Black” i
-- rozmiar „M”, uporządkowane według Name [Production.Product]
SELECT
    Name,
    Color,
    Size
FROM Production.Product
WHERE Color = 'Black' AND Size = 'M'
ORDER BY Name

-- 10. Wyświetl kolumny BusinessEntityID i HireDate dla wszystkich pracowników zatrudnionych w
-- 2010 r., uporządkowane według HireDate [HumanResources.Employee]
SELECT
    BusinessEntityID,
    HireDate
FROM HumanResources.Employee
WHERE HireDate LIKE '2010%'
ORDER BY HireDate

-- 11. Wybierz wszystkich klientów z Niemiec i posortuj ich według PersonID. (2 zapytania)
-- [Sales.Customer]
SELECT
    TerritoryID,
    Name
FROM Sales.SalesTerritory
WHERE Name = 'Germany'

SELECT *
FROM Sales.Customer
WHERE TerritoryID = 8
ORDER BY PersonID

-- 12. Wybierz produkty z kategorii "Components" i posortuj je według nazwy. (3 zapytania)
-- [Production.Product]
SELECT ProductCategoryID, Name
FROM Production.ProductCategory
WHERE Name = 'Components'

SELECT DISTINCT ProductCategoryID, ProductSubcategoryID
FROM Production.ProductSubcategory
WHERE ProductCategoryID = 2

SELECT *
FROM Production.Product
WHERE ProductSubcategoryID BETWEEN 4 AND 17

-- 13. Wybierz pracowników zatrudnionych w okresie od 1 stycznia 2005 do 31 grudnia 2006 i
-- posortuj ich według daty zatrudnienia. [HumanResources.Employee]
SELECT *
FROM HumanResources.Employee
WHERE HireDate BETWEEN '2005-01-01' AND '2006-12-31'

-- 14. Wybierz zamówienia od klienta o identyfikatorze 29485 i posortuj je według daty zamówienia
-- malejąco. [Sales.SalesOrderHeader]
SELECT *
FROM Sales.SalesOrderHeader
WHERE CustomerID = 29485
ORDER BY OrderDate DESC

-- 15. Wybierz wszystkie zamówienia, które mają metodę dostawy "OVERSEAS - DELUXE" lub
-- "CARGO TRANSPORT 5" i posortuj je według daty wysyłki. (2 zapytania)
-- [Sales.SalesOrderHeader]
SELECT ShipMethodID, Name
FROM Purchasing.ShipMethod
WHERE Name IN ('OVERSEAS - DELUXE', 'CARGO TRANSPORT 5')

SELECT *
FROM Sales.SalesOrderHeader
WHERE ShipMethodID IN (3, 5)
ORDER BY OrderDate

-- 16. Wybierz wszystkie produkty o nazwie zawierającej słowo "bike" i posortuj je według nazwy w
-- porządku rosnącym.[Production.Product]
SELECT *
FROM Production.Product
WHERE Name LIKE '%bike%'
ORDER BY Name



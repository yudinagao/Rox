# Dicionário de dados

Os seguintes arquivos deveram ser importados para o banco de dados:

- Sales.SpecialOfferProduct.csv
    - SpecialOfferID - INT NOT NULL
    - Product ID - INT NOT NULL
    - Rowguid - VARCHAR
    - ModifiedDate - TimeStamp


- Production.Product.csv
    - ProductID - INT NOT NULL
    - Name - Varchar
    - ProductNumber - Varchar
    - MakeFlag - Bool
    - FinishedGoodFlag - Bool
    - Color - VarChar
    - SafetyStockLevel - INT
    - ReorderPoint - INT
    - StandardCost - float
    - ListPrice - float
    - Size - Varchar
    - SizeMeasureCode - varchar
    - WeightUnitMeasureCode - varchar
    - Weight - float
    - DaysToManufacture - INT
    - ProductLine - Varchar
    - Class - Varchar
    - Style - Varchar
    - ProductSubcategoryID - INT
    - ProductModelID
    - SellStartDate - timestamp
    - SellEndDate - timestamo
    - DiscontinuedDate - NuLL
    - rowGuid - varchar
    - ModifiedDate - timestamp

- Sales.SalesOrderHeader.csv
    - Row - INT
    - RevisionNumber - INT
    - OrderDate - TimeStamp
    - DueDate - Timestamp
    - ShipDate - Timestamp
    - Status - int
    - OnlineOrderFlag - Bool
    - SalesOrderNumber - Varchar
    - PurchaseOrderNumber - Varchar
    - AccountNumber - Varchar
    - CustomerID - INT
    - SalesPersonID - INT
    - TerritoryID - INT
    - BillToAddressID - INT
    - ShipToAddress - INT
    - ShipMethodID - INT
    - CreditCardID - INT
    - CreditCardApprovalCode - Varchar
    - CurrencyRateID - INT
    - SubTotal - float
    - TaxAmt - float
    - Freight - float
    - TotalDue - float
    - Comment - Varchar
    - rowguid - Varchar
    - ModifiedDate - timestamp

- Sales.Customer.csv
    - CustomerID - INT NOT NULL
    - PersonID - INT
    - StoreID - INT
    - TerritoryID - INT
    - rowguid - Varchar
    - ModifiedDate - Timestamp

- Person.Person.csv
    - BusinessEntityID - INT
    - PersonType - Varchar
    - NameStyle - int
    - Title - Varchar
    - FirstName - Varchar
    - MiddleName - Varchar
    - LastName - Varchar
    - Suffix - Varchar
    - EmailPromotion - INT
    - AdditionalContactInfo - Varchar
    - Demographics - Varchar
    - rowguid - Varchar
    - ModifiedDate - TimeStamp

- Sales.SalesOrderDetail.csv
    - SalesOrderID - INT
    - SaledOrderDetail - INT
    - CArrierTrackingNumber - Varchar
    - OrderQty - INT
    - SpecialOrderID - INT
    - UnitPrice - float
    - UnitPriceDIscount - float
    - LineTotal - float
    - rowguid - Varchar
    - ModifiedDate
CREATE FUNCTION dbo.fn_GetHighValueOrderss (@MinAmount DECIMAL(10,2))
RETURNS TABLE
AS
RETURN (
    SELECT OrderID, CustomerName, OrderAmount
    FROM dbo.Orderss
    WHERE OrderAmount >= @MinAmount
);
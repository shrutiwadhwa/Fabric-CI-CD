CREATE FUNCTION dbo.fn_GetHighValueOrders (@MinAmount DECIMAL(10,2))
RETURNS TABLE
AS
RETURN (
    SELECT OrderID, CustomerName, OrderAmount
    FROM dbo.Orders
    WHERE OrderAmount >= @MinAmount
);
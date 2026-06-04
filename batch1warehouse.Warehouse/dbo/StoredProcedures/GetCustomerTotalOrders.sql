create PROCEDURE dbo.GetCustomerTotalOrders
    @CustomerName VARCHAR(100),
    @TotalAmount DECIMAL(10,2) OUTPUT
AS
BEGIN
    SELECT @TotalAmount = SUM(OrderAmount)
    FROM dbo.Orders
    WHERE CustomerName = @CustomerName;
END;
CREATE FUNCTION dbo.fn_ApplyDiscount (@Amount DECIMAL(10,2))
RETURNS TABLE
AS
RETURN (
    SELECT @Amount * 0.90 AS DiscountedAmount
);
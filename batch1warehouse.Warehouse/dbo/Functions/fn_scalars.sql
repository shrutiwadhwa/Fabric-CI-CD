create function dbo.fn_scalars(
@Amount DECIMAL(10,2)
)
RETURNS DECIMAL(10,2)
AS
BEGIN
    RETURN @Amount * 0.90;
END;
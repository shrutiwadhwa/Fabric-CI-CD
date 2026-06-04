CREATE TABLE [shruti].[Customer-Clone] (

	[CustomerID] int NULL, 
	[FirstName] varchar(50) NULL, 
	[LastName] varchar(50) NULL, 
	[Email] varchar(100) NULL, 
	[DateOfBirth] datetime2(6) NULL, 
	[IsActive] bit NULL, 
	[CreatedAt] datetime2(6) NULL, 
	[LoyaltyPoints] decimal(10,2) NULL, 
	[CountryCode] char(2) NULL, 
	[Remarks] varchar(100) NULL
);
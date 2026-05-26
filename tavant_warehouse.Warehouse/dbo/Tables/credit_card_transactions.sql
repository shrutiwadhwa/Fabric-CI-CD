CREATE TABLE [dbo].[credit_card_transactions] (

	[transaction_id] int NULL, 
	[transaction_ts] datetime2(6) NULL, 
	[card_number] varchar(16) NULL, 
	[merchant_id] varchar(10) NULL, 
	[amount] decimal(10,2) NULL, 
	[currency] varchar(5) NULL, 
	[channel] varchar(20) NULL, 
	[last_updated_ts] datetime2(6) NULL
);
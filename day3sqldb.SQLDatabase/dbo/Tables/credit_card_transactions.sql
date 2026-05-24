CREATE TABLE [dbo].[credit_card_transactions] (
    [transaction_id]  INT             NOT NULL,
    [transaction_ts]  DATETIME        NULL,
    [card_number]     VARCHAR (16)    NULL,
    [merchant_id]     VARCHAR (10)    NULL,
    [amount]          DECIMAL (10, 2) NULL,
    [currency]        VARCHAR (5)     NULL,
    [channel]         VARCHAR (20)    NULL,
    [last_updated_ts] DATETIME        NULL,
    PRIMARY KEY CLUSTERED ([transaction_id] ASC)
);


GO


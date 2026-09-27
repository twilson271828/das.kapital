
-- This function computes the net imbalance of executed trades at each event timestamp, providing insights into the market sentiment and potential price movements.
CREATE OR REPLACE FUNCTION get_trade_volume_imbalance()
RETURNS TABLE (
    ts_event TIMESTAMP,
    buy_volume NUMERIC,
    sell_volume NUMERIC,
    net_imbalance NUMERIC
) AS $$ 
BEGIN
    RETURN QUERY
    SELECT 
        m.ts_event,
        -- Accumulate the labor of the buyers
        COALESCE(SUM(CASE WHEN m.side = 'B' THEN m.size ELSE 0 END), 0) AS buy_volume,
        -- Accumulate the labor of the sellers
        COALESCE(SUM(CASE WHEN m.side = 'A' THEN m.size ELSE 0 END), 0) AS sell_volume,
        -- Compute the dialectical contradiction (Net Imbalance)
        (COALESCE(SUM(CASE WHEN m.side = 'B' THEN m.size ELSE 0 END), 0) - 
         COALESCE(SUM(CASE WHEN m.side = 'A' THEN m.size ELSE 0 END), 0)) AS net_imbalance
    FROM mes m
    -- We filter strictly for executed trades
    WHERE m.action = 'T'
    GROUP BY m.ts_event
    ORDER BY m.ts_event ASC;
END;

- This function computes the net imbalance of executed trades at each event timestamp, providing insights into the market sentiment and potential price movements.
CREATE OR REPLACE FUNCTION get_trade_volume_imbalance()
RETURNS TABLE (
    ts_event TIMESTAMP,
    buy_volume NUMERIC,
    sell_volume NUMERIC,
    net_imbalance NUMERIC
) AS $$ 
BEGIN
    RETURN QUERY
    SELECT 
        m.ts_event,
        -- Accumulate the labor of the buyers
        COALESCE(SUM(CASE WHEN m.side = 'B' THEN m.size ELSE 0 END), 0) AS buy_volume,
        -- Accumulate the labor of the sellers
        COALESCE(SUM(CASE WHEN m.side = 'A' THEN m.size ELSE 0 END), 0) AS sell_volume,
        -- Compute the dialectical contradiction (Net Imbalance)
        (COALESCE(SUM(CASE WHEN m.side = 'B' THEN m.size ELSE 0 END), 0) - 
         COALESCE(SUM(CASE WHEN m.side = 'A' THEN m.size ELSE 0 END), 0)) AS net_imbalance
    FROM mes m
    -- We filter strictly for executed trades
    WHERE m.action = 'T'
    GROUP BY m.ts_event
    ORDER BY m.ts_event ASC;
END;

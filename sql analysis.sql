--Conversion rate by test group
SELECT 
"test group",
COUNT(*) AS total_users,
SUM(CASE WHEN converted = true THEN 1 ELSE 0 END) AS conversions,
ROUND(100.0 * SUM(CASE WHEN converted = true THEN 1 ELSE 0 END) / COUNT(*), 2) AS conversion_rate
FROM testing
GROUP BY "test group";

--Overall conversion rate
SELECT
    COUNT(*) AS total_users,
    SUM(CASE WHEN converted = true THEN 1 ELSE 0 END) AS total_conversions,
    ROUND(
        100.0 * SUM(CASE WHEN converted = true THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS overall_conversion_rate
FROM testing;

--Conversion rate by day
SELECT
    "most ads day",
    COUNT(*) AS total_users,
    SUM(CASE WHEN converted = true THEN 1 ELSE 0 END) AS conversions,
    ROUND(
        100.0 * SUM(CASE WHEN converted = true THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS conversion_rate
FROM testing
GROUP BY "most ads day"
ORDER BY conversion_rate DESC;

-- Conversion rate by hour
SELECT
    "most ads hour",
    COUNT(*) AS total_users,
    SUM(CASE WHEN converted = true THEN 1 ELSE 0 END) AS conversions,
    ROUND(
        100.0 * SUM(CASE WHEN converted = true THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS conversion_rate
FROM testing
GROUP BY "most ads hour"
ORDER BY conversion_rate DESC;

--Ad exposure analysis
SELECT
    CASE
        WHEN "total ads" <= 10 THEN '0-10 ads'
        WHEN "total ads" <= 50 THEN '11-50 ads'
        WHEN "total ads" <= 100 THEN '51-100 ads'
        ELSE '100+ ads'
    END AS exposure,
    COUNT(*) AS total_users
FROM testing
GROUP BY
    CASE
        WHEN "total ads" <= 10 THEN '0-10 ads'
        WHEN "total ads" <= 50 THEN '11-50 ads'
        WHEN "total ads" <= 100 THEN '51-100 ads'
        ELSE '100+ ads'
    END;
/* Write your T-SQL query statement below */
WITH rating_by_user AS (
    SELECT TOP 1 u.name as results
    FROM Users u JOIN MovieRating r ON u.user_id = r.user_id
    GROUP BY u.name
    ORDER BY COUNT(r.movie_id) DESC, u.name
),
rating_by_movie AS (
    SELECT TOP 1 m.title as results
    FROM MovieRating r JOIN Movies m ON r.movie_id = m.movie_id
    WHERE r.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY m.title
    ORDER BY AVG(CAST(r.rating AS FLOAT)) DESC, m.title
)
SELECT * FROM rating_by_user
UNION ALL
SELECT * FROM rating_by_movie

-- כי ככה אסור בSQL: לעשות ORDER BY באופרנדים של UNION
-- (
--     SELECT TOP 1 u.name as results
--     FROM Users u JOIN MovieRating r ON u.user_id = r.user_id
--     GROUP BY u.name
--     ORDER BY COUNT(r.movie_id) DESC, u.name ASC
-- )
-- UNION
-- (
--     SELECT TOP 1 m.title
--     FROM MovieRating r JOIN Movies m ON r.movie_id = m.movie_id
--     GROUP BY m.title
--     ORDER BY AVG(r.rating) DESC
-- )

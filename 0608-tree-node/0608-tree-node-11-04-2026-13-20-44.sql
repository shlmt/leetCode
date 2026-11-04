/* Write your T-SQL query statement below */
SELECT DISTINCT t.id,
    CASE
        WHEN p.id IS NULL THEN 'Root'
        WHEN s.id IS NULL THEN 'Leaf'
        ELSE 'Inner' END
    as 'Type'
FROM Tree p RIGHT JOIN Tree t ON p.id = t.p_id LEFT JOIN Tree s ON t.id = s.p_id 
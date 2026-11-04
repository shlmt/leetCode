/* Write your T-SQL query statement below */
SELECT DISTINCT ot.id,
    CASE
        WHEN ot.p_id IS NULL THEN 'Root'
        WHEN NOT EXISTS(SELECT 1 FROM Tree it WHERE it.p_id = ot.id) THEN 'Leaf'
        ELSE 'Inner' END
    as 'type'
FROM Tree ot
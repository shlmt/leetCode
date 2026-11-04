/* Write your T-SQL query statement below */
SELECT DISTINCT ot.id,
    CASE
        WHEN NOT EXISTS(SELECT it.id FROM Tree it WHERE ot.p_id = it.id) THEN 'Root'
        WHEN NOT EXISTS(SELECT it.p_id FROM Tree it WHERE it.p_id = ot.id) THEN 'Leaf'
        ELSE 'Inner' END
    as 'type'
FROM Tree ot
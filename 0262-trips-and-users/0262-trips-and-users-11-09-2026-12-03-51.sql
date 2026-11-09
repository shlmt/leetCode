/* Write your T-SQL query statement below */
SELECT t.request_at as 'Day', CAST(SUM(CASE WHEN t.status != 'completed' THEN 1 ELSE 0 END)*1.0 / COUNT(*) AS DECIMAL(10,2)) as 'Cancellation Rate'
FROM Trips t JOIN Users u ON t.client_id = u.users_id JOIN Users drivers ON t.driver_id = drivers.users_id
WHERE u.banned = 'No' AND drivers.banned = 'No' AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at
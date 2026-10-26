/* Write your T-SQL query statement below */
SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE activity_date BETWEEN DATEADD(DAY, -29, '2019-07-27') AND '2019-07-27' AND activity_type IN ('open_session', 'end_session', 'scroll_down', 'send_message')
GROUP BY activity_date
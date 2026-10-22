CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        SELECT salary
        FROM (
            SELECT salary, ROW_NUMBER() OVER(ORDER BY salary DESC) as rn
            FROM Employee
            GROUP BY salary
        ) as t
        WHERE rn = @N
    );
END
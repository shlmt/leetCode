/* Write your T-SQL query statement below */

select lastName,firstName, city, state
from Address a right join Person p on p.personId=a.personId
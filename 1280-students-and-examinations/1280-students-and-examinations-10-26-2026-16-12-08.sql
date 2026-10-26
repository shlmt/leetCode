/* Write your T-SQL query statement below */
SELECT st.student_id, st.student_name, sub.subject_name, COUNT(e.student_id) as attended_exams
FROM Students st CROSS JOIN Subjects sub LEFT JOIN Examinations e ON sub.subject_name = e.subject_name AND st.student_id = e.student_id
GROUP BY st.student_id, st.student_name, sub.subject_name
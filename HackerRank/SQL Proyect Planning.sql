/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/


WITH ProjectsCTE AS
( 
SELECT p.Task_ID, 0 AS Child_task, p.Start_Date, p.End_Date
FROM Projects p
    
UNION ALL
--recursive select
SELECT s.Task_ID, a.Task_ID AS Child_task, a.Start_Date, a.End_Date
FROM Projects a
INNER JOIN ProjectsCTE s ON a.Start_Date = s.End_Date
)

SELECT Project_Start_Date, Proyect_End_Date
FROM(
    SELECT DISTINCT Task_ID, min(Start_Date) AS Project_Start_Date, max(End_Date) AS Proyect_End_Date
    FROM ProjectsCTE
    WHERE Task_ID NOT IN (SELECT Child_task 
                          FROM ProjectsCTE)
    GROUP BY Task_ID
) A
ORDER BY DATEDIFF(day, Proyect_End_Date, Project_Start_Date) DESC, Project_Start_Date





-- select * from projects;
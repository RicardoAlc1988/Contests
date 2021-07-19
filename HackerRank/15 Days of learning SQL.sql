/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/ 

WITH SubmissionsCTE AS
( 
SELECT p.submission_date, p.hacker_id, 1 as level
FROM Submissions p
WHERE p.submission_date = '2016-03-01'
    
UNION ALL
--recursive select
SELECT c.submission_date, c.hacker_id, p.level+1 as level
FROM Submissions c
INNER JOIN SubmissionsCTE p ON c.hacker_id = p.hacker_id
where c.submission_date = dateadd(day, 1, p.submission_date)
)

select L.submission_date, L.num_hackers, M.hacker_id, M.name
from
(
select submission_date, count(distinct hacker_id) as num_hackers
from SubmissionsCTE 
group by submission_date) L
inner join (
    select F.submission_date, F.hacker_id, H.name
    from (
        select E.submission_date, min(E.hacker_id) as hacker_id, E.num_submissions
        from (
            select B.submission_date, B.hacker_id, B.num_submissions
            from (
                select C.submission_date, max(C.num_submissions) as num_submissions
                from (
                    select s.submission_date, s.hacker_id, count(s.submission_id) as num_submissions
                    from Submissions s
                    group by s.submission_date, s.hacker_id
                ) C
                group by C.submission_date
            ) A INNER JOIN 
                (select s.submission_date, s.hacker_id, count(s.submission_id) as num_submissions
                      from Submissions s
                      group by s.submission_date, s.hacker_id
            ) B ON A.submission_date = B.submission_date AND A.num_submissions = B.num_submissions) E
        group by E.submission_date, E.num_submissions
    ) F inner join Hackers H on F.hacker_id = H.hacker_id) M on L.submission_date = M.submission_date
order by L.submission_date
    
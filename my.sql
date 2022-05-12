use mydb

--ques 1
select count(Sr_No)
from startup
where city = 'Pune';

--ques 2
select count(Sr_No) 
from startup 
where Investmentntype = 'Seed / Angel Funding';

--ques 3
select sum(Amount_in_USD) 
from ( 
    SELECT * 
    from startup 
    where IFNULL(Amount_in_USD, '') REGEXP '0' 
    ) as my
where city = 'Pune';

--ques 4
SELECT Industry_Vertical, count(Industry_Vertical) 
from startup 
group by Industry_Vertical 
order by count(Industry_Vertical) desc 
limit 5;

--ques 5
select Investors_Name,year(Date) 
from startup 
group by YEAR(Date) 
order by Amount_in_USD;



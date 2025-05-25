(select city,LENGTH(city) from station 
where length(city) = (select min(length(city)) from station)
order by city asc 
limit 1)
union
(select city,LENGTH(city) from station 
where length(city) = (select max(length(city)) from station)
order by city asc 
limit 1
)
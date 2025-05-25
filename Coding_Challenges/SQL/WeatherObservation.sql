/*

Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths 
(i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

*/
select city,LENGTH(city) from station 
where length(city) = (select min(length(city)) from station)
order by city asc 
fetch first 1 Row only;
select city, LENGTH(city) from station 
where length(city) = (select max(length(city)) from station)
order by city asc 
fetch first 1 Row only;


/*
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
*/

select distinct city from station
where lower(substr(city,1,1)) in ('a','e','i','o','u');

/*
Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

*/

select distinct city from station
where lower(substr(city,length(city),1)) in ('a','e','i','o','u');
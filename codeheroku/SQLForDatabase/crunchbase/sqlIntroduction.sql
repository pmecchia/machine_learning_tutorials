--SELECT * FROM companies

SELECT name,city,category_code from companies

SELECT name AS company_name FROM companies

SELECT name AS company_name,city as City,category_code from companies

SELECT * FROM companies LIMIT 20

--Find companies where status is operating
SELECT *  FROM companies
 WHERE STATUS = 'operating'

--Find where funding_total is NULL
SELECT *  FROM companies
 WHERE funding_total_usd IS NULL


--Find companies' name starting with 'a'
SELECT *  FROM companies
 WHERE name > 'a'

-- Convert funding_total_usd in INR
SELECT funding_total_usd*69.09 as FUNDIG_INR  FROM companies

--Create a new column which concatenate Region and city
SELECT region || "/" || city as 'Region/City' FROM companies

--Find names which start with '.'
SELECT * FROM Companies WHERE name like '.%'

--Find 5 lowest funding companies
SELECT  *  from companies WHERE funding_total_usd is not NULL order by funding_total_usd ASC limit 5

--Find all unique categories
SELECT DISTINCT(category_code) as "dist categories" from companies WHERE category_code is NOT NULL

--Count all unique categories
SELECT count(DISTINCT(category_code) )as "dist categories" from companies WHERE category_code is NOT NULL

--Find average funding amount for all companies rounded to 2 decimal places(NULL values=0)
SELECT round(avg(coalesce(funding_total_usd,0)),2) as 'Average fundind' from companies

--Display the same without decimal point
SELECT cast ( avg(coalesce(funding_total_usd,0)) as int ) + ( avg(coalesce(funding_total_usd,0)) > cast ( avg(coalesce(funding_total_usd,0)) as int ))as 'Average fundind' from companies

-- Decrease average number of funding rounds by category_code
	--Replace the null with 'Unknown'
SELECT coalesce(category_code,'Unknown'),avg(funding_rounds) as 'Average fundind' from companies GROUP BY category_code ORDER By funding_rounds DESC

-- Found count of companies founded each year
SELECT strftime('%Y',founded_at) as year_founded, count(founded_at) as count_companies from companies  
GROUP by year_founded order by count_companies DESC

-- Display all years, umber of companies founded if number of companies >10
SELECT strftime('%Y',founded_at) as year_founded, count(founded_at) as count_companies from companies  
GROUP by year_founded HAVING count_companies>10 order by count_companies DESC

--Multiple Tables: Display all companies with their founded_at date which got acquired after 2012
	--subquery & joins
	--count number of acquissitions made by each company
SELECT name, count(company_name) from companies
JOIN acquisitions on permalink=acquirer_permalink
GROUP By name



select * from dbo.Sales
where TotalAmount>=161

select * from dbo.Sales

select productid, sum(totalamount) [Sum of sales] from dbo.Sales
group by ProductID
having sum(totalamount)<700

select productid,sum(totalamount) [Sum of sales] from dbo.Sales
where TotalAmount>=161
group by productid
having sum(totalamount)>=250
order by PRODUCTid desc

select productid,sum(totalamount) [Sum of sales] from dbo.Sales
where TotalAmount>=161
group by productid
having sum(totalamount)>=250
order by sum(totalamount) asc

/*WHERE filters individual rows before GROUP BY, so it works on raw data and cannot use 
aggregates like SUM() or COUNT().
HAVING filters the grouped results after GROUP BY, so it is used with aggregate functions 
to keep or remove entire groups.can be use aggregates like SUM() or COUNT*/


--Nested case--

Select * from Products

--We need to group the data based on columns category & price into different categories i.e affordable & premium

Select
*,
case
	when Category = 'Electronics' then
	case
		when Price >=100 then 'Premium'
		else 'Affordable'
	end
	
	when Category = 'Furniture' then
	case
		when Price >=120 then 'Premium'
		else 'Affordable'
	end

	when Category ='Accessories' then
	Case
		when Price >=35 then 'Premium'
		else 'Affordable'
	end
end as [Category]
from Products

----Test
Select
*,
case
	when Category = 'Electronics' then
	case
		when Price >=100 then 'Premium'
		else 'Affordable'
	end
	
	when Category = 'Furniture' then
	case
		when Price >=120 then 'Premium'
		else 'Affordable'
	end

	when Category ='Accessories' then
	Case
		when Price >=35 then 'Premium'
		else 'Affordable'
	end
end as [Category]
from Products

-- use = or in() both work in a same way

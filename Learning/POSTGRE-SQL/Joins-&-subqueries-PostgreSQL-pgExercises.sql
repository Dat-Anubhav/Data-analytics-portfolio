--Q1:- You'd like to get the signup date of your last member. How can you retrieve this information?
Select joindate from cd.members order by memid DESC limit 1;

--Q2:- You'd like to get the first and last name of the last member(s) who signed up - not just the date. How can you do that?
Select firstname,surname,joindate from cd.members order by memid DESC limit 1;

--Q3:- How can you produce a list of the start times for bookings by members named 'David Farrell'?
Select starttime from cd.bookings bks inner join cd.members mem on bks.memid=mem.memid
where mem.firstname='David' and mem.surname='Farrell';

--Q4:- How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.
Select bks.starttime as start,fac.name as name 
from cd.bookings bks inner join cd.facilities fac 
on bks.facid=fac.facid
where bks.starttime>='2012-09-21' and bks.starttime<'2012-09-22' and fac.name LIKE 'Tennis%' 
order by bks.starttime;

Select firstname from cd.members;
Select recommendedby from cd.members;

-- Q5:- How can you output a list of all members who have recommended another member? 
--Ensure that there are no duplicates in the list, and that results are ordered by (surname, firstname).
Select distinct a.firstname as firstname,a.surname as surname from cd.members a inner join cd.members b on a.memid=b.recommendedby
order by surname,firstname;

-- Q6:- How can you output a list of all members, including the individual who recommended them (if any)? 
--Ensure that results are ordered by (surname, firstname).
Select a.firstname as memfname,a.surname as memsname,b.firstname as recfname,b.surname as recsname 
from cd.members a left outer join cd.members b on b.memid=a.recommendedby
order by memsname,memfname;

-- Q7:- How can you produce a list of all members who have used a tennis court? 
--Include in your output the name of the court, and the name of the member formatted as a single column. 
--Ensure no duplicate data, and order by the member name followed by the facility name.
Select mem.firstname ||' '|| mem.surname as member, fac.name as facility 

from cd.members mem inner join cd.bookings bks on mem.memid=bks.memid

inner join cd.facilities fac on bks.facid=fac.facid
where fac.name like 'Tennis%'
order by member,facility;

-- Q8:-How can you produce a list of bookings on the day of 2012-09-14 
--which will cost the member (or guest) more than $30? 
--Remember that guests have different costs to members (the listed costs are per half-hour 'slot'),
--and the guest user is always ID 0. Include in your output the name of the facility, 
--the name of the member formatted as a single column, and the cost. 
--Order by descending cost, and do not use any subqueries.
Select mem.firstname ||' '|| mem.surname as member, fac.name as facility,

case when mem.memid=0 then bks.slots*fac.guestcost
else bks.slots*fac.membercost
end as cost

from cd.members as mem inner join cd.bookings bks on mem.memid=bks.memid
inner join cd.facilities fac on bks.facid=fac.facid

where starttime>='2012-09-14' and starttime<'2012-09-15'
and ((mem.memid=0 and bks.slots*fac.guestcost>30) or mem.memid!=0 and bks.slots*fac.membercost>30)

order by cost DESC;

--Q9:- How can you output a list of all members, including the individual 
--who recommended them (if any), without using any joins? 
--Ensure that there are no duplicates in the list, 
--and that each firstname + surname pairing is formatted as a column and ordered.
Select distinct mem.firstname ||' '|| mem.surname as member,
(Select rec.firstname ||' '|| rec.surname as recommender from cd.members rec
	where rec.memid=mem.recommendedby)
from cd.members mem
order by member;
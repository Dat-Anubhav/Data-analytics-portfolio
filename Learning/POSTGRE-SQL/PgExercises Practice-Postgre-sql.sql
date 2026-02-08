--Q1:- How can you retrieve all the information from the cd.facilities table?
Select * from cd.facilities;

--Q2:- You want to print out a list of all of the facilities and their cost to members. How would you retrieve a list of only facility names and costs?
Select name,membercost from cd.facilities;

--Q3:- How can you produce a list of facilities that charge a fee to members?
Select * from cd.facilities where membercost>0;

--Q4:- How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.
Select facid,name,membercost,monthlymaintenance from cd.facilities where membercost>0 and membercost<(monthlymaintenance/50);

--Q5:- How can you produce a list of all facilities with the word 'Tennis' in their name?
Select * from cd.facilities where name like '%Tennis%'

--Q6:- How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.
Select * from cd.facilities where facid in (1,5);

--Q7:- How can you produce a list of facilities, with each labelled as 'cheap' or 'expensive' depending on if their monthly maintenance cost is more than $100? Return the name and monthly maintenance of the facilities in question.
Select name,
case when (monthlymaintenance>100) then 'expensive'
else 'cheap'
end as cost
from cd.facilities;

--Q8:- How can you produce a list of members who joined after the start of September 2012? Return the memid, surname, firstname, and joindate of the members in question.
Select memid,firstname,joindate from cd.members where joindate >= '2012-09-01'

--Q9:- How can you produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.
Select distinct surname from cd.members order by surname limit 10;

--Q10:- You, for some reason, want a combined list of all surnames and all facility names. Yes, this is a contrived example :-). Produce that list!
Select surname from cd.members union Select name from cd.facilities;

use Our_employee_details

Select * into #temp1
from [dbo].[Employees]

Select * into ##temp2
from [dbo].[EmployeeRecords]

Select * from #temp1

Select * from ##temp2
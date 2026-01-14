--Testing #temp1 and ##temp2

Select * from #temp1

Select * from ##temp2

--Testing after closing the original session

Select * from #temp1

Select * from ##temp2

/*Local vs Global Temporary tables:-

A local temp table (#temp1) is private: only you (your session) can see and use it, 
like a personal notepad. It disappears when your session ends. 
[not work in other session even if the original session is still active]

A global temp table (##temp1) is public: everyone on the server can access it after you create it, 
like a shared whiteboard. It lasts until your session ends and no one else uses it

[Works in other sessions too only if the original session is active]*/

Select Firstname from #temp1

Select Firstname from ##temp2

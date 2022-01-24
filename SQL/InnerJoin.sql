/*inner join, selects records that have matching values in both tables

example:*/
select Orders.OrderID, Customers.CustomerName, Orders.OrderDate
From Orders
Inner join Customers ON Orders.CustomerID=CUstomers.CustomerID

/*
Inner Join: Returns records that have matching values in both tables
If there are records in the "Order" table that do not have matches in "Customers", these orders will not be shown!


Left Join: Returns all records from the left table, and the matched records from the right table
returns all records from the left table, and the matching records from the right table. The result is 0 records from the right side, if there is no match 

right join: returns all records from the right table, and the matched records from the left table
full join : returns all records when there is a match in either left or right join

*/

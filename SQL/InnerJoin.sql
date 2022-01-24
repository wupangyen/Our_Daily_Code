/*inner join, selects records that have matching values in both tables

example:*/
select Orders.OrderID, Customers.CustomerName, Orders.OrderDate
From Orders
Inner join Customers ON Orders.CustomerID=CUstomers.CustomerID

/*
Inner Join: Returns records that have matching values in both tables

Left Join: Returns all records from the left table, and the matched records from the right table
right join: returns all records from the right table, and the matched records from the left table
full join : returns all records when there is a match in either left or right join

*/

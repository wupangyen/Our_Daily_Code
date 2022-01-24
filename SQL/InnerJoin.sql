inner join, selects records that have matching values in both tables

example:
select Orders.OrderID, Customers.CustomerName, Orders.OrderDate
From Orders
Inner join Customers ON Orders.CustomerID=CUstomers.CustomerID


Inner Join: Returns records that have matching values in both tables

Left Join: Returns all records from the lef

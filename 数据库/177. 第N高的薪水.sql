CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare m int;
set m=N-1;
  RETURN (
      select distinct Salary from Employee  order by Salary desc limit m,1
  );
END

--desc limit n-1,1 的意思是逆序排列从下标为 n-1 的元素开始取1个 。当我们输入 n 为2的时候，第2高的薪水，就要选择一个下标为 1 的属性Salary。
--distinct 使得如果不存在第 n 高的薪水，那么查询应返回 null。
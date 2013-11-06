Point of equilibrium  
================  
input: A 2D array, number in that is weight.  
output: The point of equilibrium  

输入：一个二维数组，数组中的元素代表数组的重量
输出：数组的平衡点

Infect, point of equilibrium means center of gravity. Thus, all need to do is get the weighted arithmetic mean in each direction, row and col.  
实际上平衡点就是重心。也就是说只需要在X方向和Y方向计算加权平均值就可以了。

Interestingly, in Python, we can do that by only 4 lines of code. 
使用Python只需要4行代码

> by CuGBabyBeaR
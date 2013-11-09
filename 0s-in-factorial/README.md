0s in factorial  阶乘末尾的0  
=================  

**Quesiton  问题**  
How many 0s in the end of N!  
n!(n的阶乘)末尾有多少个0？  

**Solution  解法**  
Infact, when multiplying, 0s in the end only can add from 5^n s :
 - 5 s, which is 5^1, add a 0  
 - 25 s, add two 0s  
 - 125 s, add three 0s  
 - 625 s, add four 0s  
 - ...  
 - 5^n s , add n 0s  
Thus, all need to do is find out, between 1 and N, how many of these 5 s.  


实际上，在连乘时，阶乘结果末尾的0只会从5的n次幂中得到： 
 - 5 (5^1), 增加1个0  
 - 25 (5^2), 增加2个0  
 - 125 (5^3), 增加3个0  
 - 625 (5^4), 增加4个0  
 - ...  
 - 5^n, 增加n个0  
我们只要找到这些5的n次方有多少就行了。  

 > 0s-in-factorial.py: CuGBabyBeaR
 > 0s-in-factorial.cpp: CuGBabyBeaR
Matrix Printer 矩阵打印
=======================


Print a 2D array (martix) in different order: clockwise or anti-clockwise spirally, S or Z, N or reversed N   
以顺时针/逆时针向内 S(Z)型 N型/反N型 一个二维矩阵  


S or Z, N or reversed N are easy，but spiral is tricky. The main idea is, build up 4 boundaries, move a boundary once per print, until opposite boundaries meet. Just get the headding of print and boundaries in control.
S型或者N型很好处理，难点在于螺旋形。基本思想是确立四个边界，每打印一条边就移动一次边界,直到相对的边界相遇。控制好打印方向和打印边即可。


        1    2    3    4
      --------------------
        5 |  6    7 |  8   
          |---------|
        9 | 10 | 11 | 12
      --------------|
       13   14   15 | 16
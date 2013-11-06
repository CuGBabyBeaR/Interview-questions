
#Twitter-Puddle
===================
question from: *[I Failed A Twitter Interview][1]*  
问题来自:[《I Failed A Twitter Interview》][2]  
译文:[《我的Twitter技术面试失败了》][3]  
译者:CuGBabyBeaR

##Question 题目简述:  

**Note:*** All the English description of question and logic of solution comes from original author.*   
**注意:** *所有英文的关于问题、算法逻辑的描述都是来自原作者。*

"Consider the following picture:"  
"如下图所示"

![enter image description here][4]

"In this picture we have walls of different heights. This picture is represented by an array of integers, where the value at each index is the height of the wall. The picture above is represented with an array as [2,5,1,2,3,4,7,7,6]."  
"Now imagine it rains. How much water is going to be accumulated in puddles between walls?"  
“在这个图片里我们有不同高度的墙。这个图片由一个整数数组所代表，数组中每个数是墙的高度。上边的图可以表示为数组[2,5,1,2,3,4,7,7,6]”  
“假如开始下雨了，那么墙之间的水坑能够装多少水呢？”  

![enter image description here][5]  
"We count volume in square blocks of 1X1. So in the picture above, everything to the left of index 1 spills out. Water to the right of index 7 also spills out. We are left with a puddle between 1 and 6 and the volume is 10."  
“以1×1的方块为单位计算容积。所以，在上边的图中下标为1以左的都会漏掉。下标7以右的也会漏掉。剩下的只有在1和6之间的一坑水，容积是10”

##Solution  算法逻辑  
If we traverse the list from left to right, the amount of water at each index is at most the largest value we have discovered so far. That means that if we knew for a fact that there is something larger or equal to it somewhere on the right, we would know exactly how much water we can hold without spilling. Same goes for traversing in the opposite direction: if we know we have found something larger on the left than the largest thing on the right, we can safely fill up water.

With this in mind, one solution would be to first find the absolute maximum value, traverse from the left to the maximum, and then traverse from the right to the maximum. This solution does 2 passes: one to find the maximum, and the other is split into two subtraversals.

The solution in one pass (shown in the gist) avoids finding the maximum value by moving two pointers from the opposite ends of the array towards each other. If the largest value found to the left of the left pointer is smaller than the largest value found to the right of the right pointer, then move the left pointer one index to the right. Otherwise move the right pointer one index to the left. Repeat until the two pointers intersect. (This is a wordy explanation, but the code is really simple)

如果我们从左至右遍历列表，每个下标水的量最多是到现在为止最大的数。这表示如果我们已知右边有相等或更大的，我们可以知道存下的水有多少。反向遍历的时候也一样：如果我们知道左边有比右边最大的数更大的，我们装水是毫无问题的。

基于这个想法，一个解决方法是：先找到最大值，从左遍历到最大值，然后从右遍历到最大值。这个方法需要两次遍历：一次找到最大值，另一次分成了两个子遍历。

一次遍历的方法通过两端的指针相向移动避免了寻找最大值。如果（左指针找到的左指针以左的最大值）小于（右指针找到右指针以右的最大值），将左指针向右移动一位。否则右指针向左移动一位。重复过程直到两个指针相遇。（解释起来很麻烦，但是代码很简单）

##About Code  关于代码  
Code including 3 difference test case and test code, 2 of them are from original post.  
代码中有测试代码和3个测试用例。测试用例中的两个来自原作者。

> puddle.py:    CuGBabyBeaR   
> puddle.cpp:   CuGBabyBeaR  
> puddle..java: CuGBabyBeaR  

  [1]: http://qandwhat.apps.runkite.com/i-failed-a-twitter-interview/
  [2]: http://qandwhat.apps.runkite.com/i-failed-a-twitter-interview/
  [3]: http://blog.jobbole.com/50705/
  [4]: http://ww1.sinaimg.cn/mw690/7cc829d3gw1ea56snnnkzj205m03z744.jpg
  [5]: http://ww3.sinaimg.cn/mw690/7cc829d3gw1ea56pjntkoj205m03zaa2.jpg
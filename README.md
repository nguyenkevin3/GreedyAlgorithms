README: 

Name: Kevin Nguyen 

UFID: 93349993 

Prerequisites: Python 

Instructions: 

  1) Open a terminal in the directory where main.py is located. 

  2) Run: python main.py <input file> 

      Ex: python main.py Examples/input_50.in 

  3) Output file ending in .out will be generated in the same location as input file.
______________________________________________________________________________________

(1)
| Input  | k | m | FIFO | LRU | OPTFF |
| ------ | - | - | ---- | --- | ----- |
| File1  | 5 |50 | 42   | 41  | 31    |
| File2  | 5 |100| 69   | 69  | 50    |
| File3  | 5 |150| 114  | 115 | 77    |

OPTFF has the fewest misses. 

FIFO performs roughly the same as LRU. Neither dominates the other all the time. 

______________________________________________________________________________________

(2)

For k = 3, there exists a sequence for which OPTFF incurs strictly fewer misses than LRU or FIFO. 

k = 3, m = 12 

1 2 3 4 2 5 2 1 2 3 4 5 

FIFO: 10 

LRU: 9 

OPTFF: 7 

This sequence is chosen because FIFO and LRU evict pages that are needed soon, 
whereas OPTFF evicts pages whose next use is farthest away.

______________________________________________________________________________________

(3)

Exchange argument:  

At time t, OPTFF and (A) have the same cache contents (full caches) and the same number of misses. 
Let t + 1 be the first instance in which both algorithms evict different items. 

OPTFF evicts x. 

(A) evicts y, which does not equal x. 

OPTFF, by definition, evicts the page whose next usage is farthest in the future. So, x’s next usage >= y’s next usage. 

By modifying (A) to evict x instead of y like OPTFF, without increasing future misses, (A) will evict the page that occurs later 
and keep the page that is used sooner. This is by definition of OPTFF which chose to evict x first. Both algorithms have the same 
cache contents up to time t and are running on the same request sequence. By repeating this transformation each time (A) differs from 
OPTFF without increasing misses, (A) becomes OPTFF. Therefore, OPTFF incurs misses no larger than that of (A) on any fixed sequence. 
 

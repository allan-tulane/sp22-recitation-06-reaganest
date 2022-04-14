 # CMPS 2200 Reciation 6
## Answers

**Name:** Reagan Esteves and Chenyu Zhao


Place all written answers from `recitation-06.md` here for easier grading.


- **1b.**
Comparing the running times to the asymptotic bounds, they are all similar to the asymptotic bounds. From the table, the random pivot can be seen as the best one for both sorted and randomized. Morevoer, both had a increasing trend as the n values increased. The fixed pivot also increased as the n values increased. The only difference was the fixed pivot had larger running times when the n values increased for sorted list.

Based on the tables, the sorted fixed pivot list where the pivot is the first value in the list was less efficient. The randomized qsort fixed pivot compared to the sorted one is much more efficient and the running time was not as large. Comparing the sorted random pivot list and the shuffled one, there is not a distinctive difference between the two. The one small difference is the randomized random pivot had a slightly lower running time compared to the sorted, but the difference is not very big.
Sorted
|   n |   qsort-fixed-pivot |   qsort-random-pivot |
|-----|---------------------|----------------------|
|  25 |               0.312 |                7.579 |
| 100 |               6.780 |                0.759 |
| 200 |              12.096 |                1.745 |
| 300 |              38.341 |               10.940 |
| 400 |              95.690 |                4.126 |
| 500 |             271.703 |                7.709 |
| 600 |             268.204 |                6.029 |
| 700 |             243.969 |               26.163 |
| 800 |             534.147 |               26.163 |
| 900 |             643.443 |               11.843 |

Randomized
|n shuffled |qsort-fixed-pivot    |   qsort-random-pivot |
|-----------|---------------------|----------------------|
|  25       |               0.190 |                0.203 |
| 100       |              11.282 |                1.108 |
| 200       |               1.761 |                2.180 |
| 300       |               3.097 |                3.817 |
| 400       |               4.231 |                5.210 |
| 500       |               5.627 |                5.476 |
| 600       |               7.494 |                8.531 |
| 700       |               9.044 |                9.149 |
| 800       |              70.023 |               10.629 |
| 900       |              10.778 |               10.353 |

- **1c.**
Python uses a sorting algorithm called Timsort, designed by Tim Peters. Com-
pare the fastest of your sorting implementations to the Python sorting function
sorted, conducting the tests in 3b above.

In comparison to the quick-sort algorithms, tim sort performs more efficently. Additionally, the increasing input sizes do make tim sort run slower; however, it is still faster than both quick sort algorithms in both cases. Tim sort is faster when the list is not randomized. Overall, running time for tim sort fixed is halved (nearly) in comparison to shuffled tim sort, but in both cases are better than both quick sorts.

|   n |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |
|-----|---------------------|----------------------|------------|
|  25 |               0.433 |                0.272 |      0.002 |
| 100 |              12.342 |                1.258 |      0.006 |
| 200 |              67.399 |                5.994 |      0.007 |
| 300 |             128.101 |               18.563 |      0.008 |
| 400 |             115.099 |                6.100 |      0.012 |
| 500 |             203.466 |               17.301 |      0.011 |
| 600 |             327.547 |               18.914 |      0.017 |
| 700 |             395.277 |               41.807 |      0.016 |
| 800 |             509.816 |               15.581 |      0.016 |
| 900 |             883.191 |               37.203 |      0.020 |

|   n shuffled |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |
|--------------|---------------------|----------------------|------------|
|  25          |               0.177 |                0.183 |      0.004 |
| 100          |               0.749 |                0.631 |      0.011 |
| 200          |               1.265 |                1.449 |      0.027 |
| 300          |               2.703 |                2.573 |      0.076 |
| 400          |               3.201 |                4.081 |      0.058 |
| 500          |               4.903 |                4.936 |      0.073 |
| 600          |               6.309 |                7.058 |      0.087 |
| 700          |               6.389 |               56.154 |      0.117 |
| 800          |               8.097 |                8.883 |      0.151 |
| 900          |               9.624 |               14.230 |      0.182 |


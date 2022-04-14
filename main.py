import random, time
import tabulate

def qsort(a, pivot_fn):
  if (len(a) == 0):
    return a
  else:
    p = pivot_fn(a)

    #left side
    l = filter(lambda x: x < p,a)
    left = list(l)

    #right side
    r = filter(lambda x: x >p,a)
    right = list(r)

    #middle
    m = filter(lambda x:x == p, a)
    mid= list(m)
    
    qsort_left = qsort(left, pivot_fn)
    qsort_right= qsort(right, pivot_fn)

    return qsort_left + mid + qsort_right 


def qsort_random(a):
  return qsort(a, lambda a: random.choice(a))
  
def qsort_fixed(a):
  return qsort(a, lambda a: a[0])
pass

def fixed(a):
  return a[0]

      
def time_search(sort_fn, mylist):
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###
  
def compare_sort(sizes=[25, 100, 200, 300, 400, 500, 600, 700, 800, 900]):
  qsort_fixed_pivot = qsort_fixed
  qsort_random_pivot = qsort_random
  #tim_sort = sorted
  result = []
  
  for size in sizes:
      # create list in ascending order
      mylist = list(range(size))
      # shuffles list if needed
     
      random.shuffle(mylist)
      result.append([
          len(mylist),
       time_search(qsort_fixed_pivot, mylist),
          time_search(qsort_random_pivot, mylist),#time_search(tim_sort, mylist)
      ])
  return result
    ###
  pass
  
def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', "tim-sort"],
                            floatfmt=".3f",
                            tablefmt="github"))
  
def test_print():
    print_results(compare_sort())
  
random.seed()
test_print()


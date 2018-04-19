import numpy as np

"""
[[0, 1, 1, 1],
[1, 0, 1, 0],
[1, 1, 0, 1],
[1, 0, 1, 0]]
"""


def make_color(A, m):
   if len(A)==0:
      return True

   colors = np.zeros(len(A))
   for i in xrange(len(A)):
      all_colors = np.zeros(m)
      for j in xrange(len(A)):
         if A[i][j] > 0:
            if colors[j] > 0:
               all_colors[colors[j]-1] = 1
   
      print all_colors
      if sum(all_colors)==m:
         print "imposible"
         return False

      colors[i] = np.argmin(all_colors)+1

   print colors
   return True 


A = [[0, 1, 1, 1],
[1, 0, 1, 0],
[1, 1, 0, 1],
[1, 0, 1, 0]]

print make_color(A, 3)

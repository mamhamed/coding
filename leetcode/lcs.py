
a = 'AGGTAB'
b = 'GXTXAYB'

map = {}
def lcs(str1, str2):
   if len(str1) == 0 or len(str2) == 0:
      return 0

   key = str1+'_'+str2
   if key in map.keys():
      return map[key]

   if str1[0]==str2[0]:
      m = 1+lcs(str1[1:], str2[1:])
      map[key] = m
      return m
   else:
      m1 = lcs(str1[1:], str2)
      m2 = lcs(str1, str2[1:])
      m3 = lcs(str1[1:], str2[1:])
      m = max(m1, m2, m3)
      map[key] = m
      return m



print lcs(a,b)
      


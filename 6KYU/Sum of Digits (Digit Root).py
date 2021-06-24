def digital_root(n):
   string_n = str(n)
   int_n = map(int, string_n)

   if n < 10:
       return n
   else:
       return digital_root(sum(int_n))

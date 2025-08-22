import numpy as np

print("\n",2**3,"\n")

print(np.sqrt(16),"\n")

print(16**(1/2),"\n")

M_a = [1,2,3]
M_b = [4,5,6]
print(M_a+M_b,"\n")
M_c = [x+y for x,y in zip(M_a,M_b)]
print(M_c,"\n")

#o tambien

M_a1 = np.array([1,2,3])
M_b1 = np.array([4,5,6])
M_c1 = M_a1+M_b1
print(M_c1)

#ejercicio

def f(m,n,o):
  primero =  (m/(np.sin((2*n)-3)))-o
  segundo = np.cos(3*n+2)
  terccero = np.sqrt(np.abs(np.log(o+(m**-3))**3))
  cuarto = m/(o+1)
  return ((primero**2)+segundo)/(terccero+cuarto)


m = np.array([1/3,2/5,3/7])
o = np.array([2,4,6])
n = np.array([np.radians(35), np.radians(50), np.radians(65)])

print(f(m,n,o))

import sympy as sp
sum = 3 # change the sum variable to get the equations
sum += 2
triangle = [] #This variable hosts our factorials and our data
for fact in range(1, sum):
   factorial = 1
   for x in range(1, fact+1): factorial = factorial * x
   triangle.append([2,1]) if fact == 2 else triangle.append([factorial])
 
def fuc(row):# Computing the Data Set of the triangle
   n = 0
   while n != sum-row-2:
       x1, x2 = triangle[n+row][row-1], triangle[n+row][row]
       n += 1
       triangle[n+row].append((n+1)*(x1 + x2))
   triangle[row+1].append(1)
for b in range(1,sum-2): fuc(b)
t2, row = [[] for i in range(len(triangle))], 0 #Using the 'triangle' variable to get our Main Data Set
for x in triangle:
   t2[row].append(x[0])
   for n in range(1, len(x)): t2[row].append(x[n-1]+x[n])
   t2[row].append(1)
   row += 1
 
solve, pascal, variable = [], [], sp.symbols('x') #Getting the values for our equation from the Data Set (t2)
for x in range(2, len(t2)+1):
   col, val = -1, []
   for row in range(x):
       val.append(t2[col][x+col])
       col -= 1
   if len(val)>0: solve.append(val)
for x in range(len(t2[-2])-1): pascal.append(t2[-2][x]+t2[-2][x+1])
pascal.append(1)
 
answers, i = [sp.solve(sp.Eq(variable*t2[-1][0],t2[-2][0]))[0]], 0 #Doing Algebra
for x in solve:
   pascal_num = pascal[i]
   for n in range(len(x)-1):pascal_num = pascal_num - (x[n]*answers[n])
   answers.append(sp.solve(sp.Eq(variable*x[-1],pascal_num))[0])
   i += 1
 
i = sum -1 # Displaying the equation
for x in answers:
   if i == sum -1: print(f"{x}n^{i}", end="")
   else:
       if x > 0: print(f"+ {x}n^{i} ", end="")
       elif x < 0: print(f"- {abs(x)}n^{i}", end="")
   i -= 1
print("")
 
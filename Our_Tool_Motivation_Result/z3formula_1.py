from z3 import *
i_0 = Real('i_0')
result_1 = Real('result_1')
n_0 = Real('n_0')
result_2 = Real('result_2')
i_1 = Real('i_1')
result_0 = Real('result_0')
i_2 = Real('i_2')
s = Solver()
s.add(Not(Implies(And(Not(i_1 <= n_0), And(result_1 == result_2, And(i_1 == i_2, And(i_2 == i_1 + 1, And(Not(result_2 > n_0), And(result_2 == result_1 * n_0, And(Not(result_1 >= 2), And(Not(i_1>=1), And(Not(i_1 <= n_0), And(result_1 == result_0, And(i_1 == i_0, i_0 = 1))))))))))), result_2 < ((2**256)))))
r = s.check()
if str(r) == "unsat":
    print("looksgood")
else:
    print("cannotsay")
    print(s.model())

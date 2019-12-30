def task_1():
    return "\n".join([i * str(i) for i in range(10)]) + "\n"


assert (
    task_1()
    == """
1
22
333
4444
55555
666666
7777777
88888888
999999999
"""
)

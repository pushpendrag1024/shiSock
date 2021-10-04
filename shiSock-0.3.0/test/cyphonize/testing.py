import timeit

py = timeit.timeit("Sserver.Sserver('test.yaml')", setup = 'import Sserver', number = 1000)
py_o = timeit.timeit("Sserver_o.Sserver('test.yaml')", setup = 'import Sserver_o', number = 1000)
cy = timeit.timeit("server_c.Sserver('test.yaml')",setup = 'import server_c', number = 1000)

print(f"py => {py}")
print(f"py_o => {py_o}")
print(f"cy => {cy}")
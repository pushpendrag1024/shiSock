import timeit

cy = timeit.timeit("Sclient_cy.Sclient('shikhar', 'yml.yaml')", setup = 'import Sclient_cy', number = 1000)
py = timeit.timeit("Sclient_py.Sclient('shikhar', 'yml.yaml')", setup = 'import Sclient_py', number = 1000)

print(cy, py)

print(f'Cython is {py/cy}x faster')
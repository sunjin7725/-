import numpy as np

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

photo_dict = dict(zip(name, yearning))
print([sum(list(map(lambda x: photo_dict.get(x, 0), i))) for i in photo])

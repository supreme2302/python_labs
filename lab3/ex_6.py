#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gen import field, gen_random
from librip.iterators import Unique as unique

path = sys.argv[1]
#print(path)

with open(path, encoding="utf8") as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted([st for st in unique(field(arg,'job-name'), ignore_case=True)])


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("Программист") , arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    salary = gen_random(100000, 200000, len(arg))
    return [i + ', зарплата ' + str(j) + ' руб.' for i,j in zip(arg, salary)]


#print(f4(f3(f2(f1(data)))))

with timer():
    f4(f3(f2(f1(data))))



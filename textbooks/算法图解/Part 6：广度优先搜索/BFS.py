'''
Author: ZhXZhao
Date: 2020-10-27 11:14:58
LastEditors: ZhXZhao
LastEditTime: 2020-10-27 14:42:21
Description:
'''
from collections import deque


def is_seller(person):
    if person[-1] == "m":
        return True
    else:
        return False


def BFS(graph):
    # 用队列存储待遍历的图中节点
    search_queue = deque()
    search_queue += graph["you"]
    # 该字典用于检查某个元素是否检查过，以防图中出现环，进入死循环，也可以通过创建一个列表来放置检查过的元素，每次检查元素之前先检查元素是否在列表中。
    repeat = dict()
    for name in graph.keys():
        repeat[name] = False
    while search_queue:
        person = search_queue.popleft()
        if not repeat[person]:
            print(person)
            if is_seller(person):
                print("I find the mango seller!"+person)
                return True
            else:
                search_queue += graph[person]
                repeat[person] = True
    return False


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(BFS(graph))

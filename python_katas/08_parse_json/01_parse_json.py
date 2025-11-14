# json：适合保存配置 / 前后端通信
import json
data = {"name": "Alice", "age": 25}
with open("data.json", "w") as f:
    json.dump(data, f)

# pickle：保存 Python 对象状态
import pickle
nums = [1, 2, 3]
with open("nums.pkl", "wb") as f:
    pickle.dump(nums, f)

# shelve：像 dict 一样的持久化存储
import shelve
with shelve.open("store.db") as db:
    db["user"] = {"name": "Bob", "score": 88}

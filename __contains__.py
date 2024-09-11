class MyList:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        return item in self.data


my_list = MyList([1, 2, 3, 4, 5])
print(3 in my_list)   # True
print(6 in my_list)   # False
my_list = MyList("hello world")
print("hell" in my_list)

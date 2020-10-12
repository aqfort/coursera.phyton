class Value:
    def __get__(self, obj, obj_type):
        return self.amount * (1 - obj.commission)

    def __set__(self, obj, value):
        self.amount = value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


if __name__ == "__main__":
    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)

    new_account.amount = 200

    print(new_account.amount)


# class Value:
#     def __init__(self):
#         self.amount = 0

#     def __get__(self, obj, obj_type):
#         return self.amount

#     def __set__(self, obj, value):
#         self.amount = value - value * obj.commission

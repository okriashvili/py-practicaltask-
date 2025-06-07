# დაწერეთ ფუნქცია რომელიც მომხმარებელს უსასრულოდ შეეკითხება სახელებს და ლისტში დაამატებს ამ სახელებს.
# თუ მომხმარებელი შეიყვანს სიტყვა "stop"-ს, მაგ შემთხვევაში გაჩერდეს პროგრამა და დააბრუნოს ეს ლისტი.
# გაითვალისწინეთ: "stop" სიტყვა არ უნდა ჩაამატოთ ლისტში!
# გაითვალისწინეთ: ფუნქცია არ იღებს არანაირ პარამეტრს
#
#
#
# def funct():
#     emptyDict = {}
#     while True:
#         name = input("Enter the name: ")
#         if name == "stop":
#             break
#         elif  name in emptyDict:
#             emptyDict[name] = emptyDict[name] + name
#     return emptyDict
# print(funct())


# def collect_fruits():
#     fruits_count = {}
#
#     while True:
#         fruit = input("Enter your favorite fruit: ").lower()
#
#         if fruit == "stop":
#             break
#
#         if fruit in fruits_count:
#             fruits_count[fruit] += 1
#         else:
#             fruits_count[fruit] = 1
#
#     return fruits_count
#
# # ფუნქციის გამოძახება
# result = collect_fruits()
# print(result)



def enter_names():
    names = []
    while True:
        name = input("enter a name: ")
        if name == "stop":
            break
        elif name in names:
            for i in names:
                if names.count(i) > 1:
                    names.remove(i)
        else:
            names.append(name)
    return names
print(enter_names())

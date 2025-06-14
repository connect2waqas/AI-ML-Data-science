
# name = ["waqas", "ali", "ahmed", "usman", "umer"]
# # print(name.append("hassan"))
# # print(name)
# # print(name.count("waqas"))
# print(name.copy())

# name = name.reverse()
# print(name)


import chardet

with open('file.json', 'rb') as f:
    result = chardet.detect(f.read())
    print(result['encoding'])

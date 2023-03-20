# file = open("file.txt", "w")
# file.write("hello world")
# file.close()

# with open("file.txt", "w") as f:
#     f.write("1123")
#     f.write("abc")
    
# with open("file.txt", "a") as f:
#     f.write("1123")
#     f.write("abc")
    
# with open("file.txt", "r+") as f:   #r+ и запись и чтение
#     print(f.read())
#     f.write("asaa")
#     f.seek(1)                       # считает дозаписанное с указанного(0) симола
#     print(f.read())
   
# with open("file.txt", "w") as f:
#     a = ["asaees\n", "fffs\n", "asaw\n"]
#     for i in a:
#         f.writelines(i)

# with open("file.txt", "r") as f:
#     print(f.readlines())

# with open("file.txt", "r") as f:
#     a = f.readlines()
#     a = [i.strip() for i in a]       # Собрать  список и удалить \n
#     print(a)


x = input("Enter something: ")
try:
    val = int(x)
    print("Integer")
except:
    try:
        val = float(x)
        print("Float")
    except:
        print("String")
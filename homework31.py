string=str(input())
print(string[:string.find(")")] + ")"*string.count("("))
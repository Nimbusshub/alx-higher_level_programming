#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as bussy
result = ""
for j in dir(bussy):
    result = j
    if result.startswith('_') == True:
        continue
    print("{}".format(j))

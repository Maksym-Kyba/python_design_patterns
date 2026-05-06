def concatenate(string_list):
    result = ""
    for item in string_list:
        result += item
    return result


def better_concatenate(string_list):
    result = "".join(string_list)
    return result


if __name__ == "__main__":
    string_list = ["Abc", "Def", "Ghi"]
    print(concatenate(string_list))
    print(better_concatenate(string_list))


#Concatenating strings with  + or = in a loop creates a new string object each time
#Which is inefficient. The best solution is to use the .join() method on strings
#Which is designed for efficiency when concatenating strings from a sequence or iterable.

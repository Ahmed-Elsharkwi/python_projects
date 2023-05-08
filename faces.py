#replace :) with 🙂 and replace :( with 🙁
def main():
    s = input()
    print(convert(s), end="")


def convert(n):
    n = n.replace(":)", "🙂")
    n = n.replace(":(", "🙁")
    return n
main()

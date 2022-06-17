def palindromo(string: str) -> bool:
    string = string.replace(" ", "")
    return string.upper() == string[::-1].upper()

def run():
    print(palindromo(1000))

if __name__ == "__main__":
    run()
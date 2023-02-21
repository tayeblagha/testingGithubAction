def greet(name):
    """This function greets the person passed in as a parameter"""
    print("Hello, " + name + "!")

def main():
    name = input("Enter your name: ")
    greet(name)

if __name__ == "__main__":
    main()

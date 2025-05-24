import random

def main():
    x=int(input("How many sides does your dice have? "))
    roll=random.randint(1,x)
    print(f"Your roll is {roll}")

if __name__ == '__main__':
    main()

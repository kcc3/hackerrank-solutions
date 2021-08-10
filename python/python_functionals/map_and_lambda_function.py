# Hackerrank Problem: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: pow(x, 3) # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    li = [0,1]
    for i in range(2, n):
        li.append(li[i-2] + li[i-1])
    return(li[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

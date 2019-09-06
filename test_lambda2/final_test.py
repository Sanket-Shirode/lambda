import json

def sum(n=10):
    sum_of_no = 0
    for x in range(n+1):
        sum_of_no = x + sum_of_no
    return sum_of_no

def lambda_handler(event, context):
    # TODO implement
    return f"The total value is {sum()}"
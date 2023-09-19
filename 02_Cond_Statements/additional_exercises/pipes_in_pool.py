pool_volume = int(input()) # in liters
first_pipe_debit = int(input()) # liters per hour
second_pipe_debit = int(input()) # liters per hour
hours_the_worker_is_missing = float(input())

first_pipe_total = first_pipe_debit * hours_the_worker_is_missing
second_pipe_total = second_pipe_debit * hours_the_worker_is_missing
total_debit = first_pipe_total + second_pipe_total

first_pipe_contribution_percentage = (first_pipe_total / total_debit) * 100
second_pipe_contribution_percentage = (second_pipe_total / total_debit) * 100
fullness_percentage = (total_debit / pool_volume) * 100
overflow_in_liters = total_debit - pool_volume

if total_debit <= pool_volume:
    print(f"The pool is {fullness_percentage:.2f}% full.\
 Pipe 1: {first_pipe_contribution_percentage:.2f}%.\
 Pipe 2: {second_pipe_contribution_percentage:.2f}%.")
else:
    print(f"For {hours_the_worker_is_missing} hours the pool overflows with {overflow_in_liters} liters.")
number_of_transactions=10
time_of_every_transaction=7
total_time=60

# Number of completed transactions
completed = total_time // time_of_every_transaction
# Number of remaining minutes
minutes = total_time % time_of_every_transaction
# Set the number of remaining transactions
remaining_tasks = number_of_transactions - completed
# Set the total time needed to complete all transactions
required_time = number_of_transactions * time_of_every_transaction

# Print the results
print("The number of remaining transactions is", remaining_tasks)
print("The number of minutes needed to complete all transactions is", required_time)
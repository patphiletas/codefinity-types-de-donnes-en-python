total_minutes = 60
minutes_per_transaction = 7

completed = total_minutes // minutes_per_transaction
minutes = total_minutes % minutes_per_transaction

# Print these values
print("The number of completed transactions is", completed)
print("The number of remaining minutes is", minutes)
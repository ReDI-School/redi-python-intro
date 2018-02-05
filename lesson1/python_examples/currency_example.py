amount = 100
rate_from_dollars_to_x = 15
rate_from_x_to_euros = 0.05

amount_x = amount * rate_from_dollars_to_x
amount_euros = amount_x * rate_from_x_to_euros

print(amount_euros)
def log_transfer(x):
  x = round(x, 2)
  total = 0

  if x > 0:
    total += x
    print(f"Deposited ${x}")
  
  elif x < 0:
    total -= x
    x = x * -1
    print(f"Withdrew ${x}")
  
  elif x == 0:
    print("Balance unchanged")

  elif type(x) == str:
    number = float(x)

  
log_transfer(24)
log_transfer(-13)
log_transfer(0)

log_transfer(499.2543)
log_transfer(-43.0387)
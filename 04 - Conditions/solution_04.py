customer_age = 24
is_student = True

if customer_age < 18:
    print("🎟️ Entry is FREE!")
elif is_student or customer_age > 65:
    print("🎟️ Entry is 50% off!")
else:
    print("🎟️ Entry is full-price!")

# Using a dictionary to avoid match cases repetition    

users = [
    {id:1, "total":100, "coupon":"P20"},
    {id:2, "total":200, "coupon":"P50"},
    {id:3, "total":300, "coupon":"P100"},
]
discounts = {
    "P20":(0.2,0),
    "P50":(0.5,0),
    "P100":(1,0)
}
for user in users:
    discount, extra = discounts[user["coupon"]]
    discounted_total = user["total"] * (1-discount) - extra
    print(f"User {user['id']} has a total of {discounted_total}")
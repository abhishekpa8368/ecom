import pandas as pd
import random
from faker import Faker

def generate_synthetic_data(rows=100000):
    faker = Faker()
    data = []

    for _ in range(rows):
        order_id = faker.uuid4()
        customer_name = faker.name()
        product_name = faker.random_element(
            ["Laptop", "Headphones", "Smartphone", "Monitor", "Keyboard", "Mouse"]
        )
        category = "Electronics"
        cost_price = round(random.uniform(10, 1000), 2)
        sale_price = round(cost_price + random.uniform(5, 500), 2)
        discount = round(random.uniform(0, 0.3) * sale_price, 2)
        total_price = sale_price - discount
        coupon_code = faker.random_element([None, "WELCOME10", "SALE20", "FESTIVE30"])
        order_date = faker.date_between(start_date="-1y", end_date="today")
        is_fraud = random.choices([True, False], weights=[0.01, 0.99])[0]

        data.append({
            "order_id": order_id,
            "customer_name": customer_name,
            "product_name": product_name,
            "category": category,
            "cost_price": cost_price,
            "sale_price": sale_price,
            "discount": discount,
            "total_price": total_price,
            "coupon_code": coupon_code,
            "order_date": order_date,
            "is_fraud": is_fraud
        })

    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_synthetic_data()
    df.to_csv("../data/ecommerce_data.csv", index=False)
    print("Data generated successfully!")

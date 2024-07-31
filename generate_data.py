from random import random, randint, choice
from faker import Faker
from faker.providers import misc, date_time
from sys import argv

def generate_data(rows: int) -> None:
    fake = Faker()
    fake.add_provider(misc) # for sha1
    fake.add_provider(date_time)
    customers = [fake.sha1()[:5] for _ in range(50)]
    products = [fake.sha1()[:5] for _ in range(50)]

    with open('orders.csv', 'w') as file:
        file.write('order_id;customer_id;order_date;product_id;product_name;product_price;quantity\n')
        for _ in range(rows):
            order_id = fake.sha1()[:10]
            customer_id = choice(customers)
            order_date = fake.date_this_year().isoformat()
            product_id = product_name = choice(products)
            product_price = randint(1, 10000) * random()
            quantity = randint(1, 11)
            file.write(f'{order_id};{customer_id};{order_date};{product_id};{product_name};{product_price:.2f};{quantity}\n')

if __name__ == '__main__':
    if len(argv) < 2:
        raise ValueError("Insufficient arguments")
    if len(argv) > 2:
        raise ValueError("Too many arguments")
    generate_data(int(argv[1]))

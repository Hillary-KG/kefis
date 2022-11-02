from flask_seeder import Seeder, Faker, generator
from app.products.models import Product

class ProductSeed(Seeder):
    def run(self):
        faker = Faker(
            cls=Product,
            init={
                "id":generator.Integer(start=0),
                "name":generator.Name(),
                "qtty":generator.Integer(start=0, end=15),
                "reoder_level":generator.Integer(start=5, end=10),
            }
        )

        for prdct in faker.create(10):
            self.db.session.add(prdct)
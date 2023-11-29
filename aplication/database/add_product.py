from products import Product

# Example products
product1 = Product(
    name='Product 1',
    description='Description for Product 1',
    price='19.99',
    image_url='https://images.unsplash.com/photo-1496181133206-80ce9b88a853?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
)

product2 = Product(
    name='Product 2',
    description='Description for Product 2',
    price='29.99',
    image_url='https://images.unsplash.com/photo-1525598912003-663126343e1f?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
)

# Save products to the database
product1.save()
product2.save()

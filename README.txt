"""Customer Management App

# Initial Setup
project_name = 'Config'
app_names = [
  'accounts',
]

# Models
Customer
Tag
Product  # many2many - Tag
Order  # foreignkey - Customer, Product

# URLs
config.urls,  # includes:
accounts.urls,

# Views
home,
products,
customer,
createOrder,
updateOrder,
deleteOrder,

# Templates
accounts/base.html
accounts/dashboard.html
accounts/products.html
accounts/customer.html
accounts/navbar.html
accounts/status.html
accounts/order_form.html
accounts/delete.html

# 3rd Party

"""



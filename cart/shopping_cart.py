from store.models import Product
from decimal import Decimal


class ShoppingCart:
    """
    A base Shopping Cart class, providing some default behaviours that can be
    inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("skey")
        if "skey" not in request.session:
            cart = self.session["skey"] = {}
        self.cart = cart

    def add(self, product, qty):
        """
        Adding and updating the users shopping cart session data
        """
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]["qty"] = qty
        else:
            self.cart[product_id] = {"price": str(product.price), "qty": int(qty)}

        self.save()

    def remove(self, product_id):
        """
        Remove all instances of the product from the session data
        """
        product_id = str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def update(self, product_id, qty):
        """
        Update session items data
        """
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id]["qty"] = qty

        self.save()

    def __len__(self):
        """
        Get the shopping cart data and count the quantity of items
        """
        return sum(item["qty"] for item in self.cart.values())

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for unit in products:
            cart[str(unit.id)]["product"] = unit

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def get_total_price(self):
        return sum(
            [Decimal(item["price"]) * item["qty"] for item in self.cart.values()]
        )

    def save(self):
        self.session.modified = True

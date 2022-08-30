class ShoppingCart:
    """
    A base Shopping Cart class, providing some default behaviours that can be
    inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, product, qty):
        """
        Adding and updating the users shopping cart session data
        """
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': qty}

        self.session.modified = True

    def __len__(self):
        """
        Get the shopping cart data and count the quantity of items
        """
        return sum(item['qty'] for item in self.cart.values())

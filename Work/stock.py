class Stock:
    """Represent a single holding of stock"""
    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price
        
    def cost(self):
        return self.shares * self.price

    def sell(self, amount: int):
        self.shares -= amount
    
    def __repr__(self) -> str:
        return f"Stock({self.name}, {self.shares}, {self.price})"
class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self) -> str:
        return f"{self.name} (${self.amount:.2f})"

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def __str__(self):
        titulo = self.name.center(30, '*')
        lineas = [titulo]

        for item in self.ledger:
            descripcion = item['description'][:23].ljust(23)
            monto = f"{item['amount']:.2f}".rjust(7)
            conjunto_de_lineas = descripcion + monto
            lineas.append(conjunto_de_lineas)
        lineas.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lineas)


def create_spend_chart(categories):
    gastos = []
    for categoria in categories:
        gasto = sum(item['amount'] for item in categoria.ledger if item['amount'] < 0)
        gastos.append(abs(gasto))

    total = sum(gastos)
    porcentajes = [(gasto / total) * 100 for gasto in gastos]

    chart = "Percentage spent by category\n"

    for nivel in range(100, -1, -10):
        chart += str(nivel).rjust(3) + "| "
        for porcentaje in porcentajes:
            if porcentaje >= nivel:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(categoria.name) for categoria in categories)
    for i in range(max_len):
        chart += "     "
        for categoria in categories:
            if i < len(categoria.name):
                chart += categoria.name[i] + "  "
            else:
                chart += "   "
        if i != max_len - 1:
            chart += "\n"

    return chart

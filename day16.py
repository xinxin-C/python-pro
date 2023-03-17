from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ['pikaqiu', 'ddd','dddei'])
table.add_column("Type", ['water', 'fire', 'tree'])
table.align = 'l'
print(table)
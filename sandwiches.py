sandwich_orders = ["Bacon","Beef","cheese","chicken"]
finished_sandwiches = []

while sandwich_orders:
    done = sandwich_orders.pop()
    print(f"\nI made your {done} sandwich...\n")
    finished_sandwiches.append(done)
print("-- sandwiches that was made --\n")
for finished_sandwich in finished_sandwiches:
    print("-",finished_sandwich.title())
    

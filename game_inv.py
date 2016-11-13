# starting inventory
inv = {"rope": 1, "torch": 6, "gold_coin": 42, "dagger": 1, "arrow": 12}
# additional loot
dragon_loot = ["gold_coin", "dagger", "gold_coin", "gold_coin", "ruby"]

# raw inv display
def display_inventory(inv):
    total = 0
    for k, v in inv.items():
        print("%d %s" % (v, k))
        total += v
    print("%s %d" % ("Total number of items: ", total))

# adding lists of items to inventory
def add_to_inventory(inv, added_items):
    for i in added_items:
        if i in inv:
            inv[i] += 1
        else:
            inv.update({i: inv.get(i, 0) + 1})

# same as display but sorted and organised into a table, takes an argument of these two: count.asc or count.desc
# without argument its not sorting only organising into table

def print_table(*order):
    total = 0
    mlenght = len(max(inv, key=len))
    separation = mlenght * 2 + 4
    ascinv = sorted(inv.items(), key=lambda inv : inv[1], )
    descinv = sorted(inv.items(),key=lambda inv : inv[1], reverse = True)
    print("Inventory:")
    print("{0:>{width}s}    {1:>{width}s}".format("count", "item name", width = mlenght))
    print("-" * separation)
    if len(order) == 0:
        for k, v in inv.items():
            print("{0:>{width}d}    {1:>{width}s}".format(v, k, width = mlenght))
            total += v
        print("-"*separation)
        print("%s %d" % ("Total number of items: ", total))
    elif len(order) == 1 and order[0] == "count.desc":
        for k, v in descinv:
            print("{0:>{width}d}    {1:>{width}s}".format(v, k, width = mlenght))
            total += v
        print("-"*separation)
        print("%s %d" % ("Total number of items: ", total))
    elif len(order) == 1 and order[0] == "count.asc":
        for k, v in ascinv:
            print("{0:>{width}d}    {1:>{width}s}".format(v, k, width = mlenght))
            total += v
        print("-"*separation)
        print("%s %d" % ("Total number of items: ", total))

# exports the inventoy into a file takes the wished filename as an argument (without  file-extension)
def export_inventory(filename='export_inventory'):
    fw = open(filename+".csv", "w")
    fw.write("item name,count\n")
    for key, value in inv.items():
        fw.write("%s,%d\n" % (key, value))
    fw.close()

# reads a file and imports the data from it (takes filename as argument with file extension)
def import_inventory(filename):
    fr = open(filename, "r")
    importedlist = []
    for i in fr:
        importedlist.append(i.strip().split(","))
    del importedlist[0]
    for i in range (len(importedlist)):
        if importedlist[i][0] in inv:
            inv[importedlist[i][0]] += int(importedlist[i][1])
        else:
            inv.update({importedlist[i][0]: int(importedlist[i][1])})
    fr.close()

# tests
display_inventory(inv)
add_to_inventory(inv, dragon_loot)
print_table("count.desc")
export_inventory()
import_inventory("export_inventory.csv")
print_table("count.desc")
# tests

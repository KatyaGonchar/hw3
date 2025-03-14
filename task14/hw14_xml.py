# XML

import xml.etree.ElementTree as ET


def create_xml(filename, data):
    root = ET.Element("products")

    for product in data:
        ET.SubElement(root, "product", name=product["name"],
                      price=str(product["price"]),
                      quantity=str(product["quantity"]))

    tree = ET.ElementTree(root)
    try:
        tree.write(filename)
        print(f"XML file '{filename}' was created.")
    except Exception as e:
        print(f"Error: {e}")


def calculate_total_cost(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        total_cost = 0

        for product in root.findall("product"):
            name = product.get("name")
            price = float(product.get("price"))
            quantity = int(product.get("quantity"))

            total_cost += price * quantity

            print(f"{name}: Price {price}, Quantity {quantity}, Cost {price * quantity}")

        return total_cost

    except Exception as e:
        print(f"Error: {e}")
        return None


filename = "products.xml"
data = [
    {"name": "Bananas", "price": 5, "quantity": 50},
    {"name": "Apples", "price": 10, "quantity": 100},
    {"name": "Oranges", "price": 15, "quantity": 200}
]

create_xml(filename, data)
total_cost = calculate_total_cost(filename)

if total_cost is not None:
    print(f"Total goods cost: {total_cost}")

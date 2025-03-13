# XML

import xml.etree.ElementTree as ET

filename = "products.xml"


def create_xml():
    root = ET.Element("products")

    ET.SubElement(root, "product", name="Bananas", price="5", quantity="50")
    ET.SubElement(root, "product", name="Apples", price="10", quantity="100")
    ET.SubElement(root, "product", name="Oranges", price="15", quantity="200")

    tree = ET.ElementTree(root)
    try:
        tree.write(filename)
        print(f"XML file '{filename}' was created.")
    except Exception as e:
        print(f"Error: {e}")


def calculate_total_cost():
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        total_cost = 0

        for product in root.findall("product"):
            name = product.get("name")
            price = float(product.get("price"))
            quantity = int(product.get("quantity"))

            total_cost += price * quantity

            print(f"{name}: Цена {price}, Количество {quantity}, Стоимость {price * quantity}")

        return total_cost

    except Exception as e:
        print(f"Error: {e}")
        return None


create_xml()
total_cost = calculate_total_cost()

if total_cost is not None:
    print(f"Общая стоимость всех товаров: {total_cost}")

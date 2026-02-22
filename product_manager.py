import json

def load_data():
    try:
        with open("products.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(products):
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

def add_product(products):
    name = input("Nhập tên sản phẩm: ")
    brand = input("Nhập thương hiệu: ")
    price = int(input("Nhập giá: "))
    quantity = int(input("Nhập số lượng: "))

    new_id = f"LT{len(products) + 1:02d}"

    product = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    print("Đã thêm sản phẩm")
    return products

def display_all_products(products):

    if len(products) == 0:
        print("Kho hàng trống")
        return

    print("Danh sách sản phẩm")
    for p in products:
        print(
            p[0], "|",
            p["name"], "|",
            p["brand"], "|",
            p["price"], "|",
            "SL", p["quantity"]
        )


def search_product_by_name(products):
    keyword = input("Nhập tên cần tìm: ").lower()
    found = False

    for p in products:
        if keyword in p["name"].lower():
            print(p)
            found = True

    if not found:
        # sai nhẻ not f
        print("Không tìm thấy sản phẩm.")


def update_product(products):
    id_update = input("Nhập mã sản phẩm cần sửa: ")

    for p in products:
        if p["id"] == id_update:
            p["name"] = input("Tên mới: ")
            p["brand"] = input("Thương hiệu mới: ")
            p["price"] = int(input("Giá mới: "))
            p["quantity"] = int(input("Số lượng mới: "))
            print("Đã cập nhật sản phẩm")
            return

    print("Không tìm thấy sản phẩm")

def delete_product(products):
    
    id_delete = input("Nhập mã sản phẩm cần xóa: ")

    for p in products:
        if p["id"] == id_delete:
            products.remove(p)
            print("Đã xóa sản phẩm")
            return
    print("Không tìm thấy sản phẩm")





   
              
    


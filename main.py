from product_manager import *

products = load_data()

while True:
    print("\n===== POLY LAP =====")
    print("1. Hiển thị sản phẩm")
    print("2. Thêm sản phẩm")
    print("3. Cập nhật sản phẩm")
    print("4. Xóa sản phẩm")
    print("5. Tìm kiếm sản phẩm")
    print("0. Thoát")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        display_all_products(products)
    elif choice == "2":
        products = add_product(products)
    elif choice == "3":
        update_product(products)
    elif choice == "4":
        delete_product(products)
    elif choice == "5":
        search_product_by_name(products)
    elif choice == "0":
        save_data(products)
        print("Đã lưu dữ liệu. Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")

print("Version DEV")

print("New feature v2")

print("TEST GIT CHANGE")

print("new commit")
"""Module chứa định nghĩa thực đơn, custom exceptions và logic xử lý nghiệp vụ POS."""

import logging

# Cấu hình logging hiển thị ra Terminal
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Thực đơn mặc định của hệ thống
DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}


class ItemNotFoundError(Exception):
    """Ngoại lệ xảy ra khi mã đồ uống không tồn tại trong thực đơn."""
    def __init__(self, drink_code):
        self.drink_code = drink_code
        super().__init__(f"Code: {drink_code}")


class InvalidQuantityError(Exception):
    """Ngoại lệ xảy ra khi số lượng nhập vào nhỏ hơn hoặc bằng 0."""
    def __init__(self, quantity):
        self.quantity = quantity
        super().__init__(f"Quantity: {quantity}")


def view_menu():
    """In ra thực đơn đồ uống hiện tại của cửa hàng."""
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, item in DRINK_MENU.items():
        print(f"[{code}] - {item['name']} - {item['price']:,} VNĐ")


def add_to_order(drink_code: str, quantity_str: str, order_list: list) -> bool:
    """Kiểm tra tính hợp lệ và thêm món ăn vào giỏ hàng.

    Args:
        drink_code (str): Mã đồ uống do người dùng nhập.
        quantity_str (str): Chuỗi số lượng do người dùng nhập.
        order_list (list): Danh sách giỏ hàng hiện tại.

    Returns:
        bool: True nếu thêm thành công, ngược lại False.
    """
    # Chuẩn hóa mã đồ uống (viết hoa, xóa khoảng trắng thừa)
    clean_code = drink_code.strip().upper()

    # Bẫy 2: Kiểm tra mã đồ uống tồn tại
    if clean_code not in DRINK_MENU:
        logging.warning("ItemNotFoundError - Code: %s", clean_code)
        print("Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")
        return False

    # Bẫy 1: Kiểm tra định dạng số lượng nguyên
    try:
        quantity = int(quantity_str)
    except ValueError:
        logging.error("ValueError - Invalid quantity input")
        print("Vui lòng nhập số lượng là một số nguyên!")
        return False

    # Bẫy 3: Kiểm tra số lượng phải > 0
    if quantity <= 0:
        logging.warning("InvalidQuantityError - Quantity: %d", quantity)
        print("Số lượng phải lớn hơn 0!")
        return False

    # Thêm sản phẩm vào giỏ hàng
    order_item = {
        "code": clean_code,
        "name": DRINK_MENU[clean_code]["name"],
        "price": DRINK_MENU[clean_code]["price"],
        "quantity": quantity
    }
    order_list.append(order_item)
    
    # Log thông báo thành công
    logging.info("Added %d of %s to order", quantity, clean_code)
    print(f"Đã thêm {quantity} x {DRINK_MENU[clean_code]['name']} vào giỏ hàng.")
    return True


def calculate_total(order_list: list) -> int:
    """Tính tổng tiền của tất cả các món trong giỏ hàng.

    Args:
        order_list (list): Danh sách các món trong giỏ hàng.

    Returns:
        int: Tổng số tiền cần thanh toán.
    """
    total = 0
    for item in order_list:
        total += item["price"] * item["quantity"]
    return total


def view_order(order_list: list):
    """Hiển thị chi tiết giỏ hàng hiện tại và tổng tiền."""
    if not order_list:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print(f"{'Mã SP':<6} | {'Tên đồ uống':<20} | {'Đơn giá':<8} | {'Số lượng':<8} | Thành tiền")
    print("-" * 64)
    
    for item in order_list:
        subtotal = item["price"] * item["quantity"]
        print(f"{item['code']:<6} | {item['name']:<20} | {item['price']:,:<8} | {item['quantity']:<8} | {subtotal:,} VNĐ")
        
    print("-" * 64)
    total_amount = calculate_total(order_list)
    print(f"Tổng tiền cần thanh toán: {total_amount:,} VNĐ")


def checkout(order_list: list) -> list:
    """Xử lý quy trình thanh toán và làm trống giỏ hàng nếu thành công."""
    if not order_list:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return order_list

    total_amount = calculate_total(order_list)
    print("\n--- THANH TOÁN ---")
    print(f"Tổng tiền cần thanh toán: {total_amount:,} VNĐ")
    
    confirm = input(f"Xác nhận thanh toán {total_amount:,} VNĐ? (y/n): ").strip().lower()
    
    if confirm == 'y':
        print("Thanh toán thành công.")
        logging.info("Checkout successful")
        print("Giỏ hàng đã được làm trống.")
        return []  # Trả về giỏ hàng rỗng mới
    elif confirm == 'n':
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")
        
    return order_list
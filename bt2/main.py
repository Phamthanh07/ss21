"""Module main điều khiển vòng lặp chạy giao diện CLI POS."""

import logging
import pos_logic


def main():
    """Vòng lặp tương tác Menu CLI chính của hệ thống POS."""
    current_order = []

    while True:
        print("\n========== HIGHLANDS MINI POS ==========")
        print("1. Xem thực đơn")
        print("2. Thêm món vào giỏ")
        print("3. Xem giỏ hàng & Tính tổng tiền")
        print("4. Thanh toán & Xóa giỏ hàng")
        print("5. Thoát ca làm việc")
        print("========================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            pos_logic.view_menu()
            
        elif choice == "2":
            print("\n--- THÊM MÓN VÀO GIỎ ---")
            drink_code = input("Nhập mã đồ uống: ")
            quantity_str = input("Nhập số lượng: ")
            pos_logic.add_to_order(drink_code, quantity_str, current_order)
            
        elif choice == "3":
            pos_logic.view_order(current_order)
            
        elif choice == "4":
            current_order = pos_logic.checkout(current_order)
            
        elif choice == "5":
            logging.info("Cashier logged out. System shutdown.")
            print("Đã thoát ca làm việc. Hẹn gặp lại!")
            break
            
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập từ 1 đến 5!")


if __name__ == "__main__":
    main()
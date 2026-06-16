import logging
import unittest

# 1. Định nghĩa Custom Exceptions ngay trong file
class InvalidAmountError(Exception): pass
class InsufficientBalanceError(Exception): pass

# Cấu hình logging
logging.basicConfig(filename="momo_transactions.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# 2. Logic nghiệp vụ
def deposit(user_money, amount):
    if amount <= 0: raise InvalidAmountError("Số tiền nạp phải > 0.")
    return user_money + amount

def transfer(user_money, amount, phone):
    if amount <= 0: raise InvalidAmountError("Số tiền chuyển phải > 0.")
    if amount > user_money: raise InsufficientBalanceError("Số dư không đủ.")
    return user_money - amount

# 3. Unit Test tích hợp ngay trong cùng file
class TestMomo(unittest.TestCase):
    def test_deposit(self): self.assertEqual(deposit(0, 500), 500)
    def test_transfer(self): self.assertEqual(transfer(500, 200, "0909090909"), 300)

# 4. Giao diện CLI
def main():
    # Kiểm tra nếu chạy chế độ test
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
        return

    user_money = 0
    while True:
        choice = input("\n1. Nạp | 2. Chuyển | 3. Thoát: ")
        try:
            if choice == "1":
                user_money = deposit(user_money, int(input("Số tiền nạp: ")))
            elif choice == "2":
                user_money = transfer(user_money, int(input("Số tiền chuyển: ")), "0909090909")
            elif choice == "3": break
        except Exception as e:
            print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()

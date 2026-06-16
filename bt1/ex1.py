import logging
from exceptions import InvalidAmountError, InsufficientBalanceError

# Cấu hình logging
logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def deposit(user_money, amount):
    if amount <= 0:
        raise InvalidAmountError("Số tiền nạp phải lớn hơn 0.")
    user_money += amount
    logging.info(f"Deposit: +{amount}. Balance: {user_money}")
    return user_money

def transfer(user_money, amount, phone):
    if amount <= 0:
        raise InvalidAmountError("Số tiền chuyển phải lớn hơn 0.")
    if amount > user_money:
        raise InsufficientBalanceError("Số dư không đủ để thực hiện giao dịch.")
    user_money -= amount
    logging.info(f"Transfer: -{amount} to {phone}. Balance: {user_money}")
    return user_money

def main():
    user_money = 0
    while True:
        print(f"\n--- SỐ DƯ: {user_money:,} VNĐ ---")
        print("1. Nạp tiền | 2. Chuyển tiền | 3. Thoát")
        choice = input("Chọn: ")
        
        try:
            if choice == "1":
                amt = int(input("Nhập số tiền nạp: "))
                user_money = deposit(user_money, amt)
            elif choice == "2":
                phone = input("Số ĐT: ")
                amt = int(input("Số tiền chuyển: "))
                user_money = transfer(user_money, amt, phone)
                print("Chuyển tiền thành công!")
            elif choice == "3":
                break
        except (InvalidAmountError, InsufficientBalanceError, ValueError) as e:
            print(f"LỖI: {e}")
            logging.error(f"Transaction Error: {e}")

if __name__ == "__main__":
    main()

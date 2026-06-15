"""Module kiểm thử tự động (Unit Test) cho logic nghiệp vụ POS."""

import unittest
from pos_logic import calculate_total, add_to_order


class TestHighlandsPOS(unittest.TestCase):
    """Lớp kiểm thử các hàm xử lý tính toán và bắt lỗi logic giỏ hàng."""

    def test_calculate_total(self):
        """Kiểm tra hàm tính tổng số tiền với giỏ hàng giả lập (Mock List)."""
        mock_order = [
            {"code": "P1", "name": "Phin Sữa Đá", "price": 35000, "quantity": 2},
            {"code": "F1", "name": "Freeze Trà Xanh", "price": 55000, "quantity": 1}
        ]
        # Tổng kỳ vọng: (35000 * 2) + (55000 * 1) = 125,000 VNĐ
        result = calculate_total(mock_order)
        self.assertEqual(result, 125000)

    def test_invalid_quantity(self):
        """Kiểm tra hàm add_to_order khi truyền số lượng âm xem có trả về False hay không."""
        mock_order = []
        # Thực hiện truyền số lượng không hợp lệ "-1"
        result = add_to_order(drink_code="P1", quantity_str="-1", order_list=mock_order)
        
        # Mong đợi kết quả trả về là False (Không cho phép thêm và ném log cảnh báo)
        self.assertFalse(result)
        # Giỏ hàng phải giữ nguyên trạng thái trống ban đầu
        self.assertEqual(len(mock_order), 0)


if __name__ == "__main__":
    unittest.main()
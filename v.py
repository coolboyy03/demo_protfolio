# def tinh_gia_tri_bieu_thuc_hau_to(bieu_thuc):
#     stack = []

#     for token in bieu_thuc:
#         if token.isdigit():
#             stack.append(int(token))
#         else:
#             operand2 = stack.pop()
#             operand1 = stack.pop()
#             if token == '+':
#                 stack.append(operand1 + operand2)
#             elif token == '-':
#                 stack.append(operand1 - operand2)
#             elif token == '*':
#                 stack.append(operand1 * operand2)
#             elif token == '/':
#                 stack.append(operand1 / operand2)
#             elif token == '^':
#                 stack.append(operand1 ** operand2)

#     return stack.pop()

# bieu_thuc_hau_to = ["1", "2", "3", "^", "+", "4", "5", "*", "/"]
# ket_qua = tinh_gia_tri_bieu_thuc_hau_to(bieu_thuc_hau_to)
# print("Giá trị của biểu thức hậu tố:", ket_qua)




# import datetime
# class Customer:
#     def __init__(self, ho_ten, gioi_tinh, nam_sinh, so_lan_mua_hang, tong_tien_mua_hang):
#         self.ho_ten = ho_ten
#         self.gioi_tinh = gioi_tinh
#         self.nam_sinh = nam_sinh
#         self.so_lan_mua_hang = so_lan_mua_hang
#         self.tong_tien_mua_hang = tong_tien_mua_hang

#     def __str__(self):
#         return f"{self.ho_ten}, {self.gioi_tinh}, {self.nam_sinh}, {self.so_lan_mua_hang}, {self.tong_tien_mua_hang}"
     
#     def tinh_so_tien_mua_hang_trung_binh(self):
#         if self.so_lan_mua_hang > 0:
#             return self.tong_tien_mua_hang / self.so_lan_mua_hang
#         else:
#             return 0
        
#     def tinh_tuoi_tho_hien_nay(self):
#         nam_hien_tai = datetime.datetime.now().year
#         return nam_hien_tai - self.nam_sinh
# # Khởi tạo danh sách để lưu trữ đối tượng Customer
# danh_sach_khach_hang = []

# # Mở tệp dữ liệu
# with open('customer_data.txt', 'r', encoding='utf-8') as file:
#     # Rest of your code
#     for line in file:
#         # Tách dòng thành các giá trị
#         values = line.strip().split(',')
        
#         if len(values) == 5:
#             ho_ten, gioi_tinh, nam_sinh, so_lan_mua_hang, tong_tien_mua_hang = values
#             nam_sinh = int(nam_sinh)
#             so_lan_mua_hang = int(so_lan_mua_hang)
#             tong_tien_mua_hang = float(tong_tien_mua_hang)

#             # Tạo đối tượng Customer và thêm vào danh sách
#             khach_hang = Customer(ho_ten, gioi_tinh, nam_sinh, so_lan_mua_hang, tong_tien_mua_hang)
#             danh_sach_khach_hang.append(khach_hang)

# # In danh sách khách hàng
# for khach_hang in danh_sach_khach_hang:
#     print(khach_hang)

# # Tìm khách hàng có số tiền mua hàng trung bình cao nhất
# khach_hang_cao_nhat = None
# so_tien_mua_hang_trung_binh_cao_nhat = 0

# for khach_hang in danh_sach_khach_hang:
#     so_tien_mua_hang_trung_binh = khach_hang.tinh_so_tien_mua_hang_trung_binh()
#     if so_tien_mua_hang_trung_binh > so_tien_mua_hang_trung_binh_cao_nhat:
#         khach_hang_cao_nhat = khach_hang
#         so_tien_mua_hang_trung_binh_cao_nhat = so_tien_mua_hang_trung_binh

# if khach_hang_cao_nhat:
#     print("Khách hàng có số tiền mua hàng trung bình cao nhất:")
#     print(khach_hang_cao_nhat)
#     print("Số tiền mua hàng trung bình:", so_tien_mua_hang_trung_binh_cao_nhat)
# else:
#     print("Không có khách hàng nào trong danh sách.")

# # In danh sách khách hàng và tuổi thọ hiện nay
# for khach_hang in danh_sach_khach_hang:
#     print(khach_hang)
#     print("Tuổi thọ hiện nay:", khach_hang.tinh_tuoi_tho_hien_nay())
#     print()


























# def liet_ke_tap_hop_chap(n, r):
#     def backtrack(combination, start):
#         if len(combination) == r:
#             print(combination)
#             return

#         for i in range(start, n + 1):
#             combination.append(i)
#             backtrack(combination, i + 1)
#             combination.pop()

#     if n < r:
#         print("Không có tổ hợp chập.")
#         return

#     backtrack([], 1)

# n = int(input("Nhập giá trị n: "))
# r = int(input("Nhập giá trị r: "))

# liet_ke_tap_hop_chap(n, r)
\
    
    


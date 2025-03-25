# Tạo và Truy cập Từ điển trong Python
# Tạo bằng cách đặt các mục trong dấu {ngoặc nhọn}.
# Mỗi mục trong từ điển có một cặp khóa - giá trị được phân tách bằng dấu phẩy.

# Đặc điểm của Từ điển:
# Từ điển là một tập hợp được sắp xếp không theo chỉ mục mà theo khóa, có thể thay đổi và không cho phép trùng lặp.
# Từ điển có thể thay đổi, nghĩa là chúng ta có thể thay đổi, thêm hoặc xóa các mục sau khi từ điển đã được tạo.
# Lưu ý: Khóa của từ điển phải là bất biến, chẳng hạn như tuple, chuỗi, số nguyên, v.v. Chúng ta không thể sử dụng các đối tượng có thể thay đổi (mutable) như danh sách làm khóa.

dict_a = {'name': 'Champ', 'age': 16}

# Truy cập các mục trong Từ điển:
# Để truy cập các mục trong từ điển, chúng ta sử dụng dấu ngoặc vuông [ ] cùng với khóa để lấy giá trị tương ứng.
# Chúng ta cũng có thể truy cập bằng phương thức get().
# Lưu ý:
# Khi sử dụng dấu ngoặc vuông [], nếu khóa không tồn tại trong từ điển, lỗi KeyError sẽ được thông báo.
# Nếu sử dụng phương thức get(), nó sẽ trả về None mà không gây ra lỗi

print(dict_a['name'])  # Output: Champ
# print(dict_a['city'])  # Output: KeyError: 'city'
print(dict_a.get('city'))  # Output: None

# Kiểm tra phần tử:
# Kiểm tra xem một khóa có tồn tại trong từ điển hay không.

result = 'name' in dict_a
print(result)

# Không cho phép khóa trùng lặp:
# Từ điển không thể có hai mục với cùng tên khóa. Khóa sẽ được cập nhật với giá trị cuối cùng như trong ví dụ dưới đây.

dictEx = {1: 'one', 2: 'two', 3: 'third', 3: 'three', 4: 'one'}
print(dictEx)
# Output: {1: 'one', 2: 'two', 3: 'three', 4: 'one'}
# Only the 3 with value updated at last is considered.

# Độ dài và Kiểu dữ liệu của Từ điển:
# Chúng ta có thể tìm độ dài và kiểu dữ liệu bằng các hàm tích hợp:
# len(Dict)
# type(Dict)

countries = {
    "United States": "Washington D.C.",
    "Italy": "Rome",
    "England": "London"
}
print(len(countries))
print(type(countries))
'''
Output: 
3
<class 'dict'>
'''

# Các thao tác trên Từ điển:
# Thêm một cặp khóa-giá trị

dict_a = {'name': 'Champ', 'age': 16}

dict_a['city'] = 'Delhi'
print(dict_a)

# Sửa đổi các mục hiện có
dict_a['age'] = 30
print(dict_a)

# Xóa các mục hiện có
del dict_a['age']
print(dict_a)

# Các phương thức của Từ điển:
dict_a = {'name': 'Champ', 'age': 16}

# Getting Keys:
# Để lấy các khóa trong từ điển, chúng ta
# Trả về danh sách tất cả các Khóa trong từ điển.
print(dict_a.keys())

# Getting Values:
# Trả về danh sách tất cả các Giá trị trong từ điển.
print(dict_a.values())

# Getting Items:
# Trả về danh sách tất cả các cặp (khóa-giá trị) trong từ điển.
print(dict_a.items())

# Cách duyệt qua từ điển trong Python
countries = {
    "United States": "Washington D.C.",
    "Italy": "Rome",
    "England": "London"
}
# 1. Duyệt qua các khóa (keys)
# print dictionary keys one by one
# # Cách 1: Duyệt trực tiếp
for country in countries:
  print(country)  # In ra các khóa: United States, Italy,..

print("----------")
# Cách 2: Sử dụng phương thức keys()
keys_list = list(countries.keys())
print(keys_list)
print("----------")
# Để in từng giá trị (value) của từ điển một cách riêng lẻ trong Python
for country in countries:
  capital = countries[country]
  print(capital)

# ITERATING USING DICTIONARY METHODS:
countries = {
    "United States": "Washington D.C.",
    "Italy": "Rome",
    "England": "London"
}

# Example 1: Using dict.keys() method
# Duyệt qua các khóa (keys)
# Cos 2 cách: trực tiếp và duyệt Sử dụng phương thức keys()
for key in countries.keys():
  print(key)

# Example 2: Using dict.values() method
# Duyệt qua các giá trị (values)
for value in countries.values():
  print(value)

# Example 3: Using dict.items() method
# Duyệt qua cả khóa và giá trị (items)
for key, value in countries.items():
  pair = f"{key} {value}"
  print(pair)

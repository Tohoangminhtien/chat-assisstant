# Chat Assistant

## 1. Giới thiệu
Chat Assistant là một ứng dụng trò chuyện thông minh được xây dựng bằng Python, sử dụng mô hình ngôn ngữ GPT-4o để tương tác với người dùng. Ứng dụng cung cấp giao diện web thân thiện thông qua Gradio và có khả năng thực hiện nhiều tác vụ hữu ích.

## 2. Tính năng
- **Chat thông minh**: Tương tác với người dùng thông qua mô hình GPT-4o
- **Tìm kiếm tin tức**: Cập nhật tin tức mới nhất từ các nguồn đáng tin cậy như Báo Thanh Niên
- **Đọc nội dung URL**: Khả năng tóm tắt nội dung từ các trang web được cung cấp
- **Đọc file PDF**: Phân tích và trích xuất thông tin từ tệp PDF

## 3. Cài đặt
### 3.1 Cài đặt với Python

1. Clone project

```console
git clone https://github.com/Tohoangminhtien/chat-assisstant.git
```

2. Cài đặt thư viện

```console
pip install -r requirements.txt
```

3. Chạy file app.py

```console
python app.py
```

4. Mở localhost
```console
http://localhost:7860/
```

### 3.2 Cài đặt với Docker (Recommend)
1. Pull từ Docker Hub
```console
docker pull tienthm/chat-assisstant:1.0
```
2. Run container
```console
docker run -p 7860:7860 tienthm/chat-assisstant:1.0
```

3. Mở localhost
```console
http://localhost:7860/
```
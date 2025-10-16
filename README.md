# 🧠 eLnda Quiz Extractor (EAUT)

### 📘 Giới thiệu

Công cụ **tự động thu thập và trích xuất toàn bộ câu hỏi – đáp án** từ **bài quiz trên hệ thống eLnda (EAUT)**.  
Chỉ cần dán **link bài quiz**, đăng nhập một lần, và công cụ sẽ **tự động quét toàn bộ nội dung**.

---

## ⚙️ Chức năng chính

✅ Tự quét tất cả câu hỏi trong quiz  
✅ Tự động loại bỏ định dạng thừa (A., B., C., D.)  
✅ Lưu toàn bộ nội dung ra file `quiz_text.txt` trong thư mục `output`  
✅ Giao diện dòng lệnh thân thiện, dễ sử dụng  
✅ Không cần sửa code – chỉ cần chạy là dùng được  

---

## 🧩 Cài đặt

Yêu cầu:
- Python ≥ 3.8  
- Google Chrome  
- ChromeDriver (phiên bản tương thích)

Cài đặt thư viện cần thiết:

```bash
pip install selenium beautifulsoup4
```

⚠️ Lưu ý:
Tải ChromeDriver tương ứng với bản Chrome của bạn tại:
👉 https://googlechromelabs.github.io/chrome-for-testing/

🚀 Cách sử dụng
1️⃣ Mở thư mục dự án
bash
Sao chép mã
cd answer-eaut
2️⃣ Chạy chương trình
bash
Sao chép mã
python run.py
3️⃣ Khi được hỏi:
Nhập link bài quiz:
Ví dụ:

ruby
Sao chép mã
https://elnda.eaut.edu.vn/mod/quiz/attempt.php?attempt=106566&cmid=3062&page=0
Nhập tổng số câu hỏi (nếu biết) → hoặc nhấn Enter để bỏ qua.

4️⃣ Khi trình duyệt Chrome mở lên → đăng nhập vào eLnda
Sau khi đã vào trang đầu tiên chứa câu hỏi → quay lại terminal và nhấn ENTER.

5️⃣ Chờ quá trình tự động hoàn tất
Kết quả sẽ được lưu tại:

bash
Sao chép mã
output/quiz_text.txt
📁 Cấu trúc dự án
css
Sao chép mã
📂 answer-eaut/
 ├── run.py             # File chạy chính
 ├── README.md          # Tài liệu hướng dẫn (bạn đang đọc đây)
 └── output/
      └── quiz_text.txt # File kết quả chứa toàn bộ câu hỏi + đáp án
🧠 Ví dụ đầu ra
text
Sao chép mã
Câu 1: Chủ nghĩa duy vật đã trải qua mấy hình thức phát triển trong lịch sử?
A. 2
B. 3
C. 4
D. 1

Câu 2: Trường phái triết học nào xem thường kinh nghiệm, xa rời thực tiễn?
A. Chủ nghĩa duy vật
B. Chủ nghĩa kinh viện
C. Chủ nghĩa kinh nghiệm
D. Chủ nghĩa duy tâm
✨ Thông tin
Tác giả: Nguyễn Thành Đạt
Phiên bản: v3.0
Mục tiêu: Hỗ trợ sinh viên EAUT trích xuất nội dung quiz để ôn luyện nhanh chóng.

💡 Hướng phát triển
 Xuất file .docx hoặc .xlsx

 Tự động nhận tiêu đề bài quiz để đặt tên file

 Giao diện đồ họa thân thiện hơn (GUI)

 Tích hợp nhận diện đáp án đúng

❤️ Góp ý & Đóng góp
Nếu bạn thấy dự án hữu ích, hãy ⭐ Star repo này nhé!
Mọi góp ý, báo lỗi hoặc ý tưởng phát triển thêm có thể gửi qua phần Issues trên GitHub.

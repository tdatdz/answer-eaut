# elnda_quiz_extractor_auto_v2.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time, os, re

print("🔗 Nhập link trang bạn cần copy (VD: https://elnda.eaut.edu.vn/mod/quiz/attempt.php?attempt=106566&cmid=3062&page=0)")
base_url = input("👉 Link: ").strip()

# Tách attempt và cmid từ link
match = re.search(r"attempt=(\d+).*?cmid=(\d+)", base_url)
if not match:
    print("❌ Không tìm thấy attempt hoặc cmid trong link. Vui lòng nhập đúng định dạng.")
    exit()

ATTEMPT_ID, CMID = match.groups()

# Hỏi tổng số câu hỏi (tùy chọn)
try:
    total_questions = input("🧮 Nhập tổng số câu hỏi (nếu biết, Enter để bỏ qua): ").strip()
    total_questions = int(total_questions) if total_questions else None
except:
    total_questions = None

# Tạo URL template
URL_TEMPLATE = f"https://elnda.eaut.edu.vn/mod/quiz/attempt.php?attempt={ATTEMPT_ID}&cmid={CMID}&page={{page}}"

# Cấu hình Chrome
opts = Options()
opts.add_argument("--start-maximized")
driver = webdriver.Chrome(options=opts)

print("\n🔑 Mở Chrome... Hãy đăng nhập vào eLnda và mở câu hỏi đầu tiên.")
driver.get(URL_TEMPLATE.format(page=0))
input("\n✅ Sau khi bạn đã đăng nhập và thấy câu hỏi đầu tiên, nhấn ENTER để bắt đầu quét...\n")

all_questions = []
page = 0

while True:
    print(f"➡️ Đang quét trang {page + 1} ...")
    driver.get(URL_TEMPLATE.format(page=page))
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    questions = soup.select(".que")

    if not questions:
        print("⛔ Không còn câu hỏi trên trang này. Dừng lại.")
        break

    for q in questions:
        qtext_div = q.select_one(".qtext")
        question_text = qtext_div.get_text(" ", strip=True) if qtext_div else "(Không lấy được câu hỏi)"

        ans_container = q.select_one(".answer")
        option_texts = []

        if ans_container:
            # Cố gắng lấy từng lựa chọn
            for child in ans_container.find_all(recursive=False):
                txt = child.get_text(" ", strip=True)
                if txt:
                    option_texts.append(txt)

            if not option_texts:
                for lab in ans_container.select("label"):
                    txt = lab.get_text(" ", strip=True)
                    if txt:
                        option_texts.append(txt)

            if not option_texts:
                for inp in ans_container.select("input[type='radio'], input[type='checkbox']"):
                    idattr = inp.get("id")
                    lab = ans_container.find("label", {"for": idattr}) if idattr else None
                    if not lab:
                        lab = inp.parent
                    txt = lab.get_text(" ", strip=True) if lab else ""
                    if txt:
                        option_texts.append(txt)

        # Loại trùng
        seen = set()
        deduped = []
        for t in option_texts:
            if t not in seen:
                deduped.append(t)
                seen.add(t)

        # Ghi kết quả
        text_block = f"Câu hỏi (trang {page + 1}): {question_text}\n"
        if deduped:
            for i, choice in enumerate(deduped, start=1):
                label = chr(64 + i)
                text_block += f"   {label}. {choice}\n"
        else:
            text_block += "   (Không tìm thấy lựa chọn)\n"

        text_block += "\n"
        all_questions.append(text_block)

        # Nếu người dùng nhập tổng số câu hỏi → dừng khi đủ
        if total_questions and len(all_questions) >= total_questions:
            print(f"✅ Đã thu thập đủ {total_questions} câu hỏi. Dừng lại.")
            questions = []  # ép thoát vòng ngoài
            break

    if not questions:
        break

    page += 1

driver.quit()

# Ghi file
os.makedirs("output", exist_ok=True)
outpath = os.path.join("output", "quiz_text.txt")

with open(outpath, "w", encoding="utf-8") as f:
    for q in all_questions:
        f.write(q + "\n")

print(f"\n✅ Đã trích xuất {len(all_questions)} câu hỏi.")
print(f"📁 File kết quả: {outpath}")
print("\n🧠 Code by @dsut/Nguyen Thanh Dat")

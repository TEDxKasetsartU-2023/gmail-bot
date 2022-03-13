# Gmail Bot
## วิธีติดตั้ง
1. ทำการติดตั้ง Python จาก[เว็บไซต์ของ Python](https://www.python.org/downloads/)
2. ติดตั้ง git จาก[เว็บไซต์ของ Git](https://git-scm.com/downloads)
3. ติดตั้ง gh cli โดยทำตาม[เว็บไซต์นี้](https://github.com/cli/cli)
4. ใช้คำสั่ง `gh auth login` เพื่อ login จากนั้นใช้คำสั่ง `gh repo clone TEDxKasetsartU-2023/gmail-bot` เพื่อดาวน์โหลดโค้ด
5. ใช้คำสั่ง `python -m pip install -r requirement.txt` เพื่อติดตั้ง module ทั้งหมด

หากยังไม่มี project ใน google cloud ให้ทำตามขั้นตอนต่อไปนี้ ถ้ามีแล้วให้ข้ามไปข้อ 7

6. ไปที่ [console.cloud.google.com](console.cloud.google.com) และสร้าง Project

หากมี `credentials.json` แล้วให้ข้ามไปข้อ 13

7. จาหนั้นค้นหา **Gmail API** จากนั้นกด **Enable**
8. ไปที่ **APIs & Services** > **Credentials** จากนั้นกด **CREATE CREDENTIALS** เลือก **OAuth client ID**
9. เลือก **Desktop** ตั้งชื่อตามต้องการ จากนั้นกด **CREATE**
10. กด **DOWNLOAD JSON** ตั้งชื่อว่า `credentials.json` และบันทึกไว้ในโปลเดอร์เดียวกับโค้ด

## การใช้งาน
### ไฟล์ที่จำเป็น
### วิธีใช้

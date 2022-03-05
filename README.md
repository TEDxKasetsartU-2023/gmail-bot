# Gmail Bot
## วิธีติดตั้ง และใช้งานเบื้องต้น
1. ทำการติดตั้ง Python จาก[เว็บไซต์ของ Python](https://www.python.org/downloads/)
2. ติดตั้ง git จาก[เว็บไซต์ของ Git](https://git-scm.com/downloads)
3. ติดตั้ง gh cli โดยทำตาม[เว็บไซต์นี้](https://github.com/cli/cli)
4. ใช้คำสั่ง `gh auth login` เพื่อ login จากนั้นใช้คำสั่ง `gh repo clone TEDxKasetsartU-2023/gmail-bot` เพื่อดาวน์โหลดโค้ด
5. ใช้คำสั่ง `python -m pip install -r requirement.txt` เพื่อติดตั้ง module ทั้งหมด
6. สร้างไฟล์ชื่อ `mail_list.csv` จากนั้นใส่ชื่อ และอีเมล ที่ต้องการส่งลงไป โดยให้ชื่ออยู่คอลัมน์แรก และอีเมล อยู่คอลัมน์ที่สอง
7. ใน `content.html` สามารถแก้ไขได้ตามที่ต้องการจะส่ง

หากยังไม่มี project ใน google cloud ให้ทำตามขั้นตอนต่อไปนี้ ถ้ามีแล้วให้ข้ามไปข้อ 9

8. ไปที่ [console.cloud.google.com](console.cloud.google.com) และสร้าง Project

หากมี `credentials.json` แล้วให้ข้ามไปข้อ 13

9. จาหนั้นค้นหา **Gmail API** จากนั้นกด **Enable**
10. ไปที่ **APIs & Services** > **Credentials** จากนั้นกด **CREATE CREDENTIALS** เลือก **OAuth client ID**
11. เลือก **Desktop** ตั้งชื่อตามต้องการ จากนั้นกด **CREATE**
12. กด **DOWNLOAD JSON** ตั้งชื่อว่า `credentials.json` และบันทึกไว้ในโปลเดอร์เดียวกับโค้ด
13. ใช้คำสั่ง `python main.py` เพื่อทำการส่งอีเมลไปที่เป้าหมายที่อยู่ในไฟล์ `mail_list.csv`
14. ระหว่างการส่งจะมีการเก็บผลลัพธ์ไว้ในไฟล์ `result.csv` โดยแต่ละแถวจะประกอบไปด้วย ชื่อ, อีเมล, SENT และ Timestamp ตามลำดับ

**_หมายเหตุ_**:
1. การทำงานของโค้ดจะมีการแทรกรูปเข้าไปโดยมี `Content ID` เป็น `image1` โดยจะแทรกรูป `TEDxKasetsartU_square.jpg` ลงไป
2. โค้ดจะเปลี่ยน `~~~` ใน `content.html` เป็นชื่อจากไฟล์ `mail_list.csv`

## CSV
csv หรือ comma seperated value คือรูปแบบการเก็บข้อมูลแบบหนึ่ง โดยการเก็บข้อมูลจะเป็นลัหษณะของตาราง โดยที่แต่ละบรรทัดคือแต่ละแถว และแต่ละคอลัมน์จะถูกคั่นด้วย `,` หรือ comma นั่นเอง (ไม่ควรมีการเว้นวรรคใด ๆ หน้า หรือหลัง `,` ยกเว้นแต่เป็นข้อมูล)

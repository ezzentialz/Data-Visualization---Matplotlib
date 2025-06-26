# 1. Import Library ที่จำเป็น
import matplotlib.pyplot as plt

# --- ส่วนโค้ดสำหรับรองรับภาษาไทย (เหมือนเดิม) ---
plt.rcParams['font.family'] = 'Angsana New' # หรือชื่อฟอนต์ที่ลูกใช้
plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = False
# ----------------------------------------

# 2. เตรียมข้อมูล (ในที่นี้คือสัดส่วนค่าใช้จ่ายรายเดือน)
expenses = [5000, 3000, 1500, 1000, 500] # ค่าใช้จ่ายแต่ละหมวดหมู่
categories = ['ค่าอาหาร', 'ค่าเดินทาง', 'ค่าเช่า', 'ค่าบันเทิง', 'อื่นๆ'] # ชื่อหมวดหมู่

# 3. สร้างกราฟวงกลม (plt.pie)
# ในการสร้าง Pie Chart จะมี ***** wedges , texts, autotexts*** ใช้สำหรับปรับเปลี่ยนค่า/ตกแต่ง/ไฮไลท์
#wedges = คือชิ้นส่วนของ Pie chart เช่น ชิ้นส่วน'ค่าอาหาร', ชิ้นส่วน'ค่าเดินทาง', ชิ้นส่วน'ค่าเช่า', ชิ้นส่วน'ค่าบันเทิง', ชิ้นส่วน'อื่นๆ' ทั้งหมด 5 wedge ตามindex
#texts = คือส่วนของtextที่เป็น ชื่อป้ายกำกับ label 'ค่าอาหาร', 'ค่าเดินทาง', 'ค่าเช่า', 'ค่าบันเทิง', 'อื่นๆ'
#autotexts = คือtextของค่าเปอร์เซนต์

# autopct='%1.1f%%' คือการบอกให้แสดงเปอร์เซ็นต์เป็นทศนิยม 1 ตำแหน่ง
wedges, texts, autotexts = plt.pie(expenses, labels=categories, autopct='%1.2f%%', startangle=106.5, colors=plt.cm.Set3.colors, explode=[0.2,0,0,0,0])


#สมมุติว่าเราอยากให้ 'ค่าอาหาร' ที่แยกออกมา มีขอบสีดำ เด่นชัด ให้ใช้ตัว wedge เพื่อตกแต่งตัว pie chart นั้น
#A. เราต้องกำหนด index ให้ตัวแปร food_wedge ก่อน
food_wedge = 0 #สมมุติ ว่ารู้index อยู่แล้ว
#B. เมื่อกำหนด index แล้ว ให้เข้าถึง wedge[index/ตัวแปร food_wedge] แล้วก็ปรับแต่ง
wedges[food_wedge].set_edgecolor('black') #กำหนด wedges[index0 = 'ค่าอาหาร'] ให้เป็นสีดำ
wedges[food_wedge].set_linewidth(2.0) #กำหนด wedges[index0 = 'ค่าอาหาร']ให้มีเส้นขอบ 1.5

#สมมุติ ว่าอยากเปลี่ยน ขนาดfont ตัวเปอร์เซนต์
if 'ค่าอาหาร' in categories: #กรณีที่ไม่รู้ index แต่รู้ ชื่อหมวดหมู่
    food_autotexts = categories.index('ค่าอาหาร')
    print(food_autotexts) #Debug : ลองหาindex ด้วยการลูปชื่อในcategories output = 0 เก็บเข้าตัวแปรชื่อ food_autotexts
    autotexts[food_autotexts].set_fontsize(25)
    autotexts[food_autotexts].set_fontweight('extra bold')
    autotexts[food_autotexts].set_color('red')



# 4. เพิ่มรายละเอียดให้กับกราฟ
plt.title('สัดส่วนค่าใช้จ่ายรายเดือน') # ชื่อกราฟ

# 5. จัดรูปทรงให้วงกลมไม่บิดเบี้ยว
plt.axis('equal') # ทำให้กราฟเป็นวงกลมที่แท้จริง

# 6. แสดงกราฟ
plt.show()
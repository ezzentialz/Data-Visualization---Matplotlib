# 1. Import Library ที่จำเป็น
import matplotlib.pyplot as plt
import numpy as np # *** ต้อง import numpy เพิ่มเติม เพื่อช่วยในการจัดการตัวเลขและตำแหน่งกราฟ ***

# --- ส่วนโค้ดสำหรับรองรับภาษาไทย (เหมือนเดิม) ---
plt.rcParams['font.family'] = 'Angsana New'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = False
# ----------------------------------------

# 2. เตรียมข้อมูล (ในที่นี้คือยอดขายของแต่ละทีม)
teams = ['ทีม Alpha', 'ทีม Beta', 'ทีม Gamma', 'ทีม Delta']
highest_sales_per_team = [15.2, 18.5, 12.8, 20.1]
lowest_sales_per_team = [8.1, 15.2, 9.5, 15.6]

# 3. กำหนดตำแหน่งบนแกน X และความกว้างของแท่งกราฟ
num_teams = len(teams)
bar_width = 0.35 # ความกว้างของแต่ละแท่ง
# สร้างตำแหน่งสำหรับแต่ละกลุ่มของแท่งกราฟ (เช่น 0, 1, 2, 3)
r1 = np.arange(num_teams)

# สร้างตำแหน่งสำหรับแท่งแรก (เลื่อนไปทางซ้าย)
r2 = [x + bar_width for x in r1] # r2 คือตำแหน่งของแท่งที่สอง (เลื่อนไปทางขวา)

# 4. สร้างกราฟแท่งแบบ Grouped Bar Chart
# สร้าง Figure และ Axes Object เพื่อควบคุมกราฟได้ละเอียดขึ้น
fig, ax = plt.subplots(figsize=(10, 6)) # กำหนดขนาดกราฟให้ใหญ่ขึ้นนิดหน่อยเพื่อให้อ่านง่าย

# แท่งกราฟสำหรับยอดขายสูงสุด
bars1 = ax.bar(r1, highest_sales_per_team, color='skyblue', width=bar_width,
               edgecolor='grey', label='ยอดขายสูงสุด')

# แท่งกราฟสำหรับยอดขายต่ำสุด
bars2 = ax.bar(r2, lowest_sales_per_team, color='lightcoral', width=bar_width,
               edgecolor='grey', label='ยอดขายต่ำสุด')


# 5. เพิ่มรายละเอียดให้กับกราฟ
ax.set_xlabel('ทีม', fontsize=14)
ax.set_ylabel('ยอดขาย (ล้านบาท)', fontsize=14)
ax.set_title('เปรียบเทียบยอดขายสูงสุดและต่ำสุดของแต่ละทีม', fontsize=16)

# กำหนดตำแหน่งของ ticks บนแกน X ให้อยู่กึ่งกลางระหว่างแท่งกราฟสองแท่ง
ax.set_xticks([x + bar_width /2  for x in r1])

# กำหนดป้ายกำกับของ ticks บนแกน X (ชื่อทีม)
ax.set_xticklabels(teams)

# เพิ่ม Legend (คำอธิบายกราฟ) เพื่อบอกว่าแท่งสีไหนคืออะไร
ax.legend()

# เพิ่ม Grid Lines (ไม่บังคับ แต่ช่วยให้อ่านง่ายขึ้น)
ax.yaxis.grid(True, linestyle='--', alpha=0.6) # Grid lines สำหรับแกน Y

# 6. แสดงกราฟ
plt.tight_layout() # ปรับ layout ของกราฟให้พอดี
plt.show()
# 1. Import Library ที่จำเป็น
import matplotlib.pyplot as plt
import numpy as np # จำเป็นสำหรับ bar chart แบบกลุ่ม

# --- ส่วนโค้ดสำหรับรองรับภาษาไทย (เหมือนเดิม) ---
plt.rcParams['font.family'] = 'Angsana New'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = False
# ----------------------------------------

# 2. เตรียมข้อมูลสำหรับกราฟ Line Chart (จากโจทย์ที่ 1)
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
deliveries_in_millions = [10.5, 12.2, 11.8, 14.0]

# เตรียมข้อมูลสำหรับกราฟ Bar Chart (จากโจทย์ที่ 2)
teams = ['ทีม Alpha', 'ทีม Beta', 'ทีม Gamma', 'ทีม Delta']
highest_sales_per_team = [15.2, 18.5, 12.8, 20.1]
lowest_sales_per_team = [8.1, 15.2, 9.5, 15.6]

# --- ส่วนของการจัดการข้อมูล Bar Chart (เรียงลำดับ) ---
team_sale_zip = list(zip(teams, highest_sales_per_team, lowest_sales_per_team))
sorted_team_sale = sorted(team_sale_zip, key=lambda x: x[1], reverse=True)
sorted_teams = [n[0] for n in sorted_team_sale]
sorted_high_sales = [n[1] for n in sorted_team_sale]
sorted_low_sales = [n[2] for n in sorted_team_sale]

# ข้อมูล pie chart
expenses = [5000, 3000, 1500, 1000, 500] # ค่าใช้จ่ายแต่ละหมวดหมู่
categories = ['ค่าอาหาร', 'ค่าเดินทาง', 'ค่าเช่า', 'ค่าบันเทิง', 'อื่นๆ'] # ชื่อหมวดหมู่
# ----------------------------------------------------

# 3. สร้าง Figure และ Axes Objects (1 แถว 2 คอลัมน์ = 2 กราฟวางข้างกัน)
fig, axes = plt.subplots(1,3, figsize=(15, 6)) # figsize กำหนดขนาดรวมของทั้งรูป

# --- วาดกราฟแรก: Line Chart (บน axes[0]) ---
ax1 = axes[0] # กำหนดให้ ax1 คือพื้นที่วาดกราฟตัวแรก

# วาดเส้นกราฟ
ax1.plot(quarters, deliveries_in_millions, marker='s', color='green', label='ปริมาณพัสดุต่อไตรมาส')

# ไฮไลท์ Q4 (เหมือนที่ลูกทำในโจทย์ 1)
q4_highlight_index = quarters.index('Q4')
ax1.plot(quarters[q4_highlight_index], deliveries_in_millions[q4_highlight_index],
         marker='s', markersize=12, color='red', label=f"ปริมาณพัสดุสูงสุด {quarters[q4_highlight_index]}")

# เพิ่มรายละเอียดกราฟแรก
ax1.set_title('แนวโน้มปริมาณพัสดุที่จัดส่งรายไตรมาส ปี 2024')
ax1.set_xlabel('ไตรมาส')
ax1.set_ylabel('ปริมาณพัสดุ (ล้านชิ้น)')
ax1.grid(axis='y', color='lightgray', linestyle='--', alpha=0.4)
ax1.legend()


# --- วาดกราฟที่สอง: Grouped Bar Chart (บน axes[1]) ---
ax2 = axes[1] # กำหนดให้ ax2 คือพื้นที่วาดกราฟตัวที่สอง

# กำหนดตำแหน่งและ bar_width สำหรับ Grouped Bar Chart
num_teams = len(sorted_teams)
bar_width = 0.35
r1 = np.arange(num_teams)
r2 = [x + bar_width for x in r1]

# วาดแท่งกราฟสำหรับยอดขายสูงสุดและต่ำสุด
ax2.bar(r1, sorted_high_sales, color='skyblue', width=bar_width, edgecolor='grey', label='ยอดขายสูงสุด')
ax2.bar(r2, sorted_low_sales, color='lightcoral', width=bar_width, edgecolor='grey', label='ยอดขายต่ำสุด')

# เพิ่มรายละเอียดกราฟที่สอง
ax2.set_xlabel('ทีม')
ax2.set_ylabel('ยอดขาย (ล้านบาท)')
ax2.set_title('เปรียบเทียบยอดขายสูงสุดและต่ำสุดของแต่ละทีม')
ax2.set_xticks([x + bar_width / 2 for x in r1])
ax2.set_xticklabels(sorted_teams)
ax2.legend()
ax2.yaxis.grid(True, linestyle='--', alpha=0.6)



ax3 = axes[2]

wedges, texts, autotexts = ax3.pie(expenses, labels=categories, autopct='%1.2f%%', startangle=106.5, colors=plt.cm.Set3.colors, explode=[0.2,0,0,0,0])

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
    
ax3.axis('equal') # ทำให้กราฟเป็นวงกลมที่แท้จริง    

# 4. ปรับ Layout และแสดงกราฟ
plt.tight_layout() # ปรับระยะห่างระหว่าง Subplots อัตโนมัติ
plt.show()
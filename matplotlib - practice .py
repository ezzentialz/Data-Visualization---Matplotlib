#โจทย์ที่ 1: การวิเคราะห์แนวโน้ม (Plot Chart)
#สถานการณ์: ลูกทำงานในบริษัทจัดส่งพัสดุและต้องการวิเคราะห์แนวโน้มปริมาณพัสดุที่จัดส่งในแต่ละไตรมาสของปี 2024

import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Angsana New'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
deliveries_in_millions = [10.5, 12.2, 11.8, 14.0]

plt.plot(quarters, deliveries_in_millions, marker = 's', color='green', label = 'ปริมาณพัสดุต่อไตรมาส')

#เข้าถึง index Q4
q4_highlight = 'Q4'
if 'Q4' in quarters:
    q4_highlight = quarters.index(q4_highlight)
    #print(q4_highlight) #debug : เช็ค index output = 3
    
#กำหนด ตัวแปร รับ index q4
quarters_q4_only = quarters[q4_highlight]
delivers_q4_only = deliveries_in_millions[q4_highlight]
#print(quarters_q4_only) #debug : เช็ค
    
#กำหนด plt.plot สี ขนาด
plt.plot(quarters_q4_only, delivers_q4_only,
         marker = 's',
         markersize = 12,
         color = 'red',
         label = f"ปริมาณพัสดุสูงสุด {q4_highlight}"
         )

plt.grid(axis='y', color = 'lightgray', linestyle = '--', alpha= 0.4)

plt.title('แนวโน้มปริมาณพัสดุที่จัดส่งรายไตรมาส ปี 2024')
plt.xlabel('ไตรมาส')
plt.ylabel('ปริมาณพัสดุ (ล้านชิ้น)')

plt.legend()

plt.show()



#----------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np

#โจทย์ที่ 2: การเปรียบเทียบประสิทธิภาพ (Bar Chart)
#สถานการณ์: ลูกกำลังวิเคราะห์ประสิทธิภาพของทีมขาย 4 ทีมในเดือนที่ผ่านมา เพื่อดูว่าทีมใดทำยอดขายได้สูงสุด

teams = ['ทีม Alpha', 'ทีม Beta', 'ทีม Gamma', 'ทีม Delta']
sales_per_team = [15.2, 18.5, 12.8, 20.1]
lowest_sales_per_team = [8.1, 15.2, 9.5, 15.6]

#เรียงลำดับ ทีมตามยอดขายจาก มากไปน้อย ก่อนนำไปสร้างกราฟ
#zip
team_sale_zip = list(zip(teams,sales_per_team,lowest_sales_per_team))
#print(team_sale_zip) #debug: เช็คข้อมูล zip

#เรียง
sorted_team_sale = sorted(team_sale_zip, key = lambda x  : x[1] , reverse=True)
print(sorted_team_sale) #debug: เช็คข้อมูลจากการเรียงมากไปน้อย

#unzip
sorted_team = [n[0] for n in sorted_team_sale]
sorted_high_sales = [n[1] for n in sorted_team_sale]
sorted_low_sales = [n[2] for n in sorted_team_sale]

print(sorted_team) #Debug : เช็คการ unzip
print(sorted_high_sales) #Debug : เช็คการ unzip
print(sorted_low_sales) #Debug : เช็คการ unzip

# 3. กำหนดตำแหน่งบนแกน X และความกว้างของแท่งกราฟ
num_team = len(sorted_team)
bar_width = 0.3 # ระยะกว้าง ระหว่าง ทีม ยิ่งตัวเลขเยอะ ยิ่งเข้ามาใกล้กัน

# สร้างตำแหน่งสำหรับแต่ละกลุ่มของแท่งกราฟ (เช่น 0, 1, 2, 3)
position1 = np.arange(num_team) #ใช้ Numpy จัดตำแหน่ง ของ 'sorted_team' 
print(position1) #debug : ได้ตำแหน่ง ของแท่งกราฟ 0, 1, 2, 3

# สร้างตำแหน่งสำหรับแท่งแรก (เลื่อนไปทางซ้าย)
position2 = [x + bar_width for x in position1] # กำหนก ให้ตำแหน่งแท่งที่2 = (ตำแหน่ง1+ bar_width(0.35))
print(position2) #debug : ได้ตำแหน่งที่ 2 ของแท่งกราฟ 0,1,2,3

#สร้างกราฟแท่งแบบ Grouped Bar Chart
#สร้าง Figure และ Axes Object เพื่อควบคุมกราฟได้ละเอียดขึ้น
fig, ax = plt.subplots(figsize = (10,6)) # ตรงนี้ คือการสร้างกราฟ และ (figกำหนดความกว้าง) และ (axes สูง)

# แท่งกราฟสำหรับยอดขายสูงสุด
high_sale_bar = ax.bar(position1, sorted_high_sales, color= 'blue', width=bar_width, edgecolor= 'black', label= 'ยอดขายสูงสุด')

# แท่งกราฟสำหรับยอดขายต่ำสุด
low_sale_bar = ax.bar(position2, sorted_low_sales, color = 'red', width= bar_width, edgecolor= 'lightgray', label= 'ยอดขายต่ำสุด' )

#เพิ่มรายละเอียดให้กับกราฟ ใช้ axe แทน plt.bar
ax.set_title("ยอดขายของแต่ละทีมในเดือนที่ผ่านมา")
ax.set_xlabel("ทีม")
ax.set_ylabel("ยอดขาย (ล้านบาท)")

#กำหนดตำแหน่ง label 
ax.set_xticks([x + bar_width /2 for x in position1])

# กำหนดป้ายlabel ให้อยู่พอดีกับ ตำแหน่ง x
ax.set_xticklabels(sorted_team)

# legend ใช้ตัวนี้
ax.legend()

#ทำให้กราฟมีขนาดพอดี
plt.tight_layout()

#ส่วนด้านล่างจะ คอมเม้นออกหมด เพราะเราใช้ group bar chart
'''
# สร้างกราฟ Bar Chart (กราฟแท่งแนวตั้ง)
bars = plt.bar(sorted_team, sorted_sales, color = 'lightblue')

#ให้แท่งกราฟของทีมที่มียอดขาย สูงสุด มี สีส้ม (orange) และมีขอบสีดำ (black) หนา 2.0
if 'ทีม Delta' in sorted_team: #หลังจากที่มีการเช็ค sorted_team ทำให้รู้ว่า ตำแหน่งแรกสุดชื่อว่า ทีม Delta
    highest_sales_team = sorted_team.index('ทีม Delta')
   # print(highest_sales_team) #debug : เช็คตำแหน่ง index
    bars[highest_sales_team].set_color('orange')
    bars[highest_sales_team].set_edgecolor('black')
    bars[highest_sales_team].set_linewidth(2.0)

#ตั้งชื่อกราฟว่า "ยอดขายของแต่ละทีมในเดือนที่ผ่านมา"
plt.title("ยอดขายของแต่ละทีมในเดือนที่ผ่านมา")

#ตั้งชื่อแกน X ว่า "ทีม"
plt.xlabel("ทีม")

#ตั้งชื่อแกน Y ว่า "ยอดขาย (ล้านบาท)"
plt.ylabel("ยอดขาย (ล้านบาท)")
'''

plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------------

#โจทย์ที่ 3: การวิเคราะห์สัดส่วน (Pie Chart)
#สถานการณ์: ลูกกำลังวิเคราะห์ว่าลูกค้าเลือกชำระเงินผ่านช่องทางใดมากที่สุดในระบบ E-commerce ของบริษัท

payment_methods = ['บัตรเครดิต', 'โอนเงิน', 'TrueMoney Wallet', 'เก็บเงินปลายทาง']
transactions_count = [3500, 2500, 1500, 500]

#สร้าง pie chart กำหนด wedges, texts, autotexts เผื่อไว้ก่อน สำหรับปรับแต่ง
wedges, texts, autotexts = plt.pie(transactions_count, labels=payment_methods, startangle= 90, autopct='%1.1f%%', explode=(0.15,0,0,0), colors=plt.cm.Set3.colors)

#ให้ชิ้นส่วน 'บัตรเครดิต' ที่ explode ออกมามี ขอบสีดำ (black) หนา 1.0 (linewidth=1.0)
if 'บัตรเครดิต' in payment_methods:
    credit_card = payment_methods.index('บัตรเครดิต')
    print(credit_card) # Debug: เช็คindex 
    
wedges[credit_card].set_edgecolor('black')
wedges[credit_card].set_linewidth(1.0)
# ให้ข้อความ เปอร์เซ็นต์ ของชิ้นส่วน 'บัตรเครดิต' มี ขนาดฟอนต์ 16 และเป็น ตัวหนา (bold)
autotexts[credit_card].set_fontsize(16)
autotexts[credit_card].set_fontweight('bold')

#ตั้งชื่อกราฟว่า "สัดส่วนช่องทางการชำระเงิน"
plt.title("สัดส่วนช่องทางการชำระเงิน")

#ทำให้ pie chart มีขนาด กลม
plt.axis('equal')

plt.show()

    





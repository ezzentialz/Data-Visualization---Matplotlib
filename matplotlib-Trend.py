# 1. Import Library ที่จำเป็น
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Angsana New' #ตรงนี้คือการระบุให้ใช่พร้อนไทย ลงใน matplotlib
plt.rcParams['font.size'] = 14 #กำหนดขนาดfont
plt.rcParams['axes.unicode_minus'] = False # แก้ปัญหาสัญลักษณ์ลบ

# 2. เตรียมข้อมูล (ในที่นี้คือยอดขายไอศกรีมในแต่ละเดือน)
months = ['ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ส.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.']
ice_cream_sales = [100, 120, 150, 180, 220, 250, 230, 200, 170, 140, 110, 90]

# 3. สร้างกราฟเส้นแยก เพราะต้องการระบุ สีเส้น รูปแบบเส้น ความชัดของเส้น และ label(กรอบ สี่เหลี่ยมที่มีข้อความ)
plt.plot(months, ice_cream_sales,
            color = 'gray',
            linestyle = ':',
            alpha = 0.4,
            label='ยอดขายเฉลี่ย',
            )
# 3.1 สร้าง markerแยก เพราะต้องการระบุ รูปแบบ ขนาด ขอบสี พื้นสี และ***ไม่ต้องมีเส้น*** เพราะจะเอาแค่ marker
plt.plot(months, ice_cream_sales,
         marker = 'o',
         markersize = 8,
         markeredgecolor = 'blue',
         markerfacecolor = 'blue',
         linestyle = 'None'
         )

#ลองดูครับ อยากให้ เฉพาะตำแหน่ง 'มิ.ย.' มีความแตกต่างจากอันอื่น
month_to_highlight = 'มิ.ย.'
if month_to_highlight in months:
    #หาindex ก่อน
    highlight_index = months.index(month_to_highlight)
    print(highlight_index) #Debug: ดูindex ครับ output = 5
    
    #เมื่อได้ index แล้วกำหนด indexให้กับ ข้อมูล เพื่อที่จะให้ไฮไลท์ โดยสร้างตัวแปรใหม่มารับค่า
    highlight_months = months[highlight_index] #months[5]
    highlight_ice_cream = ice_cream_sales[highlight_index] #ice_cream_sales[5]
    
    #กำหนดค่าต่างๆ ให้โดยเฉพาะ ตำแหน่ง  highlight_index
    plt.plot(highlight_months,highlight_ice_cream,
             marker = 'o', # กำหนด marker เป็น o เพราะ ถ้าเป็น x แล้ว ขนาดมันเล็กไป 
             color = 'red', # กำหนด ให้มีสีแดง
             markersize = 15, # กำหนด ขนาด marker
             markeredgecolor = 'black', #กำหนดขอบสีของ  marker เป็นสีดำ
             label=f'จุดเด่น: {month_to_highlight}' # เพิ่ม label สำหรับ legend
             )
    

# 4. เพิ่มรายละเอียดให้กับกราฟ
plt.title('ยอดขายไอศกรีมรายเดือนในปี 2024') # ชื่อกราฟ
plt.xlabel('เดือน') # ป้ายกำกับแกน X
plt.ylabel('ยอดขาย (หน่วย)') # ป้ายกำกับแกน Y

# เพิ่ม Legend (คำอธิบาย) เพื่อบอกว่าเส้นไหนคืออะไร จุดไหนคืออะไร
plt.legend()

# 5. เพิ่ม Grid Line เข้าไปในกราฟ เพื่อดูรายละเอียดมากขึ้น ***สำคัญ หากต้องการระบุเฉพาะแนวตั้งหรือแนวนอน 
# ให้เขียนใน plt.grid() บันทัดเดียว หากแยกจะเป็นการเซ็ตให้กับทั้งหมด***
'''
plt.grid(axis='y') # แสดงเฉพาะ แนวนอน
plt.grid(axis= 'x') # แสดงเฉพาะ แนวตั้ง
plt.grid(linestyle = '--') #กำหนดรูปแบบเส้น grid
plt.grid(alpha = 0.2) #ความชัดของเส้น โดย 0.0 ถึง 1.0  (1.0 = ชัดสุด)
plt.grid(color = 'red')
'''
plt.grid(axis='y', linestyle = '--', alpha = 0.7, color ='gray')
plt.grid(axis='x', linestyle = '--', alpha = 0.1, color = 'gray')

# 5. แสดงกราฟ
plt.show()

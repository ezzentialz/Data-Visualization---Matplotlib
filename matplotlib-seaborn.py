import matplotlib.pyplot as plt
import pandas as pd # เราจะใช้ Pandas DataFrame เพื่อแสดงประสิทธิภาพของ Seaborn
import seaborn as sns # *** Import Seaborn ***

# --- ส่วนโค้ดสำหรับรองรับภาษาไทย (เหมือนเดิม) ---
plt.rcParams['font.family'] = 'Angsana New'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = False
# ----------------------------------------

# 1. เตรียมข้อมูล (ในรูปของ Pandas DataFrame เพื่อให้ Seaborn ทำงานได้ดี)
data = {
    'Math_Score': [85, 90, 70, 75, 92, 60, 88, 95, 65, 78],
    'Science_Score': [80, 92, 72, 70, 90, 65, 85, 98, 60, 75],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
}
df = pd.DataFrame(data)

print("--- ข้อมูลตัวอย่าง (DataFrame) ---")
print(df)

# --- ตัวอย่างที่ 1: Scatter Plot ด้วย Matplotlib ---
print("\n--- Scatter Plot ด้วย Matplotlib ---")
plt.figure(figsize=(8, 6)) # สร้าง Figure แยกกันเพื่อแสดงกราฟ
plt.scatter(df['Math_Score'], df['Science_Score'], color='blue', alpha=0.7)
plt.title('คะแนนคณิตศาสตร์ vs วิทยาศาสตร์ (Matplotlib)')
plt.xlabel('คะแนนคณิตศาสตร์')
plt.ylabel('คะแนนวิทยาศาสตร์')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


# --- ตัวอย่างที่ 2: Scatter Plot ด้วย Seaborn ---
print("\n--- Scatter Plot ด้วย Seaborn ---")
plt.figure(figsize=(8, 6)) # สร้าง Figure แยกกัน
sns.scatterplot(x='Math_Score', y='Science_Score', data=df, hue='Gender', style='Gender', s=100, alpha=0.8) # s คือขนาดของจุด
plt.title('คะแนนคณิตศาสตร์ vs วิทยาศาสตร์ (Seaborn)')
plt.xlabel('คะแนนคณิตศาสตร์')
plt.ylabel('คะแนนวิทยาศาสตร์')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title='เพศ') # สามารถกำหนด title ให้ legend ได้
plt.show()

# --- ตัวอย่างที่ 3: กราฟประเภทอื่น ๆ ที่ Seaborn เก่ง (เช่น Pair Plot) ---
# Pair Plot: แสดงความสัมพันธ์ของทุกคู่ตัวแปรใน DataFrame
# ใช้เวลาประมวลผลนานขึ้นถ้าข้อมูลใหญ่
print("\n--- Pair Plot ด้วย Seaborn (แสดงความสัมพันธ์หลายตัวแปร) ---")
# sns.pairplot(df, hue='Gender') # จะสร้างกราฟเยอะหน่อย (ทุกคู่ของคอลัมน์ตัวเลข)
# plt.suptitle('Pair Plot ของคะแนนและเพศ', y=1.02) # ตั้งชื่อรวมของ Pair Plot
# plt.show()

# ถ้าไม่อยากเห็นกราฟเยอะเกินไป ให้ลองใช้ displot หรือ histplot แทน
print("\n--- Displot (Histogram + KDE) ด้วย Seaborn ---")
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Math_Score', kde=True, hue='Gender') # kde=True จะวาดเส้นประมาณการกระจายตัวของข้อมูลด้วย
plt.title('การกระจายตัวของคะแนนคณิตศาสตร์ (Seaborn)')
plt.xlabel('คะแนนคณิตศาสตร์')
plt.ylabel('ความถี่')
plt.show()

print("\n--- Boxplot ด้วย Seaborn ---")
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Gender', y='Math_Score', palette='viridis') # แสดงการกระจายตัวของข้อมูลสำหรับแต่ละกลุ่ม (เพศ)
plt.title('การกระจายตัวของคะแนนคณิตศาสตร์ตามเพศ (Seaborn)')
plt.xlabel('เพศ')
plt.ylabel('คะแนนคณิตศาสตร์')
plt.show()
import csv


_rows = []
with open('daily_stock_3535.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        _rows.append(row)


for i in range(len(_rows[1:])):
    if(i+2 >= len(_rows)):
        print(i)
        break
    _rows[i+1].append(_rows[i+2][3])
_rows[0].append('next_open')
_rows = _rows[:len(_rows)-1]
with open('daily_stock_3535_2.csv', 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    writer.writerows(_rows)

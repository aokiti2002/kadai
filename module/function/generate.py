import random

def employee_info(company_name, company_employees_number):
    data = []

    surnames = ["佐藤", "鈴木", "高橋", "田中", "渡辺", "伊藤", "山本", "中村", "小林", "加藤", "吉田", "山田", "佐々木", "山口", "松本", "井上", "木村", "林", "斎藤", "清水", "山﨑", "森", "池田", "橋本", "阿部", "石川", "山下", "中島", "石井", "小川", "前田", "岡田", "長谷川", "藤田", "後藤", "村上", "遠藤", "青木", "坂本", "福田", "太田", "西村", "藤井", "金子", "岡本", "藤原", "中野", "三浦", "原田", "中川"]
    male_names = ["翔太", "翔", "優斗", "拓海", "優太", "大地", "友也", "大輔", "達也", "和馬", "健太", "亮", "祐樹", "航平", "健人", "駿", "誠", "良太", "孝之", "純", "陽平", "大", "健太郎", "翼", "翔太"]
    female_names = ["美咲", "葵", "彩花", "優香", "楓", "莉子", "美月", "凛", "優香", "菜月", "結衣", "美穂", "夏美", "未来", "真子", "智子", "由香", "麻衣", "茜", "友美", "佳奈", "亜美", "杏奈", "遥", "理恵"]

    departments = ["人事部", "経理部", "総務部", "法務部", "技術部", "営業部", "企画部"]

    for i in range(0, company_employees_number):
        id = company_name + "_" + str(random.randint(1000, 9999))
        
        surname = random.choice(surnames)
        
        if random.random() < 0.5:
            name = random.choice(male_names)
        else:
            name = random.choice(female_names)

        name = (surname + name).ljust(5)

        age = str(random.randint(20, 50)).ljust(3)

        department = random.choice(departments)

        data.append({"id":id, "name":name, "age":age, "department":department})


    return data
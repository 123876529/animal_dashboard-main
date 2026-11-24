import pandas as pd
import random
import os

# 基础动物数据池（真实动物模板）
base_animals = [
    {"chinese_name": "大熊猫", "scientific_name": "Ailuropoda melanoleuca", "english_name": "Giant Panda", "class_name": "哺乳纲", "order_name": "食肉目", "family_name": "熊科", "genus_name": "大熊猫属", "iucn_level": "易危", "habitat": "森林", "region": "四川", "diet": "植食", "lifespan_years": 20, "body_length_m": 1.5, "weight_kg": 100, "endemic_to_china": "是"},
    {"chinese_name": "东北虎", "scientific_name": "Panthera tigris altaica", "english_name": "Siberian Tiger", "class_name": "哺乳纲", "order_name": "食肉目", "family_name": "猫科", "genus_name": "豹属", "iucn_level": "濒危", "habitat": "森林", "region": "黑龙江", "diet": "肉食", "lifespan_years": 15, "body_length_m": 2.8, "weight_kg": 250, "endemic_to_china": "否"},
    {"chinese_name": "朱鹮", "scientific_name": "Nipponia nippon", "english_name": "Crested Ibis", "class_name": "鸟纲", "order_name": "鹈形目", "family_name": "鹮科", "genus_name": "朱鹮属", "iucn_level": "濒危", "habitat": "湿地", "region": "陕西", "diet": "杂食", "lifespan_years": 25, "body_length_m": 0.8, "weight_kg": 1.8, "endemic_to_china": "是"},
    {"chinese_name": "扬子鳄", "scientific_name": "Alligator sinensis", "english_name": "Chinese Alligator", "class_name": "爬行纲", "order_name": "鳄目", "family_name": "鼍科", "genus_name": "鼍属", "iucn_level": "极危", "habitat": "湿地", "region": "安徽", "diet": "肉食", "lifespan_years": 50, "body_length_m": 2.0, "weight_kg": 40, "endemic_to_china": "是"},
    {"chinese_name": "川金丝猴", "scientific_name": "Rhinopithecus roxellana", "english_name": "Golden Snub-nosed Monkey", "class_name": "哺乳纲", "order_name": "灵长目", "family_name": "猴科", "genus_name": "仰鼻猴属", "iucn_level": "濒危", "habitat": "森林", "region": "四川", "diet": "杂食", "lifespan_years": 20, "body_length_m": 0.7, "weight_kg": 15, "endemic_to_china": "是"},
    {"chinese_name": "藏羚羊", "scientific_name": "Pantholops hodgsonii", "english_name": "Tibetan Antelope", "class_name": "哺乳纲", "order_name": "偶蹄目", "family_name": "牛科", "genus_name": "藏羚属", "iucn_level": "近危", "habitat": "草原", "region": "西藏", "diet": "植食", "lifespan_years": 10, "body_length_m": 1.3, "weight_kg": 45, "endemic_to_china": "否"},
    {"chinese_name": "丹顶鹤", "scientific_name": "Grus japonensis", "english_name": "Red-crowned Crane", "class_name": "鸟纲", "order_name": "鹤形目", "family_name": "鹤科", "genus_name": "鹤属", "iucn_level": "易危", "habitat": "湿地", "region": "黑龙江", "diet": "杂食", "lifespan_years": 50, "body_length_m": 1.5, "weight_kg": 9, "endemic_to_china": "否"},
    {"chinese_name": "中华鲟", "scientific_name": "Acipenser sinensis", "english_name": "Chinese Sturgeon", "class_name": "鱼纲", "order_name": "鲟形目", "family_name": "鲟科", "genus_name": "鲟属", "iucn_level": "极危", "habitat": "海洋", "region": "长江流域", "diet": "肉食", "lifespan_years": 40, "body_length_m": 3.0, "weight_kg": 200, "endemic_to_china": "是"},
    {"chinese_name": "亚洲象", "scientific_name": "Elephas maximus", "english_name": "Asian Elephant", "class_name": "哺乳纲", "order_name": "长鼻目", "family_name": "象科", "genus_name": "亚洲象属", "iucn_level": "濒危", "habitat": "森林", "region": "云南", "diet": "植食", "lifespan_years": 60, "body_length_m": 5.5, "weight_kg": 3000, "endemic_to_china": "否"},
    {"chinese_name": "褐马鸡", "scientific_name": "Crossoptilon mantchuricum", "english_name": "Brown Eared Pheasant", "class_name": "鸟纲", "order_name": "鸡形目", "family_name": "雉科", "genus_name": "马鸡属", "iucn_level": "易危", "habitat": "森林", "region": "山西", "diet": "杂食", "lifespan_years": 15, "body_length_m": 1.0, "weight_kg": 2.5, "endemic_to_china": "是"}
]

# 扩充生成到 120 条
data = []
# 真实数据先放进去
for i, animal in enumerate(base_animals):
    animal["id"] = f"A{i+1:03d}"
    animal["discovery_year"] = random.randint(1800, 2000)
    animal["image_url"] = ""
    animal["description"] = f"{animal['chinese_name']}是一种生活在{animal['region']}的{animal['class_name']}动物。"
    data.append(animal)

# 随机生成剩余的模拟数据凑数
classes = ["哺乳纲", "鸟纲", "爬行纲", "两栖纲", "鱼纲", "昆虫纲"]
iucns = ["极危", "濒危", "易危", "近危", "无危", "数据缺乏"]
habitats = ["森林", "草原", "湿地", "海洋", "沙漠", "高山"]
regions = ["四川", "云南", "西藏", "新疆", "内蒙古", "黑龙江", "海南", "广东", "福建"]
diets = ["植食", "肉食", "杂食"]
endemics = ["是", "否"]

for i in range(len(base_animals), 120):
    cls = random.choice(classes)
    data.append({
        "id": f"A{i+1:03d}",
        "chinese_name": f"模拟动物{i+1}",
        "scientific_name": f"Simulans species{i+1}",
        "english_name": f"Simulated Animal {i+1}",
        "class_name": cls,
        "order_name": "未知目",
        "family_name": "未知科",
        "genus_name": "未知属",
        "iucn_level": random.choice(iucns),
        "habitat": random.choice(habitats),
        "region": random.choice(regions),
        "diet": random.choice(diets),
        # 核心修改点：将寿命上限调低至40，让真实动物上榜
        "lifespan_years": random.randint(1, 40) if cls != "昆虫纲" else random.randint(1, 5),
        "body_length_m": round(random.uniform(0.1, 5.0), 2) if cls != "昆虫纲" else round(random.uniform(0.01, 0.1), 2),
        "weight_kg": round(random.uniform(0.5, 500), 1) if cls != "昆虫纲" else round(random.uniform(0.01, 0.5), 2),
        "endemic_to_china": random.choice(endemics),
        "discovery_year": random.randint(1750, 2023),
        "image_url": "",
        "description": f"这是一条关于模拟动物{i+1}的描述，用于数据看板测试。"
    })

# 转换为 DataFrame 并保存
df = pd.DataFrame(data)

# 确保 data 文件夹存在
os.makedirs("data", exist_ok=True)

# 保存为 CSV，使用 utf-8-sig 防止 Excel 打开乱码
df.to_csv("data/animals.csv", index=False, encoding="utf-8-sig")
print("数据生成完毕！共生成", len(df), "条数据，已保存至 data/animals.csv")
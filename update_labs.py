import sqlite3
import yaml

conn = sqlite3.connect('data.db')
cursor = conn.cursor()


def fill_db_from_yaml():
    with open("_data/labs.yml") as d:
        data = yaml.load(d)

    for alias, lab in data.items():
        cursor.execute(
            "INSERT INTO labs(title, description, alias) VALUES(?, ?, ?)",
            [lab['title'], lab['description'], alias]
        )

        cursor.execute("SELECT last_insert_rowid()")
        lab_id, = cursor.fetchone()

        for idx, category in enumerate(lab['categories']):
            cursor.execute(
                "INSERT INTO labs_categories(title, lab_id, `order`) VALUES(?, ?, ?)",
                [category, str(lab_id), str(idx)]
            )

        cursor.execute("SELECT id FROM labs_categories WHERE lab_id = ? ORDER BY `order`", [lab_id])
        categories = cursor.fetchall()
        categories = [c[0] for c in categories]

        for task in lab['tasks']:
            cursor.execute(
                "INSERT INTO tasks(description, difficult, category_id) VALUES (?, ?, ?)",
                [task['description'], task['difficult'], categories[task['category']]]
            )

        conn.commit()


def fill_yaml_from_db():
    c = cursor.execute("SELECT id, title, description, alias FROM labs")
    labs = {}
    for id, title, description, alias in c:
        labs[id] = {
            "id": id,
            "title": title,
            "description": description,
            "alias": alias,
            "tasks": [],
            "categories": []
        }

    c = cursor.execute("SELECT id, title, lab_id, `order` "
                       "FROM labs_categories ORDER BY lab_id, `order`")

    categories = {}
    for id, title, lab_id, order in c:
        categories[id] = {
            "id": id,
            "title": title,
            "lab_id": lab_id,
            "order": order,
        }
        labs[lab_id]['categories'].append(title)

    c = cursor.execute("SELECT id, description, difficult, category_id "
                       "FROM tasks ORDER BY id")

    for id, description, difficult, category_id in c:
        lab_id = categories[category_id]['lab_id']
        labs[lab_id]["tasks"].append({
            'id': id,
            'description': description,
            'difficult': difficult,
            'category_id': categories[category_id]['order'],
        })

    print(labs)


if __name__ == '__main__':
    fill_yaml_from_db()

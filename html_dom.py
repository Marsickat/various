html_dom = {
    "html": {
        "head": {
            "title": "Колобок",
        },
        "body": {
            "h2": "Привет!",
            "div": "Хочешь, я расскажу тебе сказку?",
            "p": {
                "p1": "Тест 1",
                "p2": "Тест 2"
            }
        }
    }
}


def find_element(tree, element_name):
    if element_name in tree:
        return tree[element_name]
    for key, sub_tree in tree.items():
        if isinstance(sub_tree, dict):
            result = find_element(tree=sub_tree, element_name=element_name)
            if result:
                break
    else:
        result = None
    return result


res = find_element(tree=html_dom, element_name="p2")
print(res)

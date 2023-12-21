headers = ["学号", "姓名", "班级", "性别", "年龄", "电话", "QQ", "地址"]
headers_str=['sno_str','name_str','class_str','sex_str','age_str','phone_str','qq_str','addr_str']
def man_delete(card_list,index):
    del card_list[index]


def findBysno(card_list,find_num):
    for index,card in enumerate(card_list):
        if card['sno_str']==find_num:
            return index
    return None
def man_update(card_list,rows,column_key,new_data):
    card_list[rows][column_key]=new_data

def man_find(card_list,header_str,value):
    for index,card in enumerate(card_list):
        if card[headers_str[headers.index(header_str)]]==value:
             yield index

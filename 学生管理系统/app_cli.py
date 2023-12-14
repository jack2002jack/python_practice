from lib import manipulate
from lib import vars
def input_info (dict_value,tip_message):
    """

    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户没有输人内容,返回‘字典中原有的值
    """
    #.1.提示用户输人内容
    result_str = input(tip_message)
    #2.针对用户的输人进行判断, 如果用户输人了内容, 直接返回结果
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value



def update_student (find_num,card_list):
    """修改学生信息"""
    i=manipulate.findBysno(card_list,find_num)
    if i:
        print("学号\t姓名\t班级\t性别\t年龄\t电话\tQQ\t地址")
        print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t'%card_list[i]['num_str'],
              card_list[i]['name_str'],
              card_list[i]['class_str'],
              card_list[i]['sex_str'],
              card_list[i]['age_str'],
              card_list[i]['phone_str'],
              card_list[i]['qq_str'],
              card_list[i]['addr_str'])
        #替换已经存在的键值对
        num=input("输入要修改的列号")
        key=vars.headers_str[num]
        new_data=input_info(card_list[i][num],f"要将{key}修改为什么呢")
        manipulate.man_update(card_list,i,key,new_data)
        print('修改学生信息成功！！！')
    else:
        print('抱歉,没有找到学号为%s的学生'%find_num)

def delete_student(card_list):
    """删除学生信息"""
    find_num=input("请输入待删除学生学号: ")
    manipulate.man_delete(card_list,find_num)
    print('删除信息成功！')

import random
from common.op_excel import OpExcel


class CreateData:
    _default_path = r'E:\20190304Python精英班\11_web自动化项目\2019-5-11web自动化项目day_3\code\ECshop_刘飞宇\ECSHOP_刘飞宇\data\regdit_data.xlsx'
    _a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    _b = [str(x) for x in range(10)]
    _c = ['@qq.com', '@163.com', '@126.com', '@sina.cn', '@Yeah.net',
          '@aliyun.com', '@21cn.com']
    _d = [str(x) for x in range(1, 10)]
    _phone_start = ['134', '135', '136', '137', '138', '139', '147',
                    '150', '151', '152', '157', '158', '159', '182', '183',
                    '187', '188', '178']
    _first_name = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王'
        , '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨'
        , '朱', '秦', '尤', '许', '何', '吕', '施', '张'
        , '孔', '曹', '严', '华', '金', '魏', '陶', '姜']
    _last_name = ['澄邈', '德泽', '海超', '海阳', '海荣', '海逸', '海昌', '瀚钰', '瀚文', '涵亮', '涵煦', '涵蓄', '涵衍', '浩皛', '浩波', '浩博', '浩初',
                  '浩宕', '浩歌', '浩广', '浩邈', '浩气', '浩思', '浩言', '鸿宝', '鸿波', '鸿博', '鸿才', '鸿畅', '鸿畴', '鸿达', '鸿德', '鸿飞', '鸿风',
                  '鸿福', '鸿光', '鸿晖', '鸿朗', '鸿文', '鸿轩', '鸿煊', '鸿骞', '鸿远', '鸿云', '鸿哲', '鸿祯', '鸿志', '鸿卓', '嘉澍', '光济', '澎湃',
                  '彭泽', '鹏池', '鹏海', '浦和', '浦泽', '涵雁', '问凝', '冬萱', '晓山', '雁蓉', '梦蕊', '山菡', '南莲', '飞双', '凝丝', '思萱', '怀梦',
                  '雨梅', '冷霜', '向松', '迎丝', '迎梅', '雅彤', '香薇', '以山', '碧萱', '寒云', '向南', '书雁', '怀薇', '思菱', '忆文', '翠巧', '怀山',
                  '若山', '向秋', '凡白', '绮烟', '从蕾', '天曼', '又亦', '从安', '绮彤', '之玉', '凡梅', '依琴', '沛槐', '又槐', '元绿', '安珊', '夏之',
                  '易槐', '宛亦', '白翠', '丹云', '问寒', '易文', '傲易', '青旋', '思真', '雨珍', '幻丝', '代梅', '盼曼', '妙之', '半双', '若翠', '初兰',
                  '惜萍', '初之', '宛丝', '寄南', '小萍', '静珊', '千风', '天蓉', '雅青', '寄文', '涵菱', '香波', '青亦', '元菱', '翠彤', '春海', '惜珊']
    _answer_s = ['青青园中葵', '朝露待日晞',
                 '阳春布德泽', '万物生光辉',
                 '常恐秋节至', '焜黄华叶衰',
                 '百川东到海', '何时复西归',
                 '少壮不努力', '老大徒伤悲']

    def __init__(self):
        self._username = self.create_username()
        self._password = self.create_password()
        self._email = self.create_email()
        self._phone = self.create_phone()
        # self._qq = self.create_qq()
        self._index = self.random_select_index()
        self._answer = self.create_answer()
        self._check_data = {'username': self._username,
                            'password': self._password,
                            'email': self._email,
                            'phone': self._phone,
                            # 'qq': self._qq,
                            'qustion': self._index,
                            'answer': self._answer}
        # self._no_qq_data = {'username': self._username,
        #                     'password': self._password,
        #                     'email': self._email,
        #                     'phone': self._phone,
        #                     'qq': '',
        #                     'qustion': self._index,
        #                     'answer': self._answer}
        self._no_answer_data = {'username': self._username,
                                'password': self._password,
                                'email': self._email,
                                'phone': self._phone,
                                # 'qq': self._qq,
                                'qustion': '0',
                                'answer': ''}
        self._no_all = {'username': self._username,
                        'password': self._password,
                        'email': self._email,
                        'phone': self._phone,
                        # 'qq': '',
                        'qustion': '0',
                        'answer': ''}

    def create_username(self):
        """
        随机生成用户名格式为2个字母+6个数字
        :return: 随机生成的用户名
        """
        username_list = []
        username_en = random.sample(self._a, 2) + random.sample(self._b, 6)
        username_en = ''.join(username_en)
        username_cn = random.choice(self._first_name) + random.choice(self._last_name)
        username_list.append(username_en)
        username_list.append(username_cn)
        username = username_list[random.randint(0, 1)]
        return username

    def create_password(self):
        password = random.sample(self._a, 3) + random.sample(self._b, 4)
        password = ''.join(password)
        return password

    def create_email(self):
        email = list(random.choice(self._d)) + \
                random.sample(self._b, 8) + list(random.choice(self._c))
        email = ''.join(email)
        return email

    def create_phone(self):
        ress = []
        for i in range(8):
            res = random.choice(self._b)
            ress.append(res)
        phone = [random.choice(self._phone_start)] + ress
        phone = ''.join(phone)
        return phone

    def random_select_index(self):
        my_res_index = random.choice(self._d)
        return my_res_index

    def create_answer(self):
        my_answer = random.choice(self._answer_s)
        return my_answer

    # @staticmethod
    # def create_qq():
    #     qq_num = random.randint(10000, 9999999999)
    #     return qq_num

    def get_all_data(self, data_path=_default_path):
        """
        1.检查随机生成数据是否与excel里数据重复
        2.返回所有必填项和非必填项的值
        """
        # 读取表格数据
        data_info = OpExcel(data_path)
        my_res = data_info.get_data_info()

        # 建立检查列表
        check_username = []
        check_email = []
        check_phone = []
        # check_qq = []
        # 遍历表格数据，取出username,email,phone的值循环添加到检查列表里
        for i in my_res:
            check_username.append(i['username'])
            check_email.append(i['email'])
            check_phone.append(i['phone'])
            # check_qq.append(i['qq'])
        while True:
            """
            建立循环,判断随机生成的值是否存在于列表里对应的值,是的话重新生成新的随机值,
            直到不重复为止
            """
            # 检查用户名
            if self._check_data['username'] in check_username:
                self._check_data['username'] = self.create_username()
                continue
            # 检查电话号码
            elif self._check_data['phone'] in check_phone:
                self._check_data['phone'] = self.create_phone()
                continue
            # 检查邮箱
            elif self._check_data['email'] in check_email:
                self._check_data['email'] = self.create_email()
                continue
            # 检查QQ
            # elif self._check_data['qq'] in check_qq:
            #     self._check_data['qq'] = self.create_qq()
                continue
            # 都不重复则跳出
            else:
                break

        # 最后返回不和表格里数据重复的数据
        return self._check_data, '全部填写的注册数据'

    # def get_no_qq(self, data_path=_default_path):
    #     # 读取表格数据
    #     data_info = OpExcel(data_path)
    #     my_res = data_info.get_data_info()
    #
    #     # 建立检查列表
    #     check_username = []
    #     check_email = []
    #     check_phone = []
    #     # 遍历表格数据，取出username,email,phone的值循环添加到检查列表里
    #     for i in my_res:
    #         check_username.append(i['username'])
    #         check_email.append(i['email'])
    #         check_phone.append(i['phone'])
    #     while True:
    #         """
    #         建立循环,判断随机生成的值是否存在于列表里对应的值,是的话重新生成新的随机值,
    #         直到不重复为止
    #         """
    #         # 检查用户名
    #         if self._no_answer_data['username'] in check_username:
    #             self._no_answer_data['username'] = self.create_username()
    #             continue
    #         # 检查电话号码
    #         elif self._no_answer_data['phone'] in check_phone:
    #             self._no_answer_data['phone'] = self.create_phone()
    #             continue
    #         # 检查邮箱
    #         elif self._no_answer_data['email'] in check_email:
    #             self._no_answer_data['email'] = self.create_email()
    #             continue
    #         # 都不重复则跳出
    #         else:
    #             break
    #
    #     # 最后返回不和表格里数据重复的数据
    #     # return self._no_qq_data, '不填写QQ的注册数据'

    def get_no_answer(self, data_path=_default_path):
        # 读取表格数据
        data_info = OpExcel(data_path)
        my_res = data_info.get_data_info()

        # 建立检查列表
        check_username = []
        check_email = []
        check_phone = []
        # check_qq = []
        # 遍历表格数据，取出username,email,phone的值循环添加到检查列表里
        for i in my_res:
            check_username.append(i['username'])
            check_email.append(i['email'])
            check_phone.append(i['phone'])
            # check_qq.append(i['qq'])
        while True:
            """
            建立循环,判断随机生成的值是否存在于列表里对应的值,是的话重新生成新的随机值,
            直到不重复为止
            """
            # 检查用户名
            if self._no_answer_data['username'] in check_username:
                self._no_answer_data['username'] = self.create_username()
                continue
            # 检查电话号码
            elif self._no_answer_data['phone'] in check_phone:
                self._no_answer_data['phone'] = self.create_phone()
                continue
            # 检查邮箱
            elif self._no_answer_data['email'] in check_email:
                self._no_answer_data['email'] = self.create_email()
                continue
            # 检查QQ
            # elif self._no_answer_data['qq'] in check_qq:
            #     self._no_answer_data['qq'] = self.create_qq()
            #     continue
            # 都不重复则跳出
            else:
                break

        # 最后返回不和表格里数据重复的数据
        return self._no_answer_data, '不填写密码提示问题和答案的注册数据'

    def get_no_all(self, data_path=_default_path):
        # 读取表格数据
        data_info = OpExcel(data_path)
        my_res = data_info.get_data_info()

        # 建立检查列表
        check_username = []
        check_email = []
        check_phone = []
        # 遍历表格数据，取出username,email,phone的值循环添加到检查列表里
        for i in my_res:
            check_username.append(i['username'])
            check_email.append(i['email'])
            check_phone.append(i['phone'])
        while True:
            """
            建立循环,判断随机生成的值是否存在于列表里对应的值,是的话重新生成新的随机值,
            直到不重复为止
            """
            # 检查用户名
            if self._no_all['username'] in check_username:
                self._no_all['username'] = self.create_username()
                continue
            # 检查电话号码
            elif self._no_all['phone'] in check_phone:
                self._no_all['phone'] = self.create_phone()
                continue
            # 检查邮箱
            elif self._no_all['email'] in check_email:
                self._no_all['email'] = self.create_email()
                continue
            # 都不重复则跳出
            else:
                break

        # 最后返回不和表格里数据重复的数据
        return self._no_all, '不填写QQ,密码提示问题和答案的注册数据'

    def get_data_main(self, num):
        global data
        c_num = num
        if c_num in [1]:
            data = self.get_all_data()
        # elif c_num in [2]:
        #     data = self.get_no_qq()
        elif c_num in [3]:
            data = self.get_no_answer()
        elif c_num in [4]:
            data = self.get_no_all()
        return data


if __name__ == '__main__':
    a = CreateData()
    # print('用户名 -> ', a.username)
    # print('密码 -> ', a.password)
    # print('邮箱 -> ', a.email)
    # print('电话 -> ', a.phone)
    # print('index -> ', a.index)
    res = a.get_data_main(2)
    print(res[1])

"""
注册页面
"""
from ECShop.common.base import Base,open_browser
regdit_url = 'http://ecshop.itsoso.cn/user.php?act=register'
class RegditPage(Base): # 继承了Base类
    _reg_username = ('id','username') # 用户名输入框
    _reg_email = ('id','email') # 邮件输入框
    _reg_password = ('id','password1') # 密码输入框
    _reg_conform_password = ('id','conform_password') # 确认密码输入框
    _reg_extend_field5 = ('name','extend_field5') # 手机号输入框
    _reg_sel_question = ('name','sel_question') # 密码提示问题下拉框
    _select_value_01 = 'friend_birthday'  # 密码提示问题-我最好朋友的生日？
    _select_value_02 = 'old_address'  # 密码提示问题-我儿时居住地的地址？
    _select_value_03 = 'motto'  # 密码提示问题-我的座右铭是？
    _select_value_04 = 'favorite_movie'  # 密码提示问题-我最喜爱的电影？
    _select_value_05 = 'favorite_song'  # 密码提示问题-我最喜爱的歌曲？
    _select_value_06 = 'favorite_food'  # 密码提示问题-我最喜爱的食物？
    _select_value_07 = 'interest'  # 密码提示问题-我最大的爱好？
    _select_value_08 = 'favorite_novel'  # 密码提示问题-我最喜欢的小说？
    _select_value_09 = 'favorite_equipe'  # 密码提示问题-我最喜欢的运动队？
    _reg_passwd_answer = ('name','passwd_answer') # 密码问题答案输入框
    _reg_agreement = ('name','agreement') # 我已看过并接受单选框勾选
    _reg_user_agreement_link = ('link text','用户协议') # 用户协议连接
    _reg_submit_btn = ('name','Submit') # 立即注册按钮
    _reg_have_user_link = ('link text','我已有账号，我要登录') # 我已有账号，我要登录连接
    _reg_forget_password_link = ('link text','你忘记密码了吗？') # 你忘记密码连接

    def input_nuername(self,username):
        self.send_keys(self._reg_username,username)

    def input_password(self,password):
        self.send_keys(self._reg_password,password)

    def input_email(self,email):
        self.send_keys(self._reg_email,email)

    def input_repassword(self,repassword):
        self.send_keys(self._reg_conform_password,repassword)
    # 手机收入框
    def input_phone(self,phone):
        self.send_keys(self._reg_extend_field5,phone)

    # 密码提示问题选择框
    def qustion_select(self,index):
        self.selector_by_index(self._reg_sel_question,index)

    # 密码问题答案输入框
    def input_quntion_answer(self,text):
        self.send_keys(self._reg_passwd_answer,text)

    # 接受单选框
    def reg_agreement(self):
        self.click_one_checkbox(self._reg_agreement)

    # 用户协议连接
    def reg_user_agreement_link(self):
        self.click(self._reg_user_agreement_link)
    # 立即注册按钮
    def reg_submit_btn(self):
        self.click(self._reg_submit_btn)
    # 我已有账号，我要登录连接
    def reg_have_user_link(self):
        self.click(self._reg_have_user_link)
    # 你忘记，密码了吗？连接
    def reg_forget_password_link(self):
        self.click(self._reg_forget_password_link)

if __name__ == '__main__':
    driver = open_browser()
    page = RegditPage(driver)
    page.open_url(regdit_url)
    page.input_nuername('cc2222')
    page.time_sleep(2)
    page.input_email('1122211@qq.com')
    page.input_password('ws123456ws')
    page.time_sleep(3)
    page.input_repassword('ws123456ws')
    page.time_sleep(3)
    page.close_browser()

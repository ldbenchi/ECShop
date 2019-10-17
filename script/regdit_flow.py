from ECShop.page.regist_page import RegditPage,open_browser,regdit_url

# 注册业务流程
class RegditFlow:
    def __init__(self):
        self.driver = open_browser() # 打开浏览器
        self.reg_page = RegditPage(self.driver) # 实例化对象(可使用base和RegditPage里面的所有方法)
        self.reg_page.open_url(regdit_url) # 打开注册界面网址
    # 正常注册，只输入必填项和密码提示问题
    def regdit_user(self,username,email,password,phone,qustion,answer):
        self.reg_page.scroll(300) # 下拉滚动条到300的位置
        self.reg_page.input_nuername(username)
        self.reg_page.input_email(email)
        self.reg_page.input_password(password)
        self.reg_page.input_repassword(password)
        self.reg_page.input_phone(phone)
        self.reg_page.qustion_select(qustion)
        self.reg_page.input_quntion_answer(answer)
        self.reg_page.reg_agreement()
        self.reg_page.reg_submit_btn()

    # 检查注册是否成功一致
    def cheak_reg_is_true(self,reusername):
        locator = ('class name','f4_b')
        result = self.reg_page.is_check_text_element(locator, reusername)
        return result

if __name__ == '__main__':
    a = RegditFlow()
    username = 'wcc'
    password = '666666'
    email = '119497351@qq.com'
    phone = '12355674411'
    index = '4'
    text = '这是问题'
    a.regdit_user(username,email,password,phone,index,text)
    a.cheak_reg_is_true(username)
    a.reg_page.close_browser()

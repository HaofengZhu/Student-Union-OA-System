from app.model.UserDBManager import UserDBManager
from app.server.MsgManager import MsgManager
class UserManager:
    __UserDB=UserDBManager()

    def __init__(self):
        self.__islogin=False
        self.MsgManager=MsgManager()
        pass
    #登陆，返回是否成功
    def login(self,sid,pw):

        pass
    #是否登陆
    def isLogin(self):
        return self.__islogin
    #注册，返回是否成功,register_form是注册参数字典
    def register(self,register_form):
        pass

    # 注册，返回是否成功,revise_form是注册参数的字典（这个看前端是返回全部数据还是有修改的数据
    def revise_user_info(self, revise_form):
        pass

    #提交申请，msg为一个字典，返回是否成功
    def submit_msg(self,msg):
        pass

    #查看申请列表，返回申请的二维字典，第一维说明申请的类型，第二维是具体申请的字典
    def check_msg(self):
        pass



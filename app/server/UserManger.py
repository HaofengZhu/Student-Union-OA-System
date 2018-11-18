from app.model.UserDBManager import UserDBManager
from app.model.DBSubmitterFactory import DBSubmitterFactory
from app.model.DBChecker import DBChecker
class UserManager:
    __UserDB=UserDBManager()

    def __init__(self):
        self.__islogin=False
        pass
    #登陆，返回3个参数，是否成功(布尔值),数据库，id和部门，
    def login(self,userName,password):
        if self.__islogin:
            return self.__id,self.__department

        islogin,id,department=UserDBManager.checkLogin(userName,password)
        if islogin:
            self.__islogin=True
            self.__id=id
            self.__department=department
        return islogin,id,department

    #登出
    def loginOut(self):
        self.__islogin=False
        return True

    #是否登陆
    def isLogin(self):
        return self.__islogin

    #注册，返回是否成功,register_form是注册参数字典，
    def register(self,register_form):
        ok=UserDBManager.addUser(register_form)
        return ok

    # 修改信息，返回是否成功,revise_form是修改信息参数的字典（这个看前端是返回全部数据还是有修改的数据）
    def revise_user_info(self, revise_form):
        ok = UserDBManager.revise_user_info(revise_form)
        return ok

    #提交申请，msg为一个字典,type标记了申请的类型，返回是否成功
    #type有：zhuchiren,liyidui,haibao,jiangzuopiao,wuzi,大小写不限
    def submit_msg(self,msg):
        ok=DBSubmitterFactory.getSubmitter(msg["type"]).submit(msg)
        return ok

    #查看申请列表，返回申请的字典
    def check_msg(self):
        form=DBChecker.checkMsg(self.__department)
        return form



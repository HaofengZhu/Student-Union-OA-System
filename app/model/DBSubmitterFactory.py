from app.model.DBManager import DBManager
from app.model.DBSubmitter import DBSubmitter
from app.model.HaiBaoDBSubmitter import HaiBaoDBSubmitter
from app.model.JiangZuoPiaoDBSubmitter import JiangZuoPiaoDBSubmitter
from app.model.LiYiDuiDBSubmitter import LiYiDuiDBSubmitter
from app.model.ZhuChiRenDBSubmitter import ZhuChiRenDBSubmitter
from app.model.WuZiDBSubmitter import WuZiDBSubmitter
class DBSubmitterFactory():

    @classmethod
    def getSubmitter(cls,type):
        if type.lower =="zhuchiren":
            return ZhuChiRenDBSubmitter
        elif type.lower=="liyidui":
            return LiYiDuiDBSubmitter
        elif type.lower=="jiangzuopiao":
            return JiangZuoPiaoDBSubmitter
        elif type.lower=="haibao":
            return HaiBaoDBSubmitter
        elif type.lower=="wuzi":
            return WuZiDBSubmitter
        else:
            return object


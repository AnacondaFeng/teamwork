class Member(object):
    """定义人员类"""

    def __init__(self, str, mm=12):
        """
        初始化构造方法
        :param str: 人员信息str
        """
        self.rest = str.split('-')
        self.id = self.rest[0]
        self.name = self.rest[1]
        self.band = self.rest[2]
        self.team = self.rest[3]
        self.role = self.rest[4]
        # 2020年投入MM，默认12
        self.mm = mm

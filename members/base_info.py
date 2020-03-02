import constants


class Member(object):
    """定义人员类"""
    income = 0  # 年度个人营收指标
    patent = 0  # 年度专利目标

    def __init__(self, str):
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
        if len(self.rest) == 6:
            self.mm = int(self.rest[5])
        else:
            self.mm = 12

    def sum_price_mm(self, price):
        """依照价格返回营收目标"""
        # 依照Band判断分级
        self.income = int(self.mm) / 12 * price * self.band_sel
        # 保留两位小数
        # print('%.2f' % self.income)
        self.income = float('%.2f' % self.income)
        return self.income

    @property
    def band_sel(self):
        """依照个人Band进行分级"""
        init_num = 1
        if self.band in constants.BAND_LEVEL_1:
            init_num += constants.INCOME_INCREASE_PERCENT
        elif self.band in constants.BAND_LEVEL_2:
            init_num += constants.INCOME_INCREASE_PERCENT * 2
        elif self.band in constants.BAND_LEVEL_3:
            init_num += constants.INCOME_INCREASE_PERCENT * 3
        else:
            init_num
        return init_num

    def sum_patent(self):
        """根据Band返回专利数"""
        if self.band in constants.BAND_LEVEL_0:
            self.patent = constants.PATENT_0
        elif self.band in constants.BAND_LEVEL_1:
            self.patent = constants.PATENT_1
        elif self.band in constants.BAND_LEVEL_2:
            self.patent = constants.PATENT_2
        elif self.band in constants.BAND_LEVEL_3:
            self.patent = constants.PATENT_3

        return self.patent


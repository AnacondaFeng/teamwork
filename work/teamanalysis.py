import constants
from members.base_info import Member


class TAnalysis(object):
    """小组运营分析"""
    # 存储人员对象list
    mems_list = []

    # 存储各小组成员
    t_manage = []
    t_expert = []
    t_sa = []
    t_frame = []
    t_data = []
    t_mes = []
    t_wms = []
    t_aps = []
    t_eqsys = []
    t_analysis = []
    t_report = []
    t_none = []

    # 人均营收基数
    per_income = 0

    # 新招聘人数
    new_person_cum = 0

    # 分组存储，组装成dict
    _team_dict = {'经营组': t_manage, '专家组': t_expert, 'SA组': t_sa, 'Frame组': t_frame,
                  '数据集成组': t_data, 'MES组': t_mes, 'WMS组': t_wms, 'APS组': t_aps,
                  '设备系统组': t_eqsys, '工业分析组': t_analysis, '透明化组': t_report, '无组': t_none}

    def __init__(self, info_path, new_info_path):
        # 1.读取基础信息文件中的数据(现员信息)
        with open(info_path, 'r', encoding='utf-8') as file:
            # rest = file.readlines()
            # 这么写可以不显示\n
            self.rest = file.read().splitlines()
        # 2.转换成需要使用的格式 对象list
        for i in self.rest:
            self.mem_info = Member(i)
            self.team_assign_list()
            # 暂时没什么用,求和总MM用，后面增加新人也可以用
            self.mems_list.append(self.mem_info)

        # 增加新员工初始化
        with open(new_info_path, 'r', encoding='utf-8') as new_file:
            self.new_rest = new_file.read().splitlines()

        # 判断有没有招聘计划
        if len(self.new_rest) != 0:
            for i in self.new_rest:
                self.mem_info = Member(i)
                self.team_assign_list()
                self.mems_list.append(self.mem_info)
            self.new_person_cum = len(self.new_rest)

        # 人员总数
        self._cum_mems = len(self.mems_list)

    @property
    def cum_members(self):
        """统计总人数"""
        return self._cum_mems

    def team_assign_list(self):
        """人员分组，我要对象的list"""
        if self.mem_info.team == constants.TEAM_MANAGE:
            self.t_manage.append(self.mem_info)
        elif self.mem_info.team == constants.TEAM_EXPERT:
            self.t_expert.append(self.mem_info)
        elif self.mem_info.team == constants.TEAM_SA:
            self.t_sa.append(self.mem_info)
        elif self.mem_info.team == constants.TEAM_FRAME:
            self.t_frame.append(self.mem_info)
        elif self.mem_info.team == constants.TEAM_DATA:
            self.t_data.append(self.mem_info)
        elif self.mem_info.team == constants.TEAM_MES:
            self.t_mes.append(self.mem_info)
        elif self.mem_info.team == constants.TEAM_WMS:
            self.t_wms.append(self.mem_info)
        elif self.mem_info.team == constants.TEAM_APS:
            self.t_aps.append(self.mem_info)
        elif self.mem_info.team == constants.TEAM_EQSYS:
            self.t_eqsys.append(self.mem_info)
        elif self.mem_info.team == constants.TEAM_ANALYSIS:
            self.t_analysis.append(self.mem_info)
        elif self.mem_info.team == constants.TEAM_REPORT:
            self.t_report.append(self.mem_info)
        else:
            self.t_none.append(self.mem_info)

    @property
    def return_team_dict(self):
        """返回team字典"""
        return self._team_dict

    def mem_name_list(self, team_name):
        """
        返回小组成员姓名
        :param team_list:小组成员对象组
        :return: 小组成员姓名dict
        """
        name_leader = ''
        name_list = []
        for i in self.return_team_dict[team_name]:
            if i.role == constants.ROLE_TEAM_MEMBER:
                name_list.append(i.name + '^' + str(i.income) + '万元')
            else:
                name_leader = '组长：' + i.name + '^' + str(i.income) + '万元'
        return {name_leader: name_list}

    def calc_income_all(self, target, per_income):
        """
        计算营收目标分解
        :param target:营收目标
        :return: 整理好的文档，组别 人员 收益
        """
        #    1.target是总目标，要先知道总MM，然后算单价，计算出来的是平均值，和Band还没有关系
        #     2.按照基础88万/每人 计算，求和，不满足要求，继续往上增加
        print('------------------分隔符-----------------')
        print('MM Cum:{0}, Income:{1}, Average:{2}'.format(self.sum_mm, target, int(target / self.sum_mm * 12)))

        self.per_income = per_income
        while True:
            sum_income = 0
            person_income_list = []
            for i in self.mems_list:
                # 经营组/专家组/Frame组不算钱
                if i.team not in constants.NO_INCOME_TEAM.values():
                    person_income = i.sum_price_mm(self.per_income)
                    sum_income += person_income
                    person_income_list.append(i.name + str(person_income))

            if sum_income < target:
                #         如果按照此人均目标计算小于营收目标的话，那么没办法只能往上涨了
                # print('人均收入：{0}'.format(per_income))
                self.per_income += 1
            else:
                # print(sum_income)
                # print(person_income_list)
                break

        #     将结果输出至文档
        with open(constants.OUTPUT_INFO_PATH, 'w', encoding='utf-8') as op_file:
            op_file.write(
                '2020年总人数：{0}人，新招聘人员预估：{4}人，总MM:{1}，营收目标:{2}万元， 目标人均年收入:{3}万元'.format(self.cum_members, self.sum_mm, target,
                                                                          per_income, self.new_person_cum))
            op_file.write('\n\n')
            op_file.write('未计算营收的小组包含：\n')
            for i in constants.NO_INCOME_TEAM.keys():
                op_file.write(i + '\n')

            op_file.write('\n\n')

            op_file.write('Band按照四个等级，每个等级间增长系数为{0}\n'.format(constants.INCOME_INCREASE_PERCENT))
            op_file.write('第一梯度：{0}\n'.format(constants.BAND_LEVEL_0))
            op_file.write('第二梯度：{0}\n'.format(constants.BAND_LEVEL_1))
            op_file.write('第三梯度：{0}\n'.format(constants.BAND_LEVEL_2))
            op_file.write('第四梯度：{0}\n'.format(constants.BAND_LEVEL_3))

            op_file.write('\n')
            op_file.write('经过计算，人均营收基数为(第一梯度){0}万元，总营收{1}万元\n'.format(self.per_income, '%0.2f' % sum_income))
            op_file.write('\n')
            op_file.write('各小组统计情况如下：')
            op_file.write('\n')
            # 遍历字典结果集
            for k, v in self.return_team_dict.items():
                if k in constants.INCOME_TEAM:
                    op_file.write(self.str_team_info(k, v))
                    op_file.write('\n')
                    op_file.write(str(self.mem_name_list(k)))
                    op_file.write('\n\n')

    def list_mem_name(self, team_obj):
        """定义完了，但是先没有用"""
        name_list = []
        for i in team_obj:
            if i.role == constants.ROLE_TEAM_LEADER:
                name_list[0] = i.name
            else:
                name_list.append(i.name)

        return name_list

    def str_team_info(self, team_name, team_obj):
        """返回各team统计信息"""
        sum_income = 0
        new_person = 0
        for i in team_obj:
            sum_income += i.income
            if i.id == team_name:
                new_person += 1
        return '【{0}】总营收目标：{1}万元，2020年新招聘人数需求：{2}人'.format(team_name, '%.2f' % sum_income, new_person)

    @property
    def sum_mm(self):
        """返回总MM"""
        sum_mm = 0
        for i in self.mems_list:
            sum_mm += i.mm
        return sum_mm

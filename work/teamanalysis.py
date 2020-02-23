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

    # 分组存储，组装成dict
    _team_dict = {'经营组': t_manage, '专家组': t_expert, 'SA组': t_sa, 'Frame组': t_frame,
                  '数据集成组': t_data, 'MES组': t_mes, 'WMS组': t_wms, 'APS组': t_aps,
                  '设备系统组': t_eqsys, '工业分析组': t_analysis, '透明化组': t_report, '无组': t_none}

    def __init__(self, info_path):
        # 1.读取基础信息文件中的数据
        with open(info_path, 'r', encoding='utf-8') as file:
            # rest = file.readlines()
            # 这么写可以不显示\n
            self.rest = file.read().splitlines()
        # 2.转换成需要使用的格式 对象lis
        for i in self.rest:
            self.mem_info = Member(i)
            self.team_assign_list()
            # 暂时没什么用
            self.mems_list.append(self.mem_info)

        # 3.人员总数
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
                name_list.append(i.name)
            else:
                name_leader = i.name
        return {name_leader: name_list}

    # 这个方法没啥用
    def show_byteam(self):
        """按照小组别进行人员展示"""
        print('经营组：{0}'.format(self.t_manage))
        print('专家组：{0}'.format(self.t_expert))
        print('SA组：{0}'.format(self.t_sa))
        print('Frame组：{0}'.format(self.t_frame))
        print('数据集成组：{0}'.format(self.t_data))
        print('MES组：{0}'.format(self.t_mes))
        print('WMS组：{0}'.format(self.t_wms))
        print('APS组：{0}'.format(self.t_aps))
        print('设备系统组：{0}'.format(self.t_eqsys))
        print('工业分析组：{0}'.format(self.t_analysis))
        print('透明化组：{0}'.format(self.t_report))
        print('无组：{0}'.format(self.t_none))

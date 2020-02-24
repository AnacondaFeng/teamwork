# 人员信息路径
MEMBERS_INFO_PATH = './input/members_info'
# 招聘需求信息路径
MEMBERS_NEW_INFO_PATH = './input/new_members_info'
# 结果输出路径
OUTPUT_INFO_PATH = './output/rest'

# 小组信息
TEAM_MANAGE = '0'
TEAM_EXPERT = '1'
TEAM_SA = '2'
TEAM_FRAME = '3'
TEAM_DATA = '4'
TEAM_MES = '5'
TEAM_WMS = '6'
TEAM_APS = '7'
TEAM_EQSYS = '8'
TEAM_ANALYSIS = '9'
TEAM_REPORT = '10'
TEAM_NO_EXIST = '?'

# 角色信息
ROLE_TEAM_LEADER = '0'
ROLE_TEAM_MEMBER = '1'

# Band分级
BAND_LEVEL_0 = ['Band5', 'Band6', 'Band7']
BAND_LEVEL_1 = ['Band8', 'Band9']
BAND_LEVEL_2 = ['Band10', 'Band11']
BAND_LEVEL_3 = ['Band12', 'Band13', 'Band14']

# 不同级别增长百分比
INCOME_INCREASE_PERCENT = 0.2

# 不计算收入组
# NO_INCOME_TEAM = [{TEAM_MANAGE: ''}, {TEAM_EXPERT: ''}, {TEAM_FRAME: ''}, {TEAM_NO_EXIST: ''}]
NO_INCOME_TEAM = {'经营组': TEAM_MANAGE, '专家组': TEAM_EXPERT, 'Frame组': TEAM_FRAME, '无组': TEAM_NO_EXIST}
# 计算收入组
INCOME_TEAM = {'SA组': TEAM_SA, '数据集成组': TEAM_DATA, 'MES组': TEAM_MES, 'WMS组': TEAM_WMS, 'APS组': TEAM_APS, '设备系统组': TEAM_EQSYS, '工业分析组': TEAM_ANALYSIS,
               '透明化组': TEAM_REPORT}

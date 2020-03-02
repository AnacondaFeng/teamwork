import math

import constants
from work.teamanalysis import TAnalysis



def main():
    """定义main方法"""
    ta = TAnalysis(constants.MEMBERS_INFO_PATH, constants.MEMBERS_NEW_INFO_PATH)

    # for k, v in ta.return_team_dict.items():
    #     print('{0}:{1}'.format(k, ta.mem_name_list(k)))

    # 年度营收目标6600万，人均年收入目标88万
    ta.calc_all(6600, 88)

    # print(math.ceil(1/3))

if __name__ == '__main__':
    main()

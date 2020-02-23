import constants
from work.teamanalysis import TAnalysis


def main():
    """定义main方法"""
    ta = TAnalysis(constants.MEMBERS_INFO_PATH)

    for k, v in ta.return_team_dict.items():
        print('{0}:{1}'.format(k, ta.mem_name_list(k)))

    ta.calc_income_all(6600, 88)


if __name__ == '__main__':
    main()

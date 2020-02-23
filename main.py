import constants
from work.teamanalysis import TAnalysis


def main():
    """定义main方法"""
    ta = TAnalysis(constants.MEMBERS_INFO_PATH)
    # print("一共有{0}人".format(ta.cum_members))
    # ta.show_byteam()

    for k, v in ta.return_team_dict.items():
        print('{0}:{1}'.format(k, ta.mem_name_list(k)))


if __name__ == '__main__':
    main()

scores_team_1 = [100, 95, 120]
scores_team_2 = [45, 30, 10]
scores_team_3 = [200, 35, 190]

scores =  (scores_team_1, scores_team_2, scores_team_3)

# scores_team_1[0] = 300
# print(scores[0])        # [300, 95, 120]

# 直接修改元组子项
scores[0][0] = 300
print(scores[0])        # [300, 95, 120]
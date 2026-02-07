def hang_time(traj):
    """
    landing_position: 导弹的滞空时间
    
    :param traj: 说明
    """
    return traj[0][-1]

def landing_position(traj):
    """
    hand_position: 导弹的最远射程
    
    :param traj: 说明
    """
    return traj[1][-1]

def max_height(traj):
    """
    max_height: 导弹的最高射程
    
    :param traj: 说明
    """
    return max(traj[2])


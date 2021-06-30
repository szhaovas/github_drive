import gym
from IPython import embed
import robo_gym
from robo_gym.wrappers.exception_handling import ExceptionHandling

#target_machine_add = '192.168.0.3:2150'
target_machine_add = '127.0.0.1'

# initialize environment
env = gym.make('URMaze-v0', gui=True, ur_model='ur10', ip=target_machine_add)
env = ExceptionHandling(env)
env.reset(joint_positions=[0.0, -0.25, 0.25, 0.0, -0.25, 0.0])

# get plan to object_0's translation(xyz) with random orientation
pl = env.get_moveit_plan_to_object0()
for i, pt in enumerate(pl):
    print('traj_pt %d:'%i + str(pt))

state, reward, done, info = env.execute_plan(pl, skip_to_end=False)
rs_state = env.client.get_state_msg().state_dict

print('Final ee_to_ref_translation:')
print(rs_state['ee_to_ref_translation_x'],
        rs_state['ee_to_ref_translation_y'],
        rs_state['ee_to_ref_translation_z'])

# import numpy as np
# num_episodes = 1
#
# for episode in range(num_episodes):
#     done = False
#     env.reset()
#     while not done:
#         # random step in the environment
#         state, reward, done, info = env.step(np.array([1, -1, 1, -1, 1]))
#
#         print(state, reward)


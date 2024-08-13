class Solution:
    def survivedRobotsHealths(self, positions, healths, directions: str):
        pos_to_idx = {}
        number_of_robots = len(positions)
        for i in range(number_of_robots):
            pos_to_idx[positions[i]] = i

        robots_going_right = []
        for i in sorted(pos_to_idx.keys()):
            current_index = pos_to_idx[i]
            if robots_going_right and directions[current_index] == 'L':
                while robots_going_right:
                    index_of_incoming_robot = pos_to_idx[robots_going_right[len(robots_going_right) - 1]]
                    if healths[current_index] > healths[index_of_incoming_robot]:
                        healths[index_of_incoming_robot] = 0
                        healths[current_index] -= 1
                        robots_going_right.pop()
                        continue
                    elif healths[current_index] == healths[index_of_incoming_robot]:
                        healths[index_of_incoming_robot] = 0
                        healths[current_index] = 0
                        robots_going_right.pop()
                        break
                    else:
                        healths[current_index] = 0
                        healths[index_of_incoming_robot] -= 1
                        break
            elif directions[current_index] == 'R':
                robots_going_right.append(i)
        final_list = []
        for robot_health in healths:
            if robot_health > 0:
                final_list.append(robot_health)
        return final_list


Solution().survivedRobotsHealths([3,5,2,6], [10,10,11,11], "RLRL")
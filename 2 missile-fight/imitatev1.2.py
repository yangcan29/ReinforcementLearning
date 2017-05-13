import numpy as np
import pickle

person_numbers = 2
store_numbers = 3
near = 6
mid = 4
long = 3
load = 1


class State(object):
    def __init__(self):
        self.data = np.array([[near, mid, long], [near, mid, long]])
        # self.winner = None
        self.hashVal = None
        self.end = None
        self.actions = []
        self.hit = np.array([[[0.9, 0.7], [0.75, 0.5], [0, 0], [0, 0]],
                             [[0.8, 0.8], [0.7, 0.7], [0.7, 0.6], [0.7, 60]],
                             [[0.7, 0.9], [0.65, 0.8], [0.6, 0.75], [0.55, 100]]])
        # hit[i,j]第i个导弹命中j个地方的概率
        self.damage = 0

    def get_hash(self):
        if self.hashVal is None:
            self.hashVal = 0
            for i in self.data.reshape(person_numbers*store_numbers):
                self.hashVal = self.hashVal * 10 + i
                # 这里的10保证哈希值唯一
        return int(self.hashVal)

    def is_end(self):
        if self.end is not None:
            return self.end
        if self.data.sum():
            self.end = False
        else:
            self.end = True
        return self.end

    # symbol是0或者1
    def get_actions(self, symbol):
        if self.actions:
            return self.actions
        for num, i in enumerate(self.data[symbol, :]):
            if i == 0:
                continue
            for j in range(store_numbers+1):
                a = np.zeros((person_numbers, store_numbers+1))
                a[symbol, num] = 1
                a[0 if symbol else 1, j] = 1
                self.actions.append(a)
        return self.actions

    def next_state(self, action, symbol):
        result = action.argmax(1)
        newState = State()
        newState.data = np.copy(self.data)
        newState.data[symbol, result[symbol]] -= 1
        target = result[0 if symbol else 1]
        if target < 3:
            rate = self.hit[result[symbol], target]
            if np.random.binomial(1, rate[0]):
                num_left = newState.data[0 if symbol else 1,target]
                sub = 0
                for i in range(num_left):
                    if np.random.binomial(1, rate[1]):
                        sub += 1
                num_left -= sub
                newState.data[0 if symbol else 1, target] = num_left
        else:
            rate = self.hit[result[symbol], target]
            if np.random.binomial(1, rate[0]):
                damage = rate[1]
                newState.damage = -damage-np.random.random()
        return newState
        # return newState

    def next_states(self, action, symbol):
        result = action.argmax(1)
        newState = State()
        newState.data = np.copy(self.data)
        newState.data[symbol, result[symbol]] -= 1
        target = result[0 if symbol else 1]
        newStates = []
        if target < 3:
            num_left = newState.data[0 if symbol else 1, target]
            for i in range(num_left+1):
                newState.data[0 if symbol else 1, target] = i
                newStates.append(newState)
                newState = State()
                newState.data = np.copy(self.data)
                newState.data[symbol, result[symbol]] -= 1
        return newStates


def getAllStates():
    allStates = dict()
    for i in range(near+1):
        for j in range(mid+1):
            for k in range(long+1):
                for a in range(near+1):
                    for b in range(mid+1):
                        for c in range(long+1):
                            state = State()
                            state.data = np.array([[i, j, k], [a, b, c]])
                            allStates[state.get_hash()] = (state, state.is_end())
    return allStates

if load == 1:
    fr = open('state', 'rb')
    allStates = pickle.load(fr)
    fr.close()
else:
    allStates = getAllStates()
    fw = open('state', 'wb')
    pickle.dump(allStates, fw)
    fw.close()
# print(len(allStates))


class Player(object):
    def __init__(self, symbol):
        self.symbol = symbol
        self.states_actions = {}
        for state in allStates.values():
            state[0].actions = []
        for key, val in allStates.items():
            self.states_actions[key] = [val[0], val[1], val[0].get_actions(self.symbol)]
            length = len(self.states_actions[key][2])
            if length:
                rates = np.linspace(1/length, 1/length, length)
                values = np.zeros(length)
                self.states_actions[key].append(rates)
                self.states_actions[key].append(values)
        # self.states_actions[key][state,isend,actions,rate,values]
        self.states = [] # 是state不是哈希值
        self.stepSize = 0.1
        self.exploreRate = 0.1

    def reset(self):
        self.states = []

    def feedState(self, state):
        self.states.append(state)

    def feedReward(self, reward):
        self.states = [state.get_hash()() for state in self.states]
        target = reward
        for latestState in reversed(self.states):
            value = self.states_actions[latestState][4] + self.stepSize * (target - self.states_actions[latestState][4])
            self.states_actions[latestState][4] = value
            target = value
        self.states = []

    def takeAction(self):
        state = self.states[-1]
        nextactions = self.states_actions[state.get_hash()][2]
        if nextactions:
            # print(nextactions)
            np.random.shuffle(nextactions)
            # Not sure if truncating is the best way to deal with exploratory step
            # Maybe it's better to only skip this step rather than forget all the history
            action = nextactions[0]
            # print(action)
            return state.next_state(action, self.symbol)
        else:
            return state


A = Player(0)
B = Player(1)
cuunt = 10000
win = 0
lose = 0
equal = 0
for i in range(cuunt):
    A.reset()
    B.reset()
    state = State()
    # print(state.data)
    flag = state.is_end()
    damages = [0, 0]
    while flag == 0:
        A.feedState(state)
        state = A.takeAction()
        damages[1] = state.damage
        # print(state.data)
        B.feedState(state)
        state = B.takeAction()
        damages[0] = state.damage
        # print(state.data)
        flag = state.is_end()
    # print(damages)
    if damages[0] > damages[1]:
        win += 1
    elif damages[1] > damages[0]:
        lose += 1
    else:
        equal += 1

print('平局率为', equal/cuunt)
print('赢率为', win/cuunt)
print('输率为', lose/cuunt)

#  TensorFlow

#  Created by Tiago Ferreira on 07/12/2017.
#  Copyright (c) 2017 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import random
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import sgd
import json

class Gravity:
    def __init__(self, size):
        self.size = size
        block_y = 0
        block_x = random.randint(0, self.size - 1)
        basket_x = random.randint(1, self.size - 2)
        self.state = [block_y, block_x, basket_x]

    def observe(self):
        canvas = [0] * self.size ** 2
        canvas[self.state[0] * self.size + self.state[1]] = 1
        canvas[(self.size - 1) * self.size + self.state[2] - 1] = 1
        canvas[(self.size - 1) * self.size + self.state[2] + 0] = 1
        canvas[(self.size - 1) * self.size + self.state[2] + 1] = 1
        return np.array(canvas).reshape(1, -1)

    def act(self, action):
        block_y, block_x, basket_x = self.state

        # Action takes value of 0, 1, 2 based on movement.
        basket_x += int(action) - 1

        # Make sure we don't go offscreen
        basket_x = max(1, basket_x)
        basket_x = min(self.size - 2, basket_x)

        block_y += 1
        self.state = [block_y, block_x, basket_x]

        reward = 0
        if block_y == self.size - 1:
            if abs(block_x - basket_x) <= 1:
                reward = 1 # Cathced the block, reward of 1
            else:
                reward = -1 # Failed to cath, reward of -1

        game_over = block_y == self.size - 1
        return self.observe(), reward, game_over

    def reset(self):
        self.__init__(self.size)

if __name__ == "__main__":
    GRID_DIM = 10 # Dimension of the grid
    EPSILON = 0.1 # Exploration constant
    LEARNING_RATE = 0.2 # Learning constant (rate at which the NN will learn the stuff we give it)
    LOSS_FUNCTION = "mse"
    HIDDEN_LAYER1_SIZE = 100
    HIDDEN_LAYER1_ACTIVATION = "relu"
    HIDDEN_LAYER2_SIZE = 100
    HIDDEN_LAYER2_ACTIVATION = "relu"
    BATCH_SIZE = 50 # Feed 50 training examples at a time
    EPOCHS = 1000 # Train 1K times

    model = Sequential()
    model.add(
        Dense(
            HIDDEN_LAYER1_SIZE,
            input_shape = (GRID_DIM ** 2,),
            activation = HIDDEN_LAYER1_ACTIVATION
        )
    )

    model.add(
        Dense(
            HIDDEN_LAYER2_SIZE,
            activation = HIDDEN_LAYER2_ACTIVATION
        )
    )

    model.add(Dense(3))
    model.compile(sgd(lr = LEARNING_RATE), LOSS_FUNCTION)

    env = Gravity(GRID_DIM)

    win_cnt = 0
    for epoch in range(EPOCHS):
        env.reset()
        game_over = False
        input_t = env.observe()

        while not game_over:
            input_tm1 = input_t
            if random.random() <= EPSILON:
                action = random.randint(0, 2) # Take a random action
            else:
                q = model.predict(input_tm1) # Take what our NN tells us is best
                action = np.argmax(q[0])

            input_t, reward, game_over = env.act(action)
            if reward == 1:
                win_cnt += 1

        # Print Epcoh success each time.
        print("Epoch: {:06d}/{:06d} | Win count {}".format(epoch, EPOCHS, win_cnt))

    # Save weights, these are the "knowledge"
    model.save_weights("model.h5", overwrite = True)

    # Store the NN's structure
    with open("model.json", "w") as outfile:
        json.dump(model.to_json(), outfile)

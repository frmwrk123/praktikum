from multi_layer import MultiLayerNetwork
from world import world_digits

import numpy as np


def print_image(img_data, row_len=8):

    print("")
    for i in range(len(img_data)):
        if (img_data[i] == 1):
            print("1", end="")
        else:
            print(" ", end="")
        if (i + 1) % row_len == 0:
            print("")
    print("")


def interpret_result(out_array):

    out = list(out_array)
    if 1 in out_array:
        return world_digits.digits[out.index(1)]
    else:
        return "not classified"

if __name__ == '__main__':

    digits = world_digits()

    inputsize, number_of_digits = digits.dim()

    network = MultiLayerNetwork(
        layout=(inputsize, 1000, number_of_digits),
        transfer_function = MultiLayerNetwork.sigmoid_function,
        last_transfer_function = MultiLayerNetwork.step_function)

    for cycles in range(100):
        digits.newinit()
        for i in range(number_of_digits):
            inputs = digits.sensor()
            expected = np.zeros(number_of_digits)
            expected[i] = 1

            err = network.train(inputs, expected)

            # print("train inp: {} expected: {} error: {}".format(
            #     inputs, expected, err))
            digits.act()

    digits.newinit()
    for i in range(number_of_digits):
        inputs = digits.sensor()
        print_image(digits.sensor())
        expected = np.zeros(number_of_digits)
        expected[i] = 1

        result = network.calc(inputs)
        digits.act()

        print("result: {}".format(interpret_result(result)))
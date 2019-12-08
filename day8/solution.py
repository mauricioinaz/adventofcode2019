
import matplotlib.pyplot as plt


def main():
    data = open('input.txt', 'r').read().strip()
    data = [int(c) for c in data]

    numb_layers = len(data)//(25*6)
    layers = [[] for _ in range(0, numb_layers)]
    for i, pixel in enumerate(data):
        layers[(i*numb_layers) // len(data)].append(pixel)

    # PART 1
    # least_zeroes = None
    # layer_id = None
    # for i, layer in enumerate(layers):
    #     zeroes = 0
    #     for pixel in layer:
    #         if pixel == 0:
    #             zeroes += 1
    #     if least_zeroes:
    #         if zeroes < least_zeroes:
    #             least_zeroes = zeroes
    #             layer_id = i
    #     else:
    #         least_zeroes = zeroes
    #
    # result = layers[layer_id].count(1) * layers[layer_id].count(2)
    # print(f'The number of 1*numbers of 2 in layer with least zeroes is: {result}')

    # PART 2
    final_message = [2 for _ in range(0, len(layers[0]))]
    for layer in layers:
        for i, pixel in enumerate(layer):
            if final_message[i] == 2 and pixel != 2:
                final_message[i] = pixel

    image = [final_message[(row*25):(row*25+25)] for row in range(0, 6)]
    plt.imshow(image)
    plt.show()


if __name__ == "__main__":
    main()

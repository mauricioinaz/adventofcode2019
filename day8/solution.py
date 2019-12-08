
def main():
    data = open('input.txt', 'r').read().strip()
    data = [int(c) for c in data]

    numb_layers = len(data)//(25*6)
    layers = [[] for _ in range(0, numb_layers)]
    print(len(layers))
    for i, pixel in enumerate(data):
        layers[(i*numb_layers) // len(data)].append(pixel)

    least_zeroes = None
    layer_id = None
    for i, layer in enumerate(layers):
        zeroes = 0
        for pixel in layer:
            if pixel == 0:
                zeroes += 1
        if least_zeroes:
            if zeroes < least_zeroes:
                least_zeroes = zeroes
                layer_id = i
        else:
            least_zeroes = zeroes

    result = layers[layer_id].count(1) * layers[layer_id].count(2)
    print(f'The number of 1*numbers of 2 in layer with least zeroes is: {result}')


if __name__ == "__main__":
    main()

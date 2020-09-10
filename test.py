import sys

import dealer
import alice
import bob


def __run(argv):
    if len(argv) < 4:
        print("Need to give length of n, x and y as arguments.")
        exit()
    else:
        #x = format(argv[2], 'b')
        #y = format(argv[3], 'b')
        x = 0b00000001
        y = 0b00000010

        dealer.__init(int(argv[1]))
        dealer.init_alice(x)
        dealer.init_bob(y)
        bob.receive(alice.send())
        v, z_b = bob.send()
        alice.receive(v, z_b)

        print(alice.output_z())


__run(sys.argv)

import sys

import dealer
import alice
import bob


def __run(argv):
    if len(argv) < 2:
        print("Need to give length of n as argument.")
        exit()
    else:
        dealer.__init(int(argv[1]))
        alice.__init_variables()
        bob.__init_variables()
        bob.receive(alice.send())
        alice.receive(bob.send()[0], bob.send()[1])
        print(alice.output_z())


__run(sys.argv)

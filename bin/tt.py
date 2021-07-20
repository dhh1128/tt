import os
import sys

# Add the python package to path so we can invoke it.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tt.app import main


if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print('')

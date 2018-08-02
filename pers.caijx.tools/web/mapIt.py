#! python3
# mapIt.py - Lauches a map in the browser using an address from the
# command line or clipboard.
import webbrowser,sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

# todo: Get address from clipboard.
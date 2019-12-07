import argparse
from gmpl import *

def main():
    parser = argparse.ArgumentParser()
    def add_extension(value):
        if not value.endswith('.gmpl'):
            value += '.gmpl'
        return value
    parser.add_argument('dest_file', type=add_extension, metavar='OUTPUT_FILE')
    parser.add_argument('--info-file', '-I', dest='info_file')
    parser.add_argument('--mod-file', '-m', dest='mod_file', action='append', default=[])
    parser.add_argument('--cdn-mod', '-c', dest='mod_cdn', action='append', nargs=1, default=[])
    parser.add_argument('--cdn-mod-specific', '-s', dest='specific_mod', action='append', nargs=2, default=[])
    parser.add_argument('--resources-file', '-r', dest='resources_file', action='append', default=[])
    parser.add_argument('--cdn-resources', '-C', dest='resources_cdn', action='append', nargs=1, default=[])
    parser.add_argument('--cdn-resources-specific', '-S', dest='specific_resources', action='append', nargs=2, default=[])

    args = parser.parse_args()
    print(args)
    create_gmpl_file(args.mod_file, args.mod_cdn+args.specific_mod, args.dest_file,
        json.load(open(args.info_file)), args.resources_file, args.resources_cdn+args.specific_resources)

if __name__ == '__main__': main()
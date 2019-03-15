#!/usr/bin/python3
import sys
import argparse
from reporting import report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Provides different methods of entropy calculation.')
    parser.add_argument("-i", dest="input_path", required=True, help="Input path (file or directory).")
    parser.add_argument("-d", dest="is_directory", default=False, help="Indicates if a dirctory should be processed.", action="store_true")
    parser.add_argument("-o", dest="output_path", default="", help="Output report file path.")
    parser.add_argument("-q", dest="quite", default=False, help="Surpress console messages.", action="store_true")
    parser.add_argument("-g", dest="is_graph", default=False, help="Create a graph of Shannon entropy oscillations.", action="store_true")
    parser.add_argument("-s", dest="step", default=512, help="File slice in bytes used to calculate Shannon entropy.", type=int)
    parser.add_argument("-b", dest="start_block", default=0, help="Graph start offset in bytes.", type=int)
    parser.add_argument("-e", dest="end_block", default=0, help="Graph end offset in bytes. If set to 0, the range up to the end of file is taken.")
    args = parser.parse_args()

    reporting = report(args.quite)

    if args.is_directory:
        if not args.is_graph:
            reporting.process_directory_report(args.input_path, args.output_path)
            
        else:
            reporting.process_directory_graphs(args.input_path, args.step)
    else:
        if not args.is_graph:
            reporting.write_file_report(args.input_path, args.output_path)
        else:
            reporting.write_file_graph(args.input_path, args.output_path, args.step)
	
#!/usr/bin/python3
import sys
import argparse
from entrolib import *
from reporting import report


def write_entropy_graph(in_file_name, out_file_name, step):
    """
    Calculates entropy variation for a file and write it to CSV spreadsheet.
    """
    byte_array = []
    with open(in_file_name, "rb") as f:
        byte_array = f.read()

    entropies = compute_entropy_graph(byte_array, step)
    with open(out_file_name, "w") as file_out:
        file_out.write("Entropy (per %d bytes);High Entropy\r\n" % step)
        for i in range(len(entropies)):
            file_out.write("%f;%s\r\n" % (entropies[i][0], str(entropies[i][1]) if entropies[i][1] == 8 else ""))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Provides different methods of entropy calculation.')
    parser.add_argument("-i", dest="input_path", required=True, help="Input path (file or directory).")
    parser.add_argument("-d", dest="is_directory", default=False, help="Indicates if a dirctory should be processed.", action="store_true")
    parser.add_argument("-o", dest="output_path", default="", help="Output report file path.")
    #parser.add_argument("-s", dest="is_shannon", default=True, help="Calculate Shannon entropy.", action="store_true")
    #parser.add_argument("-p", dest="is_pi", default=False, help="Calculate Monte Carlo Pi approximation deviation.", action="store_true")
    #parser.add_argument("-c", dest="is_chi", default=False, help="Calculate Chi-Squared.", action="store_true")
    parser.add_argument("-q", dest="quite", default=False, help="Surpress console messages.", action="store_true")
    parser.add_argument("-g", dest="is_graph", default=False, help="Create a graph of Shannon entropy oscillations.", action="store_true")
    parser.add_argument("-b", dest="step", default=512, help="File slice in bytes used to calculate Shannon entropy.")
    #parser.add_argument("START", dest="step", default=0, help="File slice in bytes used to calculate Shannon entropy. If 0 the whole range is taken into calculation.")
    #parser.add_argument("END", dest="step", default=0, help="File slice in bytes used to calculate Shannon entropy. If 0 the whole range is taken into calculation.")
    args = parser.parse_args()

    reporting = report(args.quite)

    if args.is_directory:
        if not args.is_graph:
            reporting.process_directory_report(args.input_path, args.output_path)
            
        else:
            reporting.process_directory_graphs(args.input_path, args.step)
    else:
        if not args.is_graph:
            # TODO: Single file general report here.
            pass
        else:
            reporting.write_entropy_graph(args.input_path, args.output_path, args.step)

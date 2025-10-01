

import sys
import subprocess

from ragtag_utilities.utilities import get_ragtag_version


def main():
    VERSION = get_ragtag_version()
    CITATION = """
Alonge, Michael, et al. "Automated assembly scaffolding elevates a new tomato system for high-throughput genome editing."
Genome Biology (2022). 
https://doi.org/10.1186/s13059-022-02823-7

** RagTag supersedes RaGOO **

Alonge, Michael, et al. "RaGOO: fast and accurate reference-guided scaffolding of draft genomes."
Genome biology 20.1 (2019): 1-17.
https://doi.org/10.1186/s13059-019-1829-6
    """

    description = """
RagTag: Tools for fast and flexible genome assembly scaffolding and improvement.
Version: %s

usage: ragtag.py <command> [options]
    
    assembly improvement:
      correct         homology-based misassembly correction
      scaffold        homology-based assembly scaffolding
      patch           homology-based assembly patching
      merge           scaffold merging
      
    file utilities:
      agp2fa          build a FASTA file from an AGP file
      agpcheck        check for valid AGP file format
      asmstats        assembly statistics
      splitasm        split an assembly at gaps
      delta2paf       delta to PAF file conversion
      paf2delta       PAF to delta file conversion
      updategff       update gff intervals
      

    options:
      -c, --citation  
      -v, --version""" % VERSION

    arg_len = len(sys.argv)
    if arg_len == 1:
        print(description)

    if arg_len > 1:
        cmd = sys.argv[1]

        if cmd == "-h" or cmd == "--help":
            print(description)

        elif cmd == "-v" or cmd == "--version":
            print(VERSION)

        elif cmd == "-c" or cmd == "--citation":
            print(CITATION)

        elif cmd == "correct":
            subcmd = ["ragtag_correct.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "scaffold":
            subcmd = ["ragtag_scaffold.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "merge":
            subcmd = ["ragtag_merge.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "patch":
            subcmd = ["ragtag_patch.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "agp2fa":
            subcmd = ["ragtag_agp2fa.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "agpcheck":
            subcmd = ["ragtag_agpcheck.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "updategff":
            subcmd = ["ragtag_update_gff.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "asmstats":
            subcmd = ["ragtag_asmstats.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "splitasm":
            subcmd = ["ragtag_splitasm.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "delta2paf":
            subcmd = ["ragtag_delta2paf.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "paf2delta":
            subcmd = ["ragtag_paf2delta.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        else:
            print(description)
            print("\n** unrecognized command: %s **" % cmd)


if __name__ == "__main__":
    main()

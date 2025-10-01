## Retrieval Argumented Generation Tag 

RagTag is a collection of software tools for scaffolding and improving modern genome assemblies. Tasks include:

RagTag also provides [command line utilities](https://github.com/oliveira-mtcode/retrieval_tag/wiki/Usage) for working with common genome assembly file formats.

## Getting Started

```bash
# install with conda
conda install -c bioconda ragtag

# correct a query assembly
ragtag.py correct ref.fasta query.fasta

# scaffold a query assembly
ragtag.py scaffold ref.fasta query.fasta

# scaffold with multiple references/maps
ragtag.py scaffold -o out_1 ref1.fasta query.fasta
ragtag.py scaffold -o out_2 ref2.fasta query.fasta
ragtag.py merge query.fasta out_*/*.agp other.map.agp

# use Hi-C to resolve conflicts
ragtag.py merge -b hic.bam query.fasta out_*/*.agp other.map.agp

# make joins and fill gaps in target.fa using sequences from query.fa
ragtag.py patch target.fa query.fa
```

## Docs
Please see the [Wiki](https://github.com/oliveira-mtcode/retrieval_tag/wiki) for detailed documentation.

## Dependencies
- Python 3 (with the following auto-installed packages)
    - numpy
    - intervaltree
    - pysam
    - networkx
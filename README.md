# Bioinformatics Cheat Sheet

Hello! This repo contains several sample code snippets that might be useful for someone beginning to learn bioinformatics. I will try to keep it up to date as I come across tools that I use particularly often.

# Setting up your environment

To ensure that downloads here don't interfere with your current working environment, here are some steps to set up a virtual environment where you can set up these bioinformatics tools:

### Install Miniforge:  

1. Download the Miniforge installer for your platform from the Miniforge releases page: [Miniforge Releases](https://github.com/conda-forge/miniforge/releases)
2. Open a terminal or command prompt.
3. Navigate to the directory containing the downloaded installer.
4. Run the installer script:  
   `bash Miniforge3-latest-MacOSX-x86_64.sh  # Replace with the actual filename`

### Create and Activate Conda Environment:  

We will call this environment "bioinformatics":
`conda create -n bioinformatics  
conda activate bioinformatics`

### Install and Verify Tools:

Here are the tools that the code in this repository requires. I've added a description and link to each tool's documentation below:

`conda install -c bioconda samtools bedtools biopython gtfparse  
pip install gseapy`

| Package | Description | Link to Documentation |
| -------- | -------- | -------- |
| Biopython | Manipulating, translating, and reverse-complementing sequences, among others | https://biopython.org/wiki/Documentation |
| samtools | Sorting, viewing, and otherwise performing analyses involving .sam or .bam files, which are the primary outputs for most RNA-seq pipelines | http://www.htslib.org/doc/samtools.html#DESCRIPTION |
| bedtools | [bedtools intersect](https://bedtools.readthedocs.io/en/latest/content/tools/intersect.html#u-unique-reporting-the-mere-presence-of-any-overlapping-features) in particular finds overlaps between two sets of genetic features, in .bed format | https://bedtools.readthedocs.io/en/latest/# |
| gtfparse | Reads .gtf files, which are the primary format for annotating the locations of genes and transcripts | https://pypi.org/project/gtfparse/ |
| gseapy | Runs tests for enrichment of pathways or gene sets, given lists of genes | https://gseapy.readthedocs.io/en/latest/introduction.html |

You'll also want to ensure that these are properly installed, which you can accomplish by running the following code snippet:

`<br>
samtools --version  
bedtools --version  
python -c "import Bio; print(Bio.__version__)"  
python -c "import gtfparse; print(gtfparse.__version__)"  
gseapy --version  
<br>`

Under this setup, you'll need to activate the environment (conda activate myenv) every time you want to use these tools and packages.

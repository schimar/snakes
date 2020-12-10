
FILES = [ os.path.basename(x) for x in glob.glob("raw/*") ]

SAMPLES = list(set([ "_".join(x.split("_")[:2]) for x in FILES]))

CONDITIONS = list(set(x.split("_")[0] for x in SAMPLES))


for path in DIRS:
    if not os.path.exists(path):
        os.mkdir(path)


rule all:
    input:
        expand('Trimming/{sample}_R1.trim.fastq', sample=SAMPLES)


rule trimming:
    input:
        adapters = ADAPTERS,
        r1 = '{sample}_R1.fastq.gz',
        r2 = '{sample}_R2.fastq.gz'

    output:
        r1 = 'Trimming/{sample}_R1.trim.fastq',
        r2 = 'Trimming/{sample}_R2.trim.fastq'

    message: ''' --- Trimming  --- '''

    shell: ' bbduk.sh in1="{input.r1}" in2="{input.r2}" out1="{output.r1}" out2="{output.r2}" \
        ref="{input.adapters}" minlen='+str(minlen)+' ktrim='+ktrim+' k='+str(k)+   \
        ' qtrim='+qtrim+' trimq='+str(trimq)+' hdist='+str(hdist)+' tpe tbo '

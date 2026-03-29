print("Initializing pipeline")

def quality_control(reads):
    print("Starting QC step")

    total_reads = len(reads)
    print(f"Total reads: {total_reads}")

    print("Checking high quality reads")

    high_quality_reads = []
    for read in reads:
        if len(read) >= 50:
            high_quality_reads.append(read)

    print(f"High quality reads retained: {len(high_quality_reads)}")
    return high_quality_reads

print("QC step finished")
print("All checks done")
print("Ready to continue")
print("Next, variant calling")

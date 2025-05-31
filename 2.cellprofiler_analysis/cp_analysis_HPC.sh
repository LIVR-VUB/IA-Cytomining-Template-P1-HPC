#!/bin/bash
#SBATCH --job-name=mhsc144hcp
#SBATCH --partition=zen5_mpi
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
#SBATCH --mem=64G
#SBATCH --time=72:00:00
#SBATCH --output=logs/%x_%j.out


module purge
module load Mamba
source $EBROOTMAMBA/etc/profile.d/conda.sh
conda activate cytomining_a

cd /rhea/scratch/brussel/vo/000/bvo00026/vsc11013/Data/Cytomining/2423_mHSC_TGF_144H/2.cellprofiler_analysis/

mkdir -p scripts

jupyter nbconvert --to python --output-dir=scripts/ *.ipynb

python scripts/cp_analysis.py 

python scripts/rename_sqlite_files.py

conda deactivate

export MAX_WORKERS=$SLURM_CPUS_PER_TASK

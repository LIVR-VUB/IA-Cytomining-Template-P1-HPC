#!/bin/bash
#SBATCH --job-name=mhsc144hic
#SBATCH --partition=zen5_mpi
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G
#SBATCH --time=12:00:00
#SBATCH --output=logs/%x_%j.out


module purge
module load Mamba
source $EBROOTMAMBA/etc/profile.d/conda.sh
conda activate cytomining_a

cd /scratch/brussel/vo/000/bvo00026/vsc11013/Data/Cytomining/2423_mHSC_TGF_144H/1.cellprofiler_ic

mkdir -p scripts

jupyter nbconvert --to python --output-dir=scripts/ *.ipynb

python scripts/cp_ic.py 

conda deactivate

export MAX_WORKERS=$SLURM_CPUS_PER_TASK

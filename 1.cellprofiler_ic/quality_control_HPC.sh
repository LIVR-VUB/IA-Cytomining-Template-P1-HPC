```bash
#!/bin/bash
#SBATCH --job-name=mhsc144h
#SBATCH --partition=zen4
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=6:00:00
#SBATCH --output=logs/%x_%j.out


module purge
module load Mamba
source $EBROOTMAMBA/etc/profile.d/conda.sh
conda activate cytomining_a

cd /scratch/brussel/vo/000/bvo00026/vsc11013/Data/Cytomining/2423_mHSC_TGF_144H/1.cellprofiler_ic/image_quality_control

mkdir -p scripts

jupyter nbconvert --to python --output-dir=scripts/ *.ipynb

python scripts/0.whole_image_qc.py 

conda deactivate

export MAX_WORKERS=$SLURM_CPUS_PER_TASK
```

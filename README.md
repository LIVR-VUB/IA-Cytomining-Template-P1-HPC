# CytoMining-Template-HPC

This repository provides a structured and reproducible template for performing image-based profiling using high-content imaging data on an HPC environment. The workflow is based on the CellProfiler + cytomining pipeline and supports batch processing using SLURM job scripts.

## Overview

The pipeline follows the typical stages of a cytomining project:

1. Raw Data Collection: Store image files and plate layout information.
2. Preprocessing: Clean and annotate metadata.
3. Image Analysis: Run CellProfiler pipelines in batch mode on HPC.
4. Feature Extraction: Export single-cell features and aggregate profiles.
5. Downstream Analysis (future scope): Apply profiling tools for classification, clustering, or drug response analysis.

## Repository Structure

```

├── 0a\_raw\_data/                     # Raw images (e.g., TIFFs) organized by plate
├── 0b\_preprocessing\_data\_metadata/ # Plate metadata & annotations
├── 1\_cellprofiler\_ic/              # CellProfiler pipeline (.cpproj) and input configs
├── 2\_cellprofiler\_analysis/        # SLURM scripts to run CellProfiler on HPC
├── environments/                   # Conda environment YAMLs
├── utils/                          # Helper scripts (e.g., rename, tile, check masks)
├── .gitattributes
├── .gitignore
└── test.md                         # Notes or test cases (optional)

````

## Requirements

- SLURM HPC cluster
- Conda or Mamba
- CellProfiler >= 4.2.1
- Python >= 3.8
- R (optional, for metadata cleaning)

To set up the environment, use:

```bash
conda env create -f environments/cytomining_a.yml
conda activate cytomining_a
````

## How to Run

1. Upload your image and metadata to the `0a_raw_data` and `0b_preprocessing_data_metadata` folders respectively.
2. Edit the CellProfiler pipeline (`.cpproj`) in `1_cellprofiler_ic`.
3. Submit your SLURM job using the template script:

```bash
cd 2_cellprofiler_analysis
sbatch cp_analysis_HPC.sh
```

4. Output features and logs will be saved in the `2_cellprofiler_analysis/` folder.

## Notes

* Ensure each image has a corresponding mask or label file if required for segmentation.
* Follow naming conventions for compatibility with CellProfiler modules.
* Use scripts in `utils/` for common preprocessing tasks, such as:

  * Renaming channels
  * Checking image–mask pairs
  * Converting `.tiff` to `.tif`

## To-Do

* [ ] Add PyCytominer scripts for normalization and profiling
* [ ] Integrate Napari viewer plugin (optional)
* [ ] Add batch processing for large-scale datasets
* [ ] Publish sample dataset and test pipeline

## License

This repository is for academic and research purposes. License to be specified.

## Contact

Maintained by [arka2696](https://github.com/arka2696)
PhD Fellow at VUB | Biomedical Image Analysis and AI

```

Let me know if you want me to tailor the environment setup instructions or CellProfiler details further. I can also generate a ready-to-upload `README.md` file if you'd like.
```

import os
import re
import shutil

# Define the directory containing the original files
source_directory = '/scratch/brussel/vo/000/bvo00026/vsc11013/Data/Cytomining/2403_mHSC_8Compounds_Stefaan/0a.raw_data/HSC005_sliced'

# Define the directory to save the renamed files
target_directory = '/scratch/brussel/vo/000/bvo00026/vsc11013/Data/Cytomining/2403_mHSC_8Compounds_Stefaan/0b.preprocessing_data_metadata/Plate_3'

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# Define the regex pattern to match old file names (case insensitive)
pattern = re.compile(r'scan_Plate_TM_p00_0_([A-Z]\d{2})f(\d{2})d(\d)\.TIF', re.IGNORECASE)

# Define the mapping for channels
channel_map = {
    "0": ("1", "DAPI"),  # Channel becomes 1, Name is DAPI
    "1": ("2", "GFP"),   # Channel becomes 2, Name is GFP
    "2": ("4", "RFP")   # Channel becomes 3, Name is RFP
}

# Iterate over files in the source directory
for filename in os.listdir(source_directory):
    print(f'Processing file: {filename}')
    # Check if the file name matches the regex pattern
    match = pattern.match(filename)
    if match:
        # Extract the matched groups
        well_position = match.group(1)  # e.g., A04
        site_number = int(match.group(2)) + 1  # e.g., 10 -> 11
        channel_number = match.group(3)  # e.g., 0

        # Map the channel number to its new numeric representation and name
        channel_info = channel_map.get(channel_number, ("Unknown", "Unknown"))
        new_channel_number, channel_name = channel_info

        # Create the new file name using the extracted groups
        # Well_Position_01_Channel_Site_ChannelName_001.tif
        new_filename = f'{well_position}_01_{new_channel_number}_{site_number}_{channel_name}_001.tif'

        # Get the full paths
        old_file_path = os.path.join(source_directory, filename)
        new_file_path = os.path.join(target_directory, new_filename)

        print(f'Old file path: {old_file_path}')
        print(f'New file path: {new_file_path}')

        # Check if the old file exists
        if os.path.exists(old_file_path):
            # Copy and rename the file
            shutil.copy2(old_file_path, new_file_path)
            print(f'Copied and renamed: {filename} -> {new_filename}')
        else:
            print(f'File not found: {old_file_path}')
    else:
        print(f'File name does not match pattern: {filename}')

print('Renaming and copying completed.')


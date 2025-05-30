import os
import re
import shutil

# Define the directory containing the original files
source_directory = '/home/arka/Desktop/Arka/00U4172H/Images'

# Define the directory to save the renamed files
target_directory = '/home/arka/Desktop/Cytomining/CellProfiler_Pycytominer/nf1_schwann_cell_painting_data/0.download_data/Plate_6'

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# Define the regex pattern to match new file names
pattern = re.compile(r'(r\d{2})c(\d{2})f(\d{2})p01-(ch\d)sk1fk1fl1\.tiff', re.IGNORECASE)

# Define the mapping for channels
channel_map = {
    "ch1": ("CY5", "5"),  # DAPI is channel 4, new label is 1
    "ch2": ("RFP", "4"),   # GFP is channel 3, new label is 2
    "ch3": ("CY3", "3"),   # RFP is channel 2, new label is 4
    "ch4": ("GFP", "2"),    # CY5 is channel 1, new label is 3
    "ch5": ("DAPI", "1")
}

# Define row mappings (fixing microscope mislabeling)
row_map = {
    "r03": "C",  # r04 corresponds to row C
    "r04": "D",  # r06 corresponds to row E
    "r05": "E",  # r08 corresponds to row G
    "r06": "F",  # r10 corresponds to row I
    "r07": "G",  # Add more if necessary
}

# Iterate over files in the source directory
for filename in os.listdir(source_directory):
    print(f'Processing file: {filename}')
    
    # Check if the file name matches the regex pattern
    match = pattern.match(filename)
    if match:
        # Extract the matched groups
        row_code = match.group(1)     # Extract rXX
        well_column = match.group(2)  # Extract cXX
        site_number = int(match.group(3)) + 1  # Convert fXX, increment
        channel_code = match.group(4).lower() # Extract channel (e.g., ch3)

        # Correct the well position by mapping row_code (rXX → Letter)
        row_letter = row_map.get(row_code, "X")  # Default to "X" if not found
        well_position = f"{row_letter}{well_column}"  # Combine row and column

        # Map the channel number to its new numeric representation and name
        channel_info = channel_map.get(channel_code, ("Unknown", "Unknown"))
        channel_name, new_channel_number = channel_info

        # Create the new file name using the extracted groups
        # Format: Well_Position_01_Channel_Site_ChannelName_001.tif
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

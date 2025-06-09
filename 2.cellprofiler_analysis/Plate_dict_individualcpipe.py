# create plate info dictionary with specified plates for the CellProfiler CLI command
plate_info_dictionary = {
    name: {
        "path_to_images": pathlib.Path(
            list(images_dir.rglob(f"Corrected_{name}"))[0]
        ).resolve(strict=True),
        "path_to_output": pathlib.Path(f"{output_dir}/{name}"),
    }
    for name in plate_names
    if not any((output_dir / name).glob("*.sqlite"))  # only process plates that have not been processed yet
}

# mapping of Plates 3–5 to their 3-channel .cppipe files
three_channel_pipelines = {
    "Plate_3": "./Analysis_3channelHSC005.cppipe",
    "Plate_4": "./Analysis_3channelHSC006.cppipe",
    "Plate_5": "./Analysis_3channelHSC008.cppipe",
}

# default fallback for any other plate (e.g. 4-channel)
default_four_channel = "./NF1_analysis_4channel.cppipe"

# assign the correct pipeline to each plate in the dictionary
for name, info in plate_info_dictionary.items():
    if name in three_channel_pipelines:
        info["path_to_pipeline"] = pathlib.Path(
            three_channel_pipelines[name]
        ).resolve(strict=True)
    else:
        info["path_to_pipeline"] = pathlib.Path(
            default_four_channel
        ).resolve(strict=True)

# view the dictionary to confirm
pprint.pprint(plate_info_dictionary, indent=4)

import argparse
import csv, os

from utility import get_prediction_files

parser = argparse.ArgumentParser(
    description='Make predictions with signature network',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)


parser.add_argument('--main_path', type=str, required=True, help='Path to directory consisting of .h5-models (to use for predicting)')
parser.add_argument('--csvs_folder', type=str, required=True)

if __name__ == "__main__":
    args = parser.parse_args()
    main_path = args.main_path
    csvs_folder = args.csvs_folder

    path_to_csvs = os.path.join(main_path, csvs_folder)

    predicted_files = get_prediction_files(path_to_csvs)
    print(predicted_files)

    output_folder = os.path.join(main_path,"statistics")

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    files_path = os.path.join(output_folder, "initial_stats")
    if not os.path.exists(files_path):
        os.mkdir(files_path)

    predicted_files = sorted(predicted_files)
    for i, file in enumerate(predicted_files):
        path = os.path.join(path_to_csvs, file)
        print(file)
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # 1. get videos names
            VIDEO_DIR = "/home/cslfiu/dev/cnn_vscf/NSF-REU-2024_VSCF/data/raw"
            DEVICES = [item for item in os.listdir(VIDEO_DIR) if os.path.isdir(os.path.join(VIDEO_DIR, item))]

            FILTERED_RESULTS = []
            
            newreader = []
            for row in reader:
                # '/home/cslfiu/dev/cnn_vscf/NSF-REU-2024_VSCF/data/generated_patchesFool/Testing/IPhone/quadrant_1/iPhone-xsMax-2(14)/iPhone-xsMax-2(14).MOV_010_P-number_024.jpg'
                file_name_row = row["File"]
                video_name = file_name_row.split("/")[-1].split(".")[0]
                row["Video Name"] = video_name
                newreader.append(row)
                

            # print(newreader)
        file_name = 'output_frames_stats_' + str(i) + '_.csv'
        csv_path = os.path.join(files_path, file_name)
        with open(csv_path, 'w') as csvfile:
            fieldnames = reader.fieldnames
            fieldnames.append("Video Name")
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for data in newreader:
                writer.writerow(data)




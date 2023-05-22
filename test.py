import os

video_folder = os.path.join(os.getcwd(), "Segmented_Video")
subject_dirs = os.listdir(video_folder)
for subject_dir in subject_dirs:
    subject_dir_path = os.path.join(video_folder, subject_dir)
    if os.path.isdir(subject_dir_path):
        for vid in os.listdir(subject_dir_path):
            if 'clip' in vid.lower() and vid.endswith('mp4'):
                full_path = os.path.join(subject_dir_path, vid)
                print(full_path)


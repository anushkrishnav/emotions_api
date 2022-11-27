
from fer import Video, FER
import os
import sys
import pandas as pd
import cv2

def get_frame_count(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return frame_count




async def process_data(video_path, file_name):
    
    face_detector = FER(mtcnn=True)
    input_video = Video(video_path)
    frame_count = get_frame_count(video_path)
    print(f"Frame count: {frame_count}")

    processing_data = input_video.analyze(face_detector, display=False,frequency=round(frame_count/10))

    vid_df = input_video.to_pandas(processing_data)
    vid_df = input_video.get_first_face(vid_df)
    vid_df = input_video.get_emotions(vid_df)

    # save the data to a csv file
    data_file = "app/data/csv/"
    if not os.path.isdir(data_file):
        os.makedirs(data_file)
    data_file += f"{file_name}.csv"
    vid_df.to_csv(data_file, index=False)
    return vid_df
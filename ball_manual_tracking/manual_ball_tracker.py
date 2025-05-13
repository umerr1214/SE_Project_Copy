import cv2
import json

def main(video_path, output_json):
    cap = cv2.VideoCapture(video_path)
    cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
    frame_number = 0
    predicted_path = []

    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    print("Instructions:")
    print("- Click on the ball in every frame where it is visible.")
    print("- Press any key to go to next frame.")
    print("- If ball is not visible in a frame, just press any key (no click).")
    print("- Close window or press 'q' to exit early.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        coords = []

        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                coords.append((x, y))
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
                cv2.imshow('Frame', frame)

        cv2.imshow('Frame', frame)
        cv2.setMouseCallback('Frame', click_event)

        key = cv2.waitKey(0)
        if key == ord('q'):
            break

        if coords:
            # Take the first click (ignore extras)
            x, y = coords[0]
            predicted_path.append({
                "pos_x": int(x),
                "pos_y": int(y),
                "pos_z": 0.0,
                "timestamp": 0.0
            })

        frame_number += 1

    cap.release()
    cv2.destroyAllWindows()

    # Save to json
    with open(output_json, "w") as outfile:
        json.dump(predicted_path, outfile, indent=4)

    print(f"\nDone! {len(predicted_path)} points saved to {output_json}")

if __name__ == "__main__":
    video_file = "input_video3.avi"          # <-- Change this to your actual video filename
    output_file = "predicted_path.json"
    main(video_file, output_file)

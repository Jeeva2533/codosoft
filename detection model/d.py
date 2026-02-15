import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

mode = input("Enter 'image' or 'video': ").strip().lower()

if mode == "image":
    image_path = input("Enter image path: ").strip()
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        exit()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite("detected_faces_image.jpg", img)
    print("Face detection complete! Output saved as detected_faces_image.jpg")

elif mode == "video":
    video_path = input("Enter video path: ").strip()
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("detected_faces_video.mp4", fourcc, 20.0,
                          (int(cap.get(3)), int(cap.get(4))))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        out.write(frame)

    cap.release()
    out.release()
    print("Face detection complete! Output saved as detected_faces_video.mp4")

else:
    print("Invalid mode. Enter 'image' or 'video'.")

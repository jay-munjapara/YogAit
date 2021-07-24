from flask import Flask,render_template,Response
import cv2
import mediapipe as mp
import numpy as np
import time
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

app=Flask(__name__)
camera=cv2.VideoCapture(0)

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle

def generate_frames(num = 0):
    TIMER = int(10)
    prev = time.time()
    cap = cv2.VideoCapture(0)
    # Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Recolor back to BGR
            image.flags.writeable = True
            
            try:
                landmarks = results.pose_landmarks.landmark
                if num == 1:
                    # Get coordinates - left
                    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

                    # Get coordinates - right
                    shoulder1 = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    hip1 = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                    knee1 = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

                    # Calculate angle
                    angle = calculate_angle(shoulder, hip, knee)
                    angle1 = calculate_angle(shoulder1, hip1, knee1)
                    if angle and 110 <= angle <= 140 and TIMER > 0 :
                        cv2.putText(image, "Yes", 
                                    tuple(np.multiply([0.8,0.1], [640, 480]).astype(int)), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 2, cv2.LINE_AA
                                        )
                        # Update and keep track of Countdown
                        # if time elapsed is one second
                        # than decrease the counter
                        if cur-prev >= 1:
                            prev = cur
                            TIMER = TIMER-1

                    elif TIMER <=0 :
                        cv2.putText(image, "Done", 
                                    tuple(np.multiply([0.8,0.1], [640, 480]).astype(int)), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2, cv2.LINE_AA
                                        )

                    else:
                        cv2.putText(image, "No", 
                                    tuple(np.multiply([0.8,0.1], [640, 480]).astype(int)), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 2, cv2.LINE_AA
                                        )
                    # Visualize angle
                    # cv2.putText(image, str(angle), 
                    #                 tuple(np.multiply(hip, [640, 480]).astype(int)), 
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2, cv2.LINE_AA
                    #                     )
                    # cv2.putText(image, str(angle1), 
                    #                 tuple(np.multiply(hip1, [640, 480]).astype(int)), 
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2, cv2.LINE_AA
                    #                     )
                    
                    # Extract landmarks
                elif num == 2:
                    # Get coordinates - left
                    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

                    # Calculate angle
                    angle = calculate_angle(shoulder, hip, knee)
                    if angle and angle <= 160 and TIMER > 0 :
                        cv2.putText(image, "Yes", 
                                    tuple(np.multiply([0.8,0.1], [640, 480]).astype(int)), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 2, cv2.LINE_AA
                                        )
                        # Update and keep track of Countdown
                        # if time elapsed is one second
                        # than decrease the counter
                        if cur-prev >= 1:
                            prev = cur
                            TIMER = TIMER-1

                    elif TIMER <=0 :
                        cv2.putText(image, "Done", 
                                    tuple(np.multiply([0.8,0.1], [640, 480]).astype(int)), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2, cv2.LINE_AA
                                        )

                    else:
                        cv2.putText(image, "No", 
                                    tuple(np.multiply([0.8,0.1], [640, 480]).astype(int)), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 2, cv2.LINE_AA
                                        )
                    # Visualize angle
                    # cv2.putText(image, str(angle), 
                    #                 tuple(np.multiply(hip, [640, 480]).astype(int)), 
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2, cv2.LINE_AA
                    #                     )
                    # cv2.putText(image, str(angle1), 
                    #                 tuple(np.multiply(hip1, [640, 480]).astype(int)), 
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2, cv2.LINE_AA
                    #                     )
                    
            except:
                pass
            # Display countdown on each frame
            # specify the font and draw the
            # countdown using puttext
            cv2.putText(image ,str(TIMER) ,
                (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 255),
                2, cv2.LINE_AA)
            # current time
            cur = time.time()

            

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                        )               

            ret, image_conv = cv2.imencode('.jpg', image)
            frame_conv = image_conv.tobytes()

            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame_conv + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/instructionsLearn')
def instructionsLearn():
    return render_template('instructionsLearn.html')


@app.route('/instructionsPractice')
def instructionsPractice():
    return render_template('instructionsPractice.html')


@app.route('/learn')
def learn():
    return render_template('learn.html')


@app.route('/practice')
def practice():
    return render_template('practice.html')

@app.route('/selection')
def selection():
    return render_template('selection.html')

@app.route('/vajrasana')
def vajrasana():
    return render_template('vajrasana.html')

@app.route('/bhadrasana')
def bhadrasana():
    return render_template('bhadrasana.html')

@app.route('/bhujangasana')
def bhujangasana():
    return render_template('bhujangasana.html')

@app.route('/matsyasana')
def matsyasana():
    return render_template('matsyasana.html')

@app.route('/pashchimottanasana')
def pashchimottanasana():
    return render_template('pashchimottanasana.html')

@app.route('/pavanmuktasana')
def pavanmuktasana():
    return render_template('pavanmuktasana.html')

@app.route('/shavasana')
def shavasana():
    return render_template('shavasana.html')

@app.route('/trikonasana')
def trikonasana():
    return render_template('trikonasana.html')

@app.route('/utkatasana')
def utkatasana():
    return render_template('utkatasana.html')

@app.route('/uttanasana')
def uttanasana():
    return render_template('uttanasana.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/vajrasana_video')
def vajrasana_video():
    return Response(generate_frames(1), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/bhadrasana_video')
def bhadrasana_video():
    return Response(generate_frames(2), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
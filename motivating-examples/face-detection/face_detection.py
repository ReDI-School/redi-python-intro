import cv2

PATH_TO_IMAGES = './pictures'
PATH_TO_RESOURCES = './resources'
INPUT_FILES = ['beatles.jpg']

face_cascade_name = '/'.join((PATH_TO_RESOURCES, 'haarcascade_frontalface_default.xml'))

for file in INPUT_FILES:
    file_name = "/".join((PATH_TO_IMAGES, file))
    image = cv2.imread(file_name)
    result_image = image.copy()

    face_cascade = cv2.CascadeClassifier()
    face_cascade.load(face_cascade_name)

    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayimg = cv2.equalizeHist(grayimg)

    # Run the classifiers
    faces = face_cascade.detectMultiScale(grayimg, 1.1, 2, 0 | cv2.CASCADE_SCALE_IMAGE, (30, 30))

    print("Processing file %s" % file)

    if len(faces) != 0:
        face_number = 0
        for f in faces:
            x, y, w, h = [v for v in f]
            if w > 100: #hack to get rid of false positives
                face_number += 1
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 5)
                sub_face = image[y: y + h, x: x + w]

                face_file_name = "%s/face_%s.jpg" % (PATH_TO_IMAGES, face_number)
                cv2.imwrite(face_file_name, sub_face)
                result_image[y: y + sub_face.shape[0], x: x + sub_face.shape[1]] = sub_face
        print("%s faces detected" % face_number)
    else:
        print("no faces detected")

    cv2.imwrite('%s/result_%s' % (PATH_TO_IMAGES, file), result_image)

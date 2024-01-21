from deepface import DeepFace


class Gender_Model():

    def predict_gender(self, im,face_image):
        demography = DeepFace.analyze(im, actions=['gender'], enforce_detection=True)
        result_gender=demography["gender"]
        return result_gender

   
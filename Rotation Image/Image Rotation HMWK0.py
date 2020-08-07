import cv2
import numpy as np
import math


def matrix_multiplication(matrix1, matrix2):

    return np.matmul(matrix1, matrix2)

def open_image(image_name):
    origIM = cv2.imread(image_name)
    cv2.imshow("Here's a picture", origIM)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotate_image():
    #newx = use the given cos and sin values she gave for matirx rotation
    #newy = use the same concept

def find_center():
    #try to use trig and hypotenuse values to find the center

def create_backdrop():
    #need to make the larger image as a backdrop
    #her code - newIM = np.zeros( (size, size, 3), np.float32)




def main():
   A = np.array([[1,2,3,4],[5,6,7,8]])
   B = np.array([[2,3,4,5],[6,7,8,9]])
   print(A)
   print(B)
   A_2 = np.reshape([1,2,3,4,5,6,7,8],(4,2))
   print(A_2)
   print(matrix_multiplication(A_2, B))




if __name__ == "__main__":
    main()
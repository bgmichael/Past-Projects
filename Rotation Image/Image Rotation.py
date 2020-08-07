import cv2
import numpy as np
import math


def matrix_multiplication(matrix1, matrix2):

    return np.matmul(matrix1, matrix2)

def image_rotation(image, angle):

    origIM = cv2.imread(str(image))
    imH = origIM.shape[0]
    imW = origIM.shape[1]
    black_image = np.zeros((imH, imW, 3))
    black_image2 = black_image
    black_image3 = black_image
    black_image4 = black_image

    #combine images for bigger image

    img = cv2.imread("Pyramids.png")
    combIM = np.concatenate((origIM, black_image), axis=1)
    cv2.imwrite("First_comb.png", combIM)
    combIM = cv2.imread("First_comb.png")

    combIM2 = np.concatenate((black_image2, black_image3), axis=1)
    cv2.imwrite("second_image_combo.png", combIM2)
    combIM2 = cv2.imread("second_image_combo.png")

    LowerIM = np.concatenate((combIM2, combIM2), axis=0)
    cv2.imwrite("third_image_combo.png", LowerIM)
    LowerIM = cv2.imread("third_image_combo.png")

    SideIM = np.concatenate((LowerIM, combIM2), axis=0)
    cv2.imwrite("fourth_image_combo.png", SideIM)
    SideIM = cv2.imread("fourth_image_combo.png")

    RightIM = np.concatenate((combIM, LowerIM), axis=0)
    cv2.imwrite("Right_combo_image.png", RightIM)
    RightIM = cv2.imread("Right_combo_image.png")

    fullIM = np.concatenate((RightIM, SideIM), axis=1)
    cv2.imwrite("Final_combo.png", fullIM)
    fullIM = cv2.imread("Final_combo.png")

    ### Value for rotation matrix
    origIM_BlackBack = cv2.imread("Final_combo.png")
    IM_B_H = origIM_BlackBack.shape[0]
    IM_B_W = origIM_BlackBack.shape[1]  ### new image is 600 by 1650
    Down_Shift = int((IM_B_H // 3) + 1)
    Right_Shift = int((IM_B_W // 3) + 1)

    ### Move Image
    for i in range(imH):
        for j in range(imW):
            original_color = origIM_BlackBack[imH - i][imW - j]  # Store the color of the picture
            # original_location = np.reshape([j, i], (1, 1))#Store the location of the picture
            black = origIM_BlackBack[IM_B_H - 1][IM_B_W - 1]
            # new_color = origIM_BlackBack[(i + Down_Shift)][(j + Right_Shift)]#color of pixel to be overwritten
            origIM_BlackBack[((imH - i) + Down_Shift)][((imW - j) + Right_Shift)] = original_color  # change black pixel to picture
            origIM_BlackBack[imH - i][imW - j] = black

    ####### Math and constants

    rm0_0 = math.cos(angle)
    rm0_1 = (-1) * math.sin(angle)
    rm1_0 = math.sin(angle)
    rm1_1 = math.cos(angle)

    rotation_matrix_r = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
    # print(rotation_matrix_r)
    # print(origIM[0][1])
    a = 0
    b = 0
    icount = 0
    jcount = 0
    j_length = range(imW)
    i_length = range(imH)
    alteredIM = origIM_BlackBack.copy()
    alteredIM_blacked = np.zeros_like(alteredIM)


    Down_Shift = int((IM_B_H // 3) + 1)
    Right_Shift = int((IM_B_W // 3) + 1)
    black = origIM_BlackBack[IM_B_H - 1][IM_B_W - 1]
    distance = 0

    ##### ACTUAL ROTATION MATH########
    for i in range(imH):  # access the y coordinate in the matrix
        icount = icount + 1
        for j in range(imW):  # access the x coordinate in the matrix
            jcount = jcount + 1
            x_start = (imW + Right_Shift) - j
            y_start = (imH + Down_Shift) - i
            pixel_color_holder = origIM_BlackBack[y_start][x_start]
            pixel_place_array = np.reshape([(y_start), (x_start)], (2, 1))

            rotated_pixel_value = np.matmul(rotation_matrix_r, pixel_place_array)


            rotated_pixel_value1 = rotated_pixel_value.item(0)  # the array value r0c0
            rotated_pixel_value1 = int(rotated_pixel_value1)  # round off the calculated value
            rotated_pixel_value2 = rotated_pixel_value.item(1)  # the array value r1c0
            rotated_pixel_value2 = int(rotated_pixel_value2)  # round off the value
            rotated_pixel_value[0] = rotated_pixel_value1  # set the array to the rounded values
            rotated_pixel_value[1] = rotated_pixel_value2  # set the array to the rounded values
            ## rotated_pixel_value is now the new spot that the color for origIM should go to
            rotated_pixel_value[0, 0] = rotated_pixel_value1
            rotated_pixel_value[1, 0] = rotated_pixel_value2

            x = int(rotated_pixel_value.item(0))
            y = int(rotated_pixel_value.item(1))
            pixel_displacement = math.sqrt(((x_start-x)^2) + ((y_start-y)^2))
            distance = int(distance) + pixel_displacement
            alteredIM_blacked[x][y] = pixel_color_holder

    distance = distance/jcount

    ####### Display Image########
    cv2.imshow("Here's your final picture", origIM_BlackBack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    x = 0
    cv2.imshow("Here's your final picture", alteredIM_blacked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow("Here's your final picture", origIM_BlackBack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return distance



def main():

    print(image_rotation("Cube.png", 360))










if __name__ == "__main__":
    main()
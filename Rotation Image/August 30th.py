import cv2
import numpy as np
import math


# code to read in an image
origIM = cv2.imread("Cube.png")
alteredIM = origIM
blackIM = alteredIM

# display an image
# cv2.imshow("Here's a picture", origIM)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




#images
imH= origIM.shape[0]
imW = origIM.shape[1]

imHA = alteredIM.shape[0]
imWA = alteredIM.shape[1]

imHB = blackIM.shape[0]
imWB = blackIM.shape[1]

#Make black images

black_image = np.zeros((imH, imW, 3))
black_image2 = black_image
black_image3 = black_image
black_image4 = black_image




#combine images
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

cv2.imshow("Here's a picture", fullIM)
cv2.waitKey(0)
cv2.destroyAllWindows()

######### move the image over and down################

origIM_BlackBack = cv2.imread("Final_combo.png")
IM_B_H = origIM_BlackBack.shape[0]
IM_B_W = origIM_BlackBack.shape[1]### new image is 600 by 1650
Down_Shift = int((IM_B_H // 3) + 1)
Right_Shift = int((IM_B_W // 3) + 1)


for i in range(imH):
    for j in range(imW):
        original_color = origIM_BlackBack[imH - i][imW - j]#Store the color of the picture
        #original_location = np.reshape([j, i], (1, 1))#Store the location of the picture
        black = origIM_BlackBack[IM_B_H - 1][IM_B_W - 1]
        #new_color = origIM_BlackBack[(i + Down_Shift)][(j + Right_Shift)]#color of pixel to be overwritten
        origIM_BlackBack[((imH - i) + Down_Shift)][((imW - j) + Right_Shift)] = original_color# change black pixel to picture
        origIM_BlackBack[imH - i][imW - j] = black


cv2.imshow("Here's origIM_BlackBack", origIM_BlackBack)
cv2.waitKey(0)
cv2.destroyAllWindows()








####create an empty image
####zero matrix (height, width, color channels)
#### your image size will have to be big enough to handle size rotation, meaning there will have to be a blank
####image that is created around your image in order to rotate the image without losing pixels

# backdrop_height = int(newIM.shape[0] * 150/100)
# backdrop_width = int(newIM.shape[1] * 150/100)
# backdrop_dimensions = (backdrop_width, backdrop_height)
#
#newIM.resize(backdrop_dimensions)
newIM = np.zeros((imH, imW, 3), np.float32)

niH = newIM.shape[0]
niW = newIM.shape[1]

A = cv2.getRotationMatrix2D((niW/2, niH/2), 90, 1.0)
rotated90 = cv2.warpAffine(newIM, A, (niH, niW))

B = cv2.getRotationMatrix2D((imW, imH), 180, 1.0)
rotate180 = cv2.warpAffine(origIM, B, (imW, imH))

# print(range(imH))#int number of pixels
# print(range(imW))#int number of pixels




#Iterate through you image, need to finish from her code
# for i in range(imH):#access the y coordinate in the matrix
#     for j in range(imW):#access the x coordinate in the matrix
#         for k in range(3):#access the R/G/B color value
#             #syntax fo raccessing individual pixels
#             #newIM[i][j][k] = origIM[i][j][k] ###her code for iterating through the pixels
#             print(k)

x = math.radians(60)

rm0_0 = math.cos(x)
rm0_1 = (-1)*math.sin(x)
rm1_0 = math.sin(x)
rm1_1 = math.cos(x)

rotation_matrix_r = np.array([[math.cos(x), -math.sin(x)],[math.sin(x), math.cos(x)]])
print(rotation_matrix_r)
print(origIM[0][1])
a = 0
b = 0
icount = 0
jcount = 0
j_length = range(imW)
i_length = range(imH)
alteredIM = origIM_BlackBack.copy()
alteredIM_blacked = np.zeros_like(alteredIM)
#alteredIM_blacked = np.zeros((2000, 2000))

Down_Shift = int((IM_B_H // 3) + 1)
Right_Shift = int((IM_B_W // 3) + 1)
black = origIM_BlackBack[IM_B_H - 1][IM_B_W - 1]



for i in range(imH):#access the y coordinate in the matrix
    icount = icount + 1
    for j in range(imW):#access the x coordinate in the matrix
        jcount = jcount + 1

        x_start = (imW + Right_Shift) - j
        y_start = (imH + Down_Shift) - i

        pixel_color_holder = origIM_BlackBack[y_start][x_start]
        #pixel_place_array = np.reshape([i,j],(2,1))
        pixel_place_array = np.reshape([(y_start),(x_start)] , (2, 1))

        rotated_pixel_value = np.matmul(rotation_matrix_r, pixel_place_array)
        test = rotated_pixel_value

        rotated_pixel_value1 = rotated_pixel_value.item(0)# the array value r0c0
        rotated_pixel_value1 = int(rotated_pixel_value1)# round off the calculated value
        rotated_pixel_value2 = rotated_pixel_value.item(1)# the array value r1c0
        rotated_pixel_value2 = int(rotated_pixel_value2)#round off the value
        rotated_pixel_value[0] = rotated_pixel_value1#set the array to the rounded values
        rotated_pixel_value[1] = rotated_pixel_value2#set the array to the rounded values
        ## rotated_pixel_value is now the new spot that the color for origIM should go to
        ## color of pixel_place_array is stored in pixel_color_holder

        rotated_pixel_value[0,0] = rotated_pixel_value1
        rotated_pixel_value[1,0] = rotated_pixel_value2

        # print(rotated_pixel_value)
        # print()

        x = int(rotated_pixel_value.item(0))
        y = int(rotated_pixel_value.item(1))
        # print()
        # print(x)
        # print(y)
        # print(rotated_pixel_value)
        # print(x_start)
        # print(y_start)
        # print(jcount)
        # print(icount)
        # print()
        alteredIM_blacked[x][y] = pixel_color_holder
        #alteredIM[y_start][x_start] = black

        ### alteredIM(rpv) should be the pixel we want to change to the color from the origIM color
        # print(alteredIM[x][y])



cv2.imshow("Here's your final picture", alteredIM_blacked)
cv2.waitKey(0)
cv2.destroyAllWindows()








#for k in range(3):
            #pixel_place_array = np.array([i, j])
            #pixel_color_holder = origIM[i][j]

            #test_holder = origIM[i][j][k] #iterates through the color array

            #rotated_pixel_value = np.matmul(pixel_place_array, rotation_matrix_r)
            #print(origIM[i][j])
            #print(origIM[i][j])
            #Rotated_value =             #syntax fo raccessing individual pixels
            #newIM[i][j][k] = origIM[i][j][k] ###her code for iterating through the pixels
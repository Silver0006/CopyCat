import pyautogui, cv2, pytesseract

#These need to have a way to be refreshed or auto updated
Primary_Monitor_Resolution = pyautogui.size()
App_Window_Names = pyautogui.getAllTitles()

Search_Term = input("Type in text to search for: ")
print("Resolution: " + str(Primary_Monitor_Resolution))
Current_Image_Info = pyautogui.screenshot('Current_Image.png')
print("Image has been created")
Current_Image = cv2.imread("Current_Image.png")
Current_Image_Grayscale = cv2.cvtColor(Current_Image, cv2.COLOR_BGR2GRAY)
Image_Data = pytesseract.image_to_data(Current_Image_Grayscale, output_type=pytesseract.Output.DICT)
for i in range(len(Image_Data['text'])):
    #print(Image_Data["text"][i] + " " + str(Image_Data["left"][i]) + " " + str(Image_Data["top"][i]))
    if Image_Data["text"][i] == Search_Term:
        print(str(Image_Data["left"][i]) + " " + str(Image_Data["top"][i]))

exit(0)
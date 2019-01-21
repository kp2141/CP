#Whatsapp autonomous code write msg


from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input("Enter the name of user or group :")
msg = input("Enter your message:")
count = int(input("Rtner the count no:"))

input("Enter anything after scanning Qr code")
#title means the user name(Type the user name)
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

#grabing the class name of the input box of the whatsapp

msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    msg_box.send_keys(msg)
    #grabbing the submit button of the
    button  = driver.find_element_by_class_name('_35EW6')
    button.click()
from selenium import webdriver
from time import sleep

url = 'https://www.google.com/search?q=machine+learning&rlz=1C1CHBF_enUS1009US1009&sxsrf=ALiCzsaqkOpEcPpNuq1lLz_F14kM6s2Gaw%3A1657815465105&ei=qUHQYsz1BfPz9APZwL-gCg&ved=0ahUKEwiM7pnv4_j4AhXzOX0KHVngD6QQ4dUDCA4&uact=5&oq=machine+learning&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyCggAELEDEIMBEEMyBAgAEEMyBAgAEEMyBAguEEMyBAgAEEMyEAgAEIAEEIcCELEDEIMBEBQyCwgAEIAEELEDEIMBMggIABCABBDJAzoFCAAQkQI6EQguEIAEELEDEIMBEMcBENEDOgcILhDUAhBDOgQILhAnOhAILhCxAxCDARDHARDRAxBDOgoILhDHARCvARBDOgcIIxDqAhAnOg4ILhCABBCxAxDHARDRAzoLCC4QxwEQrwEQkQI6CgguEMcBENEDEEM6CAguEIAEELEDOg4ILhCABBCxAxDHARCvAToHCAAQsQMQQzoLCAAQsQMQgwEQkQI6BwgjELECECc6CggAELEDEIMBEAo6BwgAEMkDEAo6BwgAELEDEAo6BwgAEIAEEAo6CggAEIAEEMkDEApKBAhBGABKBAhGGABQAFjmKGCWKmgIcAF4AYABkQGIAe4PkgEEMTUuN5gBAKABAbABCsABAQ&sclient=gws-wiz'
browser = webdriver.Chrome()
sleep(3)
browser.quit()


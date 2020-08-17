from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import emojis

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\diretorio\geckodriver.exe')
    
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comente_na_foto('uri da foto')

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(2,5)/30)

    def comente_na_foto(self, href_foto):
        i = 0
        while i<10:
            driver = self.driver
            driver.get("https://www.instagram.com/p/"+ href_foto +"/")

            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

            try:
            	comentario = 'comentario'
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_xpath("//textarea[@placeholder='Adicione um comentário...']")
                time.sleep(random.randint(2,5))
                campo_comentario.clear()
                self.digite_como_uma_pessoa(random.choice(comentario), campo_comentario)
                time.sleep(random.randint(5,10))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(5)
                i += 1
                print(i)
            except Exception as e:
                print(e)
                i = 11


matheusBot = InstagramBot('username', 'password')
matheusBot.login()
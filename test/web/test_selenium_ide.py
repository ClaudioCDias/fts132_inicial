# 1 - Importar Bibliotecas / Pacotes

import pytest  # Framework de Teste de Unidade / Engine / Motor
import time  # Controle do Tempo
import json  # Ler e Escrever no formato Json
from selenium import webdriver  # Bibliotecas do Selenium WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 2 - Classe e Definições
class TestConsultaPreparatrioCTFLAT():
    def setup_method(self, method):
        # Instanciar o objeto do Selenium WebDriver como Chrome
        self.driver = webdriver.Chrome('C:/Users/Claudio/PycharmProjects/fts132_inicial/drivers/chromedriver109/chromedriver.exe')
        self.driver.implicitly_wait(30)  # O robô irá esperar por até 30 segundos pelos elementos
        self.driver.maximize_window()  # Maximizar a janela do navegador
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_consultaPreparatrioCTFLAT(self):
        self.driver.get("https://www.iterasys.com.br/pt")
        self.driver.set_window_size(1366, 728)
        time.sleep(3)  # pausa forçada / "alfinete" / sempre deve remover antes de salvar no repositório
        self.driver.find_element(By.CSS_SELECTOR, "#\\31 6237702146520 > .item-pill").click()
        self.driver.find_element(By.CSS_SELECTOR, ".feature-list-item:nth-child(4) .feature-nav-hover").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        assert self.driver.find_element(By.CSS_SELECTOR, "h1:nth-child(1)").text == "Preparatório CTFL-AT"
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".content-purchase-info:nth-child(2) .content-price-installments-amount").text == "R$ 24,83"
        time.sleep(30) # pausa forçada / "alfinete" / sempre deve remover antes de salvar no repositório


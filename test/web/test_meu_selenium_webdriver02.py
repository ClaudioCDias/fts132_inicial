#1 Importar Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC
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

#2 Classe
class Test_selenium_webdriver():

    # Definição de Início - Executa Antes do teste
    def setup_method(self, method):
        # Declarar o objeto do Selenium e instanciar como o navegador desejado
        self.driver = webdriver.Chrome('C:/Users/Claudio/PycharmProjects/fts132_inicial/drivers/chromedriver109/chromedriver.exe')
        self.driver.implicitly_wait(30) # O Selenium vai esperar até três segundos pelos elementos
        self.driver.maximize_window() # Maximizar a janela do navegador

    # Definição de Fim - Executa depois do teste
    def teardown_method(self, method):
        # Destruir o objeto do Selenium
        self.driver.quit()

    # Definição do Teste
    @pytest.mark.parametrize('termo, curso, preço',[
        ('ctfl-at', 'ctfl-at', 'R$ 24,83'),
        ('ctfl', 'preparatório ctfl', 'R$ 199,00'),
    ])
    def testar_comprar_curso_PreparatorioCTFLAT(self, termo, curso, preco):
        # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br/pt')
        # O Selenium clica na caixa de pesquisa
        # self.driver.find_element(By.ID, 'searchtext').click()
        # O Selenium apaga o conteúdo da caixa de pesquisa
        # self.driver.find_element(By.ID, 'searchtext').clear()
        # O Selenium escreve mantis na caixa de pesquisa
        # self.driver.find_element(By.ID, 'searchtext').send_keys(termo)
        # O Selenium clica no botão cursos
        self.driver.find_element(By.ID, '16237702146520').click()
        # O selenium clica em preparatorio ctfl-at
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/pt/cursos/preparatorio-ctfl-at"] div').click()
        # O Selenium valida o nome do curso no carrinho de compras
        time.sleep(30)
        assert self.driver.find_element(By.CSS_SELECTOR, 'h1[style="--fg:#283252; --primary-light:#77CCA6;"]').text == curso
        # O Selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'p[class="content-price-installments-amount"]').text == preco


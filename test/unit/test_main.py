import pytest

from main import (somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros,
                  elevar_um_numero_pelo_outro, calcular_area_do_quadrado, calcular_area_do_retangulo,
                  calcular_area_do_triangulo, calcular_area_do_circulo, calcular_volume_do_paralelograma)

def testar_somar_dois_numeros():
    # 1ª Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / InPut
    num1 = 4
    num2 = 5
    # Saída / OutPut
    resultado_esperado = 9

    # 2ª Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_subtrair_dois_numeros():
    # 1 - Configura
    # Dados / Valores
    # Entrada / InPut
    num1 = 7
    num2 = 5
    # Saída / OutPut
    resultado_esperado = 2

    # 2 - Executa
    resultado_atual = subtrair_dois_numeros(num1, num2)

    # 3 - Valida
    assert resultado_atual == resultado_esperado

def testar_multiplicar_dois_numeros():
    # 1 - Configura
    # Dados / Valores
    # Entrada / InPut
    num1 = 3
    num2 = 5
    # Saída / OutPut
    resultado_esperado = 15

    # 2 - Executa
    resultado_atual = multiplicar_dois_numeros(num1, num2)

    # 3 - Valida
    assert resultado_atual == resultado_esperado

def testar_dividir_dois_numeros():
    # 1 - Configura
    # Dados / Valores
    # Entrada / InPut
    num1 = 8
    num2 = 4
    # Saída / OutPut
    resultado_esperado = 2

    # 2 - Executa
    resultado_atual = dividir_dois_numeros(num1, num2)

    # 3 - Valida
    assert resultado_atual == resultado_esperado

def testar_elevar_um_numero_pelo_outro():
    # 1 - Configura
    # Dados / Valores
    # Entrada / InPut
    num1 = 2
    num2 = 3
    # Saída / OutPut
    resultado_esperado = 8

    # 2 - Executa
    resultado_atual = elevar_um_numero_pelo_outro(num1, num2)

    # 3 - Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_quadrado():
    # 1 - Configura
    # Dados / Valores
    # Entrada / InPut
    area = 3
    # Saída / OutPut
    resultado_esperado = 9

    # 2 - Executa
    resultado_atual = calcular_area_do_quadrado(area)

    # 3 - Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_retangulo():
    # 1 - Configura
    # Dados / Valores
    # Entrada / InPut
    Lado1 = 6
    Lado2 = 9
    # Saída / OutPut
    resultado_esperado = 54

    # 2 - Executa
    resultado_atual = calcular_area_do_retangulo(Lado1, Lado2)

    # 3 - Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_triangulo():
    # 1 - Configura
    # Dados / Valores
    # Entrada / InPut
    Lado1 = 7
    Lado2 = 10
    # Saída / OutPut
    resultado_esperado = 35

    # 2 - Executa
    resultado_atual = calcular_area_do_triangulo(Lado1, Lado2)

    # 3 - Valida
    assert resultado_atual == resultado_esperado

#anotação para utilizar como massa de teste
@pytest.mark.parametrize('raio,resultado_esperado',[
                             # valores
                             (1, 3.14),   # teste nº 1
                             (2, 12.56),  # teste nº 2
                             (3, 28.26),  # teste nº 3
                             (4, 50.24),  # teste nº 4
                             ('a', 'Falha no Calculo - Raio não é um número'), # teste nº 5
                             (' ', 'Falha no Calculo - Raio não é um número'), # teste nº 6
                         ])
def testar_calcular_area_do_circulo(raio, resultado_esperado):
    # 1 - Configura / Comentamos para que os parametros sejam lidos
    #raio = 2
    #resultado_esperado = 12.56

    # 2 - Executa
    resultado_atual = calcular_area_do_circulo(raio)

    # 3 - Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_volume_do_paralelograma():
    # 1 - Configura
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100

    # 2 - Executa
    resultado_atual = calcular_volume_do_paralelograma(largura, comprimento, altura)

    # 3 - Valida
    assert resultado_atual == resultado_esperado

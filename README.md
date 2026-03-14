# 🎭 Real-Time Face Filter (Haar Cascades)

Este projeto é uma aplicação de Visão Computacional desenvolvida em Python que utiliza classificadores em cascata (**Haar Cascades**) para detectar rostos em tempo real via webcam e sobrepor filtros dinâmicos com suporte a transparência (Canal Alfa).

## 🚀 Funcionalidades

* **Detecção em Tempo Real:** Identifica faces utilizando o algoritmo de Viola-Jones.
* **Alpha Blending:** Sobreposição inteligente de imagens PNG, preservando a transparência e garantindo que o filtro não cubra o fundo de forma quadrada.
* **Ajuste Dinâmico:** O filtro redimensiona e reposiciona automaticamente conforme a aproximação ou afastamento do usuário da câmera.

## 🛠️ Tecnologias Utilizadas

* [Python 3.x](https://www.python.org/)
* [OpenCV](https://opencv.org/) (Processamento de imagem e detecção facial)
* [NumPy](https://numpy.org/) (Manipulação de matrizes matemáticas)

## 📦 Instalação e Uso

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Instale as dependências:**

   ```bash
   pip install opencv-python numpy
   ```

3. **Execute a aplicação:**

   ```bash
   python maskin.py
   ```

4. Pressione a tecla **'q'** para encerrar a aplicação.

## 🧠 Como funciona?

O projeto utiliza o arquivo `haarcascade_frontalface_default.xml` do OpenCV. O computador busca padrões de contraste (Haar Features) que assemelham-se à anatomia humana.

### Mistura de Pixels (Alpha Blending)

Para sobrepor a máscara sem o fundo branco, utilizamos o Canal Alfa (transparência) para calcular a intensidade de cada pixel:

```math
Pixel_{final} = (Filtro \times Alfa) + (Webcam \times (1 - Alfa))
```

## 🧪 Observações da Investigação

Durante os testes, foram observados os seguintes comportamentos:

* **Perfil:** O algoritmo falha ao virar o rosto, pois o classificador utilizado é treinado apenas para faces frontais.
* **Oclusão:** Cobrir a boca ou os olhos reduz drasticamente a precisão da detecção.
* **Flickering:** A máscara pode "piscar" devido a variações de iluminação ou ruído digital que quebram o padrão de contraste momentaneamente.

Desenvolvido para fins acadêmicos de estudo em Visão Computacional.

**Desenvolvido por:** Artur Tabosa Rodrigues Reis e
                      Gabriel Loyo de Holanda Lisboa

# Criação de um Chatbot simples com PyTorch. 
A base deste projeto pode ser encontrada em https://github.com/patrickloeber/pytorch-chatbot.

- Implementação baseada em Rede Neural Direta com 2 camadas ocultas;
- As customizações nas mensagem devem ser feitas nos arquivos `intents.json` ou `intents_por.json`, este  último para mensagem em português.

## Treinamento do modelo
O modelo é treina com a biblioteca `nltk`, utilizando `nltk.stem.porter.PorterStemmer` para a versão em inglês e `nltk.stem.RSLPStemmer` para a versão em português para o tratamento das palavras e utilizando a PyTorch para treinar a rede neural. Após o treinamento é gerado um arquivo `data.pth` onde o modelo treinado é salvo.

## Chat
O chat utiliza o modelo treinado para devolver, de forma aleatória, uma resposta baseada na categorização da mensagem.

## Aplicação
A aplicação consiste em uma tela, como na imagem abaixo, construida com TKinter, onde a mensagem é enviada e retornada pela função de construção do chat.

![image](https://github.com/felipesbreve/chatbot/assets/72587609/0245dff8-f308-41ad-8b2b-2edc5145ad2f)

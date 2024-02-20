## Funcionalidades Específicas

- Contador de Movimentos: Conta quantas repetições de um exercício específico foram realizadas.
- Classificação de Movimento: Determina se o movimento realizado é "limpo" ou correto, baseando-se em critérios pré-definidos.
- Cálculo de Cadência: Calcula a cadência do movimento, ou seja, a rapidez com que as repetições são realizadas.
- Visualização de Dados: Exibe dados em tempo real, como o ângulo dos braços, o número de repetições e a cadência do exercício.

## Passos básicos no Flutter

- Estabelecer Conexão WebSocket:
Utilize o pacote web_socket_channel para criar uma conexão WebSocket com o servidor.

- Capturar Imagem da Câmera:
Com o pacote camera, inicie a câmera e configure um loop para capturar frames em intervalos regulares ou baseado em alguma interação do usuário.

- Enviar Frame para o Servidor:
Codifique o frame capturado (por exemplo, como um JPEG) e envie para o servidor via WebSocket. Provavelmente, você precisará converter a imagem para um formato de dados binários ou base64.

- Receber Resposta do Servidor:
Trate as mensagens recebidas do servidor, que podem conter informações ou análises baseadas no frame enviado.

## Lado do Servidor (Python)

No servidor Python, você precisará adaptar o método handle_message para lidar com os dados da imagem recebidos, processá-los (por exemplo, utilizando OpenCV para análise de imagem) e enviar uma resposta adequada de volta ao cliente.

Adaptações no servidor:

- Recebimento de Frames:
O método handle_message deve ser capaz de descompactar os dados da imagem recebida, convertendo-os de volta para uma forma que possa ser processada por bibliotecas como OpenCV.

- Processamento de Imagem:
Utilize OpenCV ou outra biblioteca de processamento de imagem para analisar o frame recebido, realizar detecções, contagens, etc.

-Envio de Resposta:
Envie os resultados do processamento de volta ao cliente Flutter via WebSocket.

Importante:
Performance e Latência: Enviar frames de vídeo em tempo real através de WebSocket pode ser desafiador em termos de performance e latência. Ajustes na resolução e taxa de quadros podem ser necessários.
Codificação de Dados: Atenção à codificação e decodificação de imagens entre o formato binário e a representação utilizada no WebSocket.
Segurança: Considere aspectos de segurança, especialmente se as imagens processadas contiverem informações sensíveis.

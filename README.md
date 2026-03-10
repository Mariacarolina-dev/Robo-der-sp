===============================================================================
          ROBÔ DE CONSULTA DER-SP (PLACA/AIT) - GUIA DO USUÁRIO
===============================================================================

Este software automatiza a consulta de multas e protocolos no portal oficial 
do DER-SP. Ele foi desenvolvido para processar múltiplas consultas de forma 
rápida e segura.

-------------------------------------------------------------------------------
1. PRÉ-REQUISITOS PARA O USUÁRIO FINAL
-------------------------------------------------------------------------------
Para que o programa funcione corretamente no seu computador, certifique-se de:
- Ter o Google Chrome instalado e atualizado.
- Ter uma conexão ativa com a internet (o robô precisa acessar o site do DER).
- O Windows pode exibir um alerta de "Fornecedor Desconhecido" ao abrir o .exe
  pela primeira vez. Clique em "Mais informações" e "Executar assim mesmo".

-------------------------------------------------------------------------------
2. COMO INSTALAR E RODAR
-------------------------------------------------------------------------------
O programa é "Portable" (Portátil), o que significa que não precisa de um 
instalador complexo:
1. Crie uma pasta em um local de fácil acesso (ex: Área de Trabalho ou Documentos).
2. Cole o arquivo "Consulta_DER.exe" dentro desta pasta.
3. Dê um clique duplo para abrir. 
   *Nota: Na primeira vez, ele pode demorar alguns segundos para carregar as 
    bibliotecas internas.*

-------------------------------------------------------------------------------
3. PASSO A PASSO DE USO (DENTRO DO PROGRAMA)
-------------------------------------------------------------------------------
Passo 1: Prepare suas listas.
   - Na coluna da ESQUERDA, cole as PLACAS (uma por linha).
   - Na coluna da DIREITA, cole os números de AIT (um por linha).
   IMPORTANTE: A quantidade de Placas deve ser a mesma de AITs.

Passo 2: Inicie a Consulta.
   - Clique no botão VERDE "Consultar".
   - Uma janela do navegador Chrome será aberta automaticamente. 
   - ATENÇÃO: Não feche ou mexa na janela do navegador que o robô abriu, 
     pois isso interromperá o processo.

Passo 3: Verifique os Resultados.
   - Assim que o robô terminar, os dados aparecerão na tabela inferior.
   - Para copiar uma linha específica (Placa, AIT, Situação e Protocolo), 
     clique com o botão DIREITO sobre a linha e escolha "Copiar".

Passo 4: Finalização.
   - Ao terminar todas as consultas, o robô exibirá um aviso de "Concluído" 
     e fechará o navegador automaticamente.

-------------------------------------------------------------------------------
4. SOLUÇÃO DE PROBLEMAS (FAQ)
-------------------------------------------------------------------------------
- O NAVEGADOR FECHOU SOZINHO: Isso acontece se houver erro de conexão ou se 
  o site do DER estiver fora do ar. Tente clicar em "Consultar" novamente.
- ERRO DE "WEBDRIVER": Verifique se o seu Google Chrome está atualizado. O 
  robô tenta baixar o driver correto sozinho, mas precisa de internet para isso.
- O PROGRAMA TRAVOU: A interface foi projetada para não travar (Multithread), 
  mas se o computador estiver muito lento, aguarde alguns segundos.

-------------------------------------------------------------------------------
5. SUPORTE E CRÉDITOS
-------------------------------------------------------------------------------
Desenvolvido por: Maria Carolina
Versão: 1.0 (2026)
Tecnologias: Python, Selenium & Tkinter.
===============================================================================

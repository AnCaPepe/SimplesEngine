# -*- coding: cp1252 -*-
# Permite acentos e cedilha nos coment�rios

from GameLogicInterface import getStringValue
#valor{s} = getStringValue(chave{s}): Obter valor de string global

from GameLogicInterface import setStringValue
#setStringValue(chave{s},valor{s}): Definir valor de string global

from GameLogicInterface import getNumberValue
#valor{i} = getNumberValue(chave{s}): Obter valor num�rico global

from GameLogicInterface import setNumberValue
#setNumberValue(chave{s},valor{i}): Definir valor num�rico global

from GameLogicInterface import actorsNumber
#valor{i} = actorsNumber(): Obter n�mero de objetos ativos

from GameLogicInterface import elapsedTime
#valor{i} = elapsedTime(): Intervalo de tempo(ms) desde a �ltima atualiza��o

from GameLogicInterface import getMapSize
#(largura{i},altura{i}) = getMapSize(): Dimens�es do mapa em pixels

from GameLogicInterface import isCharId
#valor{i} = isCharId(id{i}): Verifica se objeto �(1) ou n�o(0) personagem

from GameLogicInterface import getObjIdState
#estado{i} = getCharIdState(id{i}): Obter estado de objeto de ID fornecido

from GameLogicInterface import setItemId
#setItemId(id{i},estado{i}[,�cone{s},escala{f}]): Define estado (> 0), �cone e escala (opcionais)de item de ID fornecido

from GameLogicInterface import setCharId
#setCharId(id{i},estado{i}[,configura��o{s},escala{f}]): Define estado (> 0), arquivo de configura��o e escala (opcionais) de personagem de ID fornecido

from GameLogicInterface import objIdCollision
#valor{i} = objIdCollision(id1{i},id2{i}): Verfica colis�o(1) ou n�o(0) entre objetos de IDs fornecidos

from GameLogicInterface import createItem
#colis�o{i} = createItem((x{i},y{i})[,�cone{s},escala{f}]):
#Insere item no mapa na posi��o fornecida, usando (opcional) �cone e escala definidos
#Retorna -1 se item for criado em regi�o obstru�da (por mapa ou outro objeto)

from GameLogicInterface import createChar
#colis�o{i} = createChar((x{i},y{i})[,configura��o{s},escala{f},controles{s}]):
#Insere personagem no mapa na posi��o fornecida usando (opcional) arquivo de configura��o, escala e arquivo de controles definidos
#Retorna -1 se personagem for criado em regi�o obstru�da (por mapa ou outro objeto)

from GameLogicInterface import deleteObjId
#deleteObjId(id{i}): Deleta objeto de ID fornecido

from GameLogicInterface import registerValue
#registerValue(valor{i}): Registra valor num�rico no sistema de Log

from GameLogicInterface import getObjIdPos
#(x{i},y{i}) = getObjIdPos(id{i}): Obter posi��o do objeto de ID fornecido

from GameLogicInterface import setObjIdPos
#colis�o{i} = setObjIdPos(id{i},(x{i},y{i})): Define posi��o do objeto de ID fornecido
#Retorna -1 se objeto for criado em regi�o obstru�da (por mapa ou outro objeto)

from GameLogicInterface import endGame
#endGame(tela{s}): Termina gameplay ( vai para tela especificada )

from GameLogicInterface import getEposIdValue
#valor{i} = getEposIdValue(id{i},tipo{i}): Obter da Epos de ID fornecido valor do tipo especificado

from GameLogicInterface import setEposIdState
#setEposIdState(id{i},modo{i}[,ativo{i},vel{i},acel{i},desacel{i}]):
#Define modo de opera��o e estado (ativo ou n�o, opcional) da Epos de ID fornecido

from GameLogicInterface import works
#Teste

position, velocity, current = range( 3 )

clientBegin, clientKeep, clientEnd = range( 1, 4 ) 

stepDirectionMode = -6   #Motor de passo
masterEncoderMode = -5   #Usa posi��o de refer�ncia
currentMode = -3         #Modo de corrente
velocityMode = -2        #Modo de velocidade
positionMode = -1        #Modo de posi��o
profilePositionMode = 1  #Modo de posicionamento com perfil definido
profileVelocityMode = 3  #Modo de velocidade com perfil definido
homingMode = 6

#Recomendo copiar tudo acima para o seu arquivo de inicializa��o

import random
import math

SR, SL, SD, SU, WR, WL, WD, WU = range( 8 ) 

setNumberValue("game_points", 0)
setNumberValue("game_time", 0)
setNumberValue("total_game_time", 50)
total_game_time = getNumberValue("total_game_time")
remaining_game_time_ms = total_game_time * 1000;

playerId = createChar((150,150), "Caipira", 1.0, "key_config.txt")

id1 = createChar((300,150), "Aranha")
id2 = createChar((400,300), "Ifrit")

num_items = 0
while num_items < 10:
   x = random.randrange( getMapSize()[0] )
   y = random.randrange( getMapSize()[1] )
   image = random.randrange( 1, 4 )
   if createItem((x, y), "food" + str(image) + ".png", 0.25) > 0:
      num_items += 1

setNumberValue("num_items", num_items)

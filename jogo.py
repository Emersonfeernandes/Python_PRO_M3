import pygame
from time import sleep
from classes.objeto import Carro

pygame.init()

largura = 600
altura = 400

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('City')

velo = 2
pos = 0
posf = 0
posc2 = 600
jog = 100
jog1 = 270
jog2 = 1000


cenario_01 = pygame.image.load('ima/CENARIO_01.png').convert_alpha()
cenario_02 = pygame.image.load('ima/CENARIO_02.png').convert_alpha()
#jogador = pygame.image.load('ima/TON_01.png').convert_alpha()
#andar = pygame.image.load('ima/TON_02.png').convert_alpha()

class Jogador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.sprites = []
		self.sprites.append(pygame.image.load('ima/TON/TON_01.png'))
		self.sprites.append(pygame.image.load('ima/TON/TON_02.png'))
		self.sprites.append(pygame.image.load('ima/TON/TON_03.png'))
		self.sprites.append(pygame.image.load('ima/TON/TON_04.png'))
		self.sprites.append(pygame.image.load('ima/TON/TON_05.png'))
		self.sprites.append(pygame.image.load('ima/TON/TON_06.png'))
		self.primera = 0
		self.image = self.sprites[self.primera]

		self.rect = self.image.get_rect()
		self.rect.topleft = 50, 302
		self.passo = False
	def andar(self):
		self.passo = True
	def update(self):
		if self.passo == True:
			self.primera = self.primera + 0.25
			if self.primera >= len(self.sprites):
				self.primera = 0
				self.passo = False
			self.image = self.sprites[int(self.primera)]


grupo_sprites = pygame.sprite.Group()
jogador = Jogador()
grupo_sprites.add(jogador)
carro = Carro()
grupo_sprites.add(carro)

relogio = pygame.time.Clock()
run = True
while run:
	relogio.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	carro.correr()

	comandos = pygame.key.get_pressed()
	if comandos[pygame.K_RIGHT]:
		sleep(0.03)
		if posf == -600:
			posf = 600
		if posc2 == -600:
			posc2 = 600
		if jog == 200:
		   posf -= velo
		   posc2 -= velo
		jog += velo
		if jog > 200:
			jog = 200
	tela.blit(cenario_01, (posf, pos))
	tela.blit(cenario_02, (posc2, pos))
	if comandos[pygame.K_RIGHT]:
		jogador.andar()
	grupo_sprites.draw(tela)
	grupo_sprites.update()



	pygame.display.update()



pygame.quit()

f = open("./files/outputdemo1.txt", "w",encoding='utf8')
x="Mais de mil cidades e aldeias em toda a Ucrânia continuam " \
  "\nsem electricidade por causa dos ataques russos dos últimos dias, " \
  "\ndizem responsáveis ucranianos citados pela BBC. Os ataques tiveram como " \
  "\nalvo, muitas vezes, a infra-estrutura energética do país e, segundo o " \
  "\nPresidente Volodymyr Zelensky, destruíram 30% das centrais eléctricas da Ucrânia."
print(f.write(x))
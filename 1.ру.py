    def give_line(line):
       with open(KR.txt, encoding='UTF-8') as f:
           слово, частьречи, чтотоещё = line.split('|')
           частьречи= частьречи.split()
	   частьречислова=частьречи[0]
	   return частьречислова
